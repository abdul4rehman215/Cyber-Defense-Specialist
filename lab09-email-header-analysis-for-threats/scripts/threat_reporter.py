#!/usr/bin/env python3

from header_analyzer import EmailAnalyzer
from spf_validator import SPFValidator
from dkim_validator import DKIMValidator
from dmarc_validator import DMARCValidator
from email import message_from_file
from email.utils import parseaddr
from datetime import datetime
import os
import json
import re


class ThreatReporter:

    def __init__(self):
        self.header_analyzer = EmailAnalyzer()
        self.spf_validator = SPFValidator()
        self.dkim_validator = DKIMValidator()
        self.dmarc_validator = DMARCValidator()

    def analyze_email(self, email_file):

        report = {
            'file': email_file,
            'timestamp': datetime.now().isoformat(),
            'header_analysis': {},
            'spf_result': None,
            'dkim_result': None,
            'dmarc_result': None,
            'threat_score': 0,
            'threat_level': 'UNKNOWN',
            'recommendations': []
        }

        if not os.path.exists(email_file):
            print("File not found.")
            return report

        with open(email_file, 'r') as f:
            message = message_from_file(f)

        routing = self.header_analyzer.analyze_received_path(message)
        spoofing = self.header_analyzer.check_spoofing(message)
        content = self.header_analyzer.analyze_content(message)

        score, level = self.header_analyzer.calculate_threat_score(
            spoofing, content, routing
        )

        report['header_analysis'] = {
            "routing": routing,
            "spoofing": spoofing,
            "content": content
        }

        from_header = message.get('From', '')
        sender_email = parseaddr(from_header)[1]
        domain = sender_email.split('@')[-1] if sender_email else None

        sender_ip = None
        received_headers = message.get_all('Received', [])

        if received_headers:
            match = re.search(r'\[(\d+\.\d+\.\d+\.\d+)\]', received_headers[0])
            if match:
                sender_ip = match.group(1)

        # SPF Validation
        if domain and sender_ip:
            report['spf_result'] = self.spf_validator.validate_ip(domain, sender_ip)
        else:
            report['spf_result'] = "None"

        # DKIM Validation
        report['dkim_result'] = self.dkim_validator.validate_signature(email_file)

        # DMARC Validation
        report['dmarc_result'] = self.dmarc_validator.validate_policy(
            domain if domain else "unknown",
            report['spf_result'],
            report['dkim_result']
        )

        total_score = score

        # Adjust score based on authentication failures
        if report['spf_result'] == "Fail":
            total_score += 3

        if not report['dkim_result']:
            total_score += 3

        if report['dmarc_result'] in ["Reject", "Quarantine"]:
            total_score += 4

        report['threat_score'] = total_score

        if total_score >= 15:
            report['threat_level'] = "HIGH"
        elif total_score >= 8:
            report['threat_level'] = "MEDIUM"
        elif total_score > 0:
            report['threat_level'] = "LOW"
        else:
            report['threat_level'] = "MINIMAL"

        report['recommendations'] = self.generate_recommendations(report)

        return report

    def generate_recommendations(self, report):

        recommendations = []

        if report['spf_result'] != "Pass":
            recommendations.append("Verify SPF configuration for sender domain.")

        if not report['dkim_result']:
            recommendations.append("DKIM signature validation failed or missing.")

        if report['dmarc_result'] in ["Reject", "Quarantine"]:
            recommendations.append("DMARC policy indicates enforcement action.")

        if report['threat_level'] == "HIGH":
            recommendations.append("Block email and investigate sender immediately.")

        if report['threat_level'] == "MEDIUM":
            recommendations.append("Flag email for manual security review.")

        return recommendations

    def export_report(self, report, output_file):

        os.makedirs("output", exist_ok=True)

        with open(output_file, 'w') as f:
            json.dump(report, f, indent=4)

    def print_report(self, report):

        print("\n" + "="*60)
        print(f"EMAIL THREAT REPORT: {report['file']}")
        print("="*60)
        print(f"Threat Score : {report['threat_score']}")
        print(f"Threat Level : {report['threat_level']}")
        print(f"SPF Result   : {report['spf_result']}")
        print(f"DKIM Result  : {report['dkim_result']}")
        print(f"DMARC Result : {report['dmarc_result']}")
        print("Recommendations:")
        for rec in report['recommendations']:
            print(f" - {rec}")
        print("="*60)


def main():

    reporter = ThreatReporter()

    samples = [
        'samples/legitimate.eml',
        'samples/phishing.eml',
        'samples/malware.eml'
    ]

    for sample in samples:
        report = reporter.analyze_email(sample)
        reporter.print_report(report)
        reporter.export_report(report, f"output/{sample.split('/')[-1]}.json")


if __name__ == "__main__":
    main()
