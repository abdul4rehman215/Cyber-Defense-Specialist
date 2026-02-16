#!/usr/bin/env python3

import json
import os
from datetime import datetime
from collections import defaultdict


class WazuhAnalyzer:

    def __init__(self, log_file="/var/ossec/logs/alerts/alerts.json"):
        self.log_file = log_file
        self.alerts = []
        self.stats = defaultdict(int)

    def load_alerts(self):

        if not os.path.exists(self.log_file):
            print("Alert file not found.")
            return

        with open(self.log_file, "r") as f:
            for line in f:
                try:
                    self.alerts.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

    def analyze_severity(self):

        for alert in self.alerts:
            level = alert.get("rule", {}).get("level", 0)
            self.stats[f"level_{level}"] += 1

            if level >= 10:
                self.stats["high_priority"] += 1

    def detect_brute_force(self):

        ip_failures = defaultdict(list)

        for alert in self.alerts:
            if "authentication failed" in str(alert).lower():
                ip = alert.get("data", {}).get("srcip", "unknown")
                timestamp = alert.get("timestamp")
                ip_failures[ip].append(timestamp)

        suspicious_ips = []
        for ip, attempts in ip_failures.items():
            if len(attempts) >= 5:
                suspicious_ips.append(ip)

        self.stats["brute_force_ips"] = suspicious_ips

    def generate_report(self):

        report_path = os.path.expanduser("~/soc-lab/reports/wazuh_report.txt")

        with open(report_path, "w") as f:
            f.write("WAZUH SECURITY ANALYSIS REPORT\n")
            f.write(f"Generated: {datetime.now()}\n\n")

            for key, value in self.stats.items():
                f.write(f"{key}: {value}\n")

        print("Wazuh report generated.")
        print(f"High priority alerts: {self.stats.get('high_priority', 0)}")


def main():

    analyzer = WazuhAnalyzer()
    analyzer.load_alerts()
    analyzer.analyze_severity()
    analyzer.detect_brute_force()
    analyzer.generate_report()


if __name__ == "__main__":
    main()
