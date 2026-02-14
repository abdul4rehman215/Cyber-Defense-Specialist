#!/usr/bin/env python3

import re
import sys
from collections import defaultdict

class HTTPParser:
    def __init__(self):
        self.suspicious_patterns = {
            'sql_injection': [r'union\s+select', r'drop\s+table', r"'.*or.*'"],
            'xss': [r'<script>', r'javascript:', r'onerror='],
            'path_traversal': [r'\.\./', r'%2e%2e'],
            'command_injection': [r';\s*(cat|ls|whoami)', r'\|.*\|']
        }

    def parse_request(self, request_text):
        lines = request_text.strip().splitlines()
        if not lines:
            return None

        first_line = lines[0].split()
        if len(first_line) < 3:
            return None

        method, path, version = first_line
        headers = {}

        for line in lines[1:]:
            if ':' in line:
                key, value = line.split(':', 1)
                headers[key.strip().lower()] = value.strip()

        return {
            'method': method,
            'path': path,
            'version': version,
            'headers': headers
        }

    def detect_anomalies(self, parsed_request):
        anomalies = []

        path = parsed_request.get('path', '').lower()
        headers = parsed_request.get('headers', {})

        for category, patterns in self.suspicious_patterns.items():
            for pattern in patterns:
                if re.search(pattern, path):
                    anomalies.append(category)

        user_agent = headers.get('user-agent', '')
        if not user_agent or len(user_agent) < 5:
            anomalies.append('unusual_user_agent')

        if 'x-forwarded-for' in headers:
            anomalies.append('proxy_header_detected')

        return list(set(anomalies))

    def generate_report(self, requests):
        method_count = defaultdict(int)
        anomaly_count = defaultdict(int)

        for req in requests:
            parsed = self.parse_request(req)
            if not parsed:
                continue

            method_count[parsed['method']] += 1
            anomalies = self.detect_anomalies(parsed)

            for anomaly in anomalies:
                anomaly_count[anomaly] += 1

        print("\nHTTP Traffic Analysis Report")
        print("=" * 40)
        print("\nRequest Methods:")
        for method, count in method_count.items():
            print(f"{method}: {count}")

        print("\nDetected Anomalies:")
        for anomaly, count in anomaly_count.items():
            print(f"{anomaly}: {count}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 http_parser.py <input_file>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        content = f.read()

    raw_requests = content.split("HTTP/1.1")
    parser = HTTPParser()
    parser.generate_report(raw_requests)

if __name__ == "__main__":
    main()
