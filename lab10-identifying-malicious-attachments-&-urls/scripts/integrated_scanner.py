#!/usr/bin/env python3

import os
import re
import sys
import json
from datetime import datetime
from attachment_scanner import AttachmentScanner
from url_analyzer import URLAnalyzer


class EmailSecurityScanner:

    def __init__(self):
        self.attachment_scanner = AttachmentScanner()
        self.url_analyzer = URLAnalyzer()
        self.results = {
            'attachments': [],
            'urls': [],
            'overall_risk': 'CLEAN',
            'timestamp': datetime.now().isoformat()
        }

    def extract_urls_from_text(self, text):

        url_pattern = r'https?://[^\s]+'
        return re.findall(url_pattern, text)

    def analyze_email(self, email_file, attachments_dir):

        print("=" * 60)
        print("INTEGRATED EMAIL SECURITY SCAN")
        print("=" * 60)

        if not os.path.exists(email_file):
            print("Email file not found.")
            return

        with open(email_file, "r") as f:
            content = f.read()

        urls = self.extract_urls_from_text(content)

        print(f"\nFound URLs: {urls}")

        # Analyze URLs
        for url in urls:
            self.url_analyzer.analyze_url(url)

        self.url_analyzer.generate_report()
        self.results['urls'] = self.url_analyzer.results

        # Analyze Attachments
        if os.path.isdir(attachments_dir):
            for file in os.listdir(attachments_dir):
                full_path = os.path.join(attachments_dir, file)
                if os.path.isfile(full_path):
                    self.attachment_scanner.scan_file(full_path)

            self.attachment_scanner.generate_report()
            self.results['attachments'] = self.attachment_scanner.scan_results

        self.calculate_overall_risk()
        self.save_report()

    def calculate_overall_risk(self):

        total_score = 0

        for url in self.results['urls']:
            total_score += url.get("risk_score", 0)

        for attachment in self.results['attachments']:
            total_score += attachment.get("risk_score", 0)

        if total_score >= 100:
            level = "HIGH"
        elif total_score >= 50:
            level = "MEDIUM"
        elif total_score >= 10:
            level = "LOW"
        else:
            level = "CLEAN"

        self.results['overall_risk'] = level

        print("\nOverall Email Risk:", level)

    def save_report(self):

        os.makedirs("reports", exist_ok=True)

        output_file = f"reports/integrated_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        with open(output_file, "w") as f:
            json.dump(self.results, f, indent=4)

        print("Integrated report saved:", output_file)


def main():

    if len(sys.argv) != 3:
        print("Usage: python3 integrated_scanner.py <email_file> <attachments_dir>")
        sys.exit(1)

    email_file = sys.argv[1]
    attachments_dir = sys.argv[2]

    scanner = EmailSecurityScanner()
    scanner.analyze_email(email_file, attachments_dir)


if __name__ == "__main__":
    main()
