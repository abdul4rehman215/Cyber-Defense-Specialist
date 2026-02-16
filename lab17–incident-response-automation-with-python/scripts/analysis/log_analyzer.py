#!/usr/bin/env python3

import re
import json
import datetime
from pathlib import Path
from collections import defaultdict, Counter


class LogAnalyzer:

    def __init__(self):
        self.base_dir = Path.home() / "incident_response"
        self.logs_dir = self.base_dir / "logs"
        self.reports_dir = self.base_dir / "reports" / "incidents"

        self.security_patterns = {
            "failed_login": [
                r"Failed password for .+ from (\d+\.\d+\.\d+\.\d+)",
                r"FAILED LOGIN.*FROM (\d+\.\d+\.\d+\.\d+)"
            ],
            "sql_injection": [
                r"SQL injection",
                r"(\'\s*OR\s*\d+\s*=\s*\d+)"
            ],
            "xss_attempt": [
                r"<script.*?>",
                r"javascript:"
            ],
            "privilege_escalation": [
                r"sudo.*?rm\s+-rf",
                r"USER=root.*COMMAND="
            ]
        }

        self.severity_mapping = {
            "failed_login": "medium",
            "sql_injection": "high",
            "xss_attempt": "medium",
            "privilege_escalation": "critical"
        }

        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    def analyze_log_file(self, log_file):

        incidents = []

        with open(log_file, "r") as f:
            lines = f.readlines()

        for line in lines:
            for incident_type, patterns in self.security_patterns.items():
                for pattern in patterns:
                    match = re.search(pattern, line, re.IGNORECASE)
                    if match:
                        ip = match.group(1) if match.groups() else "unknown"

                        incident = {
                            "timestamp": self.timestamp,
                            "log_file": str(log_file),
                            "incident_type": incident_type,
                            "severity": self.severity_mapping[incident_type],
                            "source_ip": ip,
                            "raw_log": line.strip()
                        }

                        incidents.append(incident)

        return incidents

    def analyze_all_logs(self):

        all_incidents = []

        for subdir in self.logs_dir.iterdir():
            if subdir.is_dir():
                for log_file in subdir.glob("*.log"):
                    incidents = self.analyze_log_file(log_file)
                    all_incidents.extend(incidents)

        return all_incidents

    def categorize_incidents(self, incidents):

        categorized = {
            "by_type": defaultdict(list),
            "by_severity": defaultdict(list),
            "by_source_ip": defaultdict(list)
        }

        for incident in incidents:
            categorized["by_type"][incident["incident_type"]].append(incident)
            categorized["by_severity"][incident["severity"]].append(incident)
            categorized["by_source_ip"][incident["source_ip"]].append(incident)

        return categorized

    def calculate_statistics(self, incidents):

        stats = {
            "total_incidents": len(incidents),
            "by_type": Counter(),
            "by_severity": Counter(),
            "top_source_ips": Counter()
        }

        for incident in incidents:
            stats["by_type"][incident["incident_type"]] += 1
            stats["by_severity"][incident["severity"]] += 1
            stats["top_source_ips"][incident["source_ip"]] += 1

        stats["top_source_ips"] = dict(stats["top_source_ips"].most_common(5))
        stats["by_type"] = dict(stats["by_type"])
        stats["by_severity"] = dict(stats["by_severity"])

        return stats

    def generate_analysis_report(self, incidents, categorized, stats):

        report = {
            "generated_at": self.timestamp,
            "statistics": stats,
            "categorized_incidents": {
                "by_type": {k: len(v) for k, v in categorized["by_type"].items()},
                "by_severity": {k: len(v) for k, v in categorized["by_severity"].items()},
                "by_source_ip": {k: len(v) for k, v in categorized["by_source_ip"].items()}
            },
            "incidents": incidents
        }

        report_file = self.reports_dir / f"analysis_report_{self.timestamp}.json"

        with open(report_file, "w") as f:
            json.dump(report, f, indent=4)

        return report, str(report_file)

    def print_summary(self, stats):

        print("\n" + "="*50)
        print("INCIDENT ANALYSIS SUMMARY")
        print("="*50)
        print(f"Total Incidents: {stats['total_incidents']}")

        print("\nIncidents by Type:")
        for k, v in stats["by_type"].items():
            print(f" - {k}: {v}")

        print("\nIncidents by Severity:")
        for k, v in stats["by_severity"].items():
            print(f" - {k}: {v}")

        print("\nTop Source IPs:")
        for k, v in stats["top_source_ips"].items():
            print(f" - {k}: {v}")

        print("="*50)

    def run_analysis(self):

        print("[INFO] Starting log analysis")

        incidents = self.analyze_all_logs()
        categorized = self.categorize_incidents(incidents)
        stats = self.calculate_statistics(incidents)

        report, report_path = self.generate_analysis_report(
            incidents, categorized, stats
        )

        self.print_summary(stats)

        print(f"[INFO] Analysis report saved to {report_path}")


if __name__ == "__main__":
    analyzer = LogAnalyzer()
    analyzer.run_analysis()
