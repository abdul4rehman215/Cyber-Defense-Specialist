#!/usr/bin/env python3
import json

def display_results(report_file):
    with open(report_file, "r") as f:
        report = json.load(f)

    print("Total Findings:", report["total_findings"])
    for fnd in report["findings"]:
        print(f"[{fnd['technique_id']}] {fnd['technique']} -> {fnd['log']}")

if __name__ == "__main__":
    display_results("../reports/analysis_report.json")
