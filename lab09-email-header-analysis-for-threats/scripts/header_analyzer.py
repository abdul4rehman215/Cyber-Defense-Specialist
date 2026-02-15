#!/usr/bin/env python3

import re
import os
from email import message_from_file
from email.utils import parseaddr


class EmailAnalyzer:

    def __init__(self):
        self.threat_keywords = ['urgent', 'verify', 'suspended', 'click here', 'act now']
        self.suspicious_domains = ['bit.ly', 'tinyurl.com']

    def parse_email(self, filepath):

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"{filepath} not found")

        with open(filepath, 'r') as f:
            return message_from_file(f)

    def extract_headers(self, message):

        headers = {}
        important = [
            'From',
            'To',
            'Subject',
            'Return-Path',
            'Reply-To',
            'Received',
            'X-Originating-IP',
            'Message-ID'
        ]

        for header in important:
            headers[header] = message.get_all(header)

        return headers

    def analyze_received_path(self, message):

        received_headers = message.get_all('Received', [])
        servers = []
        suspicious_ips = []

        ip_pattern = r'\[(\d+\.\d+\.\d+\.\d+)\]'

        for header in received_headers:

            match = re.search(r'from\s+([^\s]+)', header)
            if match:
                servers.append(match.group(1))

            ip_match = re.search(ip_pattern, header)
            if ip_match:
                ip = ip_match.group(1)

                # Example logic to flag suspicious IP ranges
                if ip.startswith("203.") or ip.startswith("198."):
                    suspicious_ips.append(ip)

        return {
            'hops': len(received_headers),
            'servers': servers,
            'suspicious_ips': suspicious_ips
        }

    def check_spoofing(self, message):

        indicators = []

        from_header = message.get('From', '')
        reply_to = message.get('Reply-To', '')
        return_path = message.get('Return-Path', '')

        from_email = parseaddr(from_header)[1]
        reply_email = parseaddr(reply_to)[1]
        return_email = parseaddr(return_path)[1]

        # Check From vs Reply-To mismatch
        if reply_email and from_email != reply_email:
            indicators.append("From and Reply-To mismatch")

        # Check From vs Return-Path mismatch
        if return_email and from_email:
            from_domain = from_email.split('@')[-1]
            return_domain = return_email.split('@')[-1]

            if from_domain != return_domain:
                indicators.append("From and Return-Path domain mismatch")

        return indicators

    def analyze_content(self, message):

        suspicious = []

        subject = message.get('Subject', '').lower()

        for keyword in self.threat_keywords:
            if keyword in subject:
                suspicious.append(f"Suspicious subject keyword: {keyword}")

        attachment = message.get('X-Attachment', '')

        if attachment.endswith('.exe'):
            suspicious.append("Executable attachment detected")

        return suspicious

    def calculate_threat_score(self, spoofing, content, routing):

        score = 0

        score += len(spoofing) * 3
        score += len(content) * 2
        score += len(routing['suspicious_ips']) * 4

        if score >= 10:
            level = "HIGH"
        elif score >= 5:
            level = "MEDIUM"
        elif score > 0:
            level = "LOW"
        else:
            level = "MINIMAL"

        return score, level

    def analyze(self, filepath):

        print(f"\n{'='*60}")
        print(f"ANALYZING: {filepath}")
        print(f"{'='*60}")

        message = self.parse_email(filepath)

        headers = self.extract_headers(message)
        routing = self.analyze_received_path(message)
        spoofing = self.check_spoofing(message)
        content = self.analyze_content(message)

        score, level = self.calculate_threat_score(spoofing, content, routing)

        print(f"Threat Score: {score}")
        print(f"Threat Level: {level}")
        print(f"Spoofing Indicators: {spoofing}")
        print(f"Content Indicators: {content}")
        print(f"Routing Analysis: {routing}")


def main():

    analyzer = EmailAnalyzer()

    samples = [
        'samples/legitimate.eml',
        'samples/phishing.eml',
        'samples/malware.eml'
    ]

    for sample in samples:
        analyzer.analyze(sample)


if __name__ == "__main__":
    main()
