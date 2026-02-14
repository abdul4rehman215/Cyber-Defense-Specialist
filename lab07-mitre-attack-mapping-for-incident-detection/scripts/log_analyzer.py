#!/usr/bin/env python3
import re
import json
from mitre_parser import MitreAttackParser

class LogAnalyzer:
    def __init__(self, mitre_parser):
        self.mitre = mitre_parser
        self.findings = []
        self.rules = {
            "T1059.001": [r"powershell.*-enc"],
            "T1003.001": [r"mimikatz", r"lsass.exe"],
            "T1543.003": [r"service.*started", r"malicious_svc"],
            "T1071.001": [r"http", r"https"],
            "T1046": [r"port:445", r"smb"]
        }

    def analyze_log(self, file_path):
        with open(file_path, "r", errors="ignore") as f:
            for line in f:
                for tid, patterns in self.rules.items():
                    for pattern in patterns:
                        if re.search(pattern, line, re.IGNORECASE):
                            technique = self.mitre.get_technique_by_id(tid)
                            if technique:
                                self.findings.append({
                                    "technique_id": tid,
                                    "technique": technique["name"],
                                    "log": line.strip()
                                })

    def generate_report(self, output_file):
        report = {
            "total_findings": len(self.findings),
            "findings": self.findings
        }
        with open(output_file, "w") as f:
            json.dump(report, f, indent=2)

if __name__ == "__main__":
    parser = MitreAttackParser()
    analyzer = LogAnalyzer(parser)

    analyzer.analyze_log("../logs/windows_security.log")
    analyzer.analyze_log("../logs/linux_auth.log")
    analyzer.analyze_log("../logs/network.log")

    analyzer.generate_report("../reports/analysis_report.json")
