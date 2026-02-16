#!/usr/bin/env python3

"""
Threat Intelligence Report Generator
Complete implementation for Ubuntu 24.04 (Python 3.12)
"""

import json
import os
from datetime import datetime
from collections import Counter


class ReportGenerator:

    def __init__(self, data_file):
        self.data_file = data_file
        self.data = self.load_data(data_file)
        self.indicators = self.data.get("indicators", [])
        self.metadata = self.data.get("metadata", {})
        self.report_sections = []

    def load_data(self, data_file):

        if not os.path.exists(data_file):
            raise FileNotFoundError(f"Normalized data file not found: {data_file}")

        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "indicators" not in data:
            raise ValueError("Invalid normalized data structure")

        return data

    def generate_executive_summary(self):

        total = len(self.indicators)
        high = len([i for i in self.indicators if i["severity"] == "HIGH"])
        medium = len([i for i in self.indicators if i["severity"] == "MEDIUM"])
        low = len([i for i in self.indicators if i["severity"] == "LOW"])

        type_counter = Counter(i["type"] for i in self.indicators)

        summary = f"""
EXECUTIVE SUMMARY
-----------------
Report Generated: {datetime.utcnow().isoformat()}

Total Indicators: {total}
High Severity: {high}
Medium Severity: {medium}
Low Severity: {low}

Top Indicator Types:
"""

        for t, count in type_counter.items():
            summary += f" - {t}: {count}\n"

        return summary

    def generate_severity_breakdown(self):

        total = len(self.indicators)
        severity_counts = Counter(i["severity"] for i in self.indicators)

        breakdown = "\nSEVERITY BREAKDOWN\n------------------\n"

        for severity in ["HIGH", "MEDIUM", "LOW", "INFO"]:
            count = severity_counts.get(severity, 0)
            percentage = (count / total * 100) if total > 0 else 0
            breakdown += f"{severity}: {count} ({percentage:.2f}%)\n"

        return breakdown

    def generate_indicator_type_analysis(self):

        total = len(self.indicators)
        type_counts = Counter(i["type"] for i in self.indicators)

        analysis = "\nINDICATOR TYPE ANALYSIS\n-----------------------\n"

        for indicator_type, count in type_counts.items():
            percentage = (count / total * 100) if total > 0 else 0
            analysis += f"{indicator_type}: {count} ({percentage:.2f}%)\n"

        return analysis

    def generate_top_threats(self, limit=10):

        sorted_indicators = sorted(
            self.indicators,
            key=lambda x: x.get("risk_score", 0),
            reverse=True
        )

        top = sorted_indicators[:limit]

        section = "\nTOP THREATS\n-----------\n"

        for idx, indicator in enumerate(top, start=1):
            section += (
                f"{idx}. {indicator['value']} "
                f"(Type: {indicator['type']}, "
                f"Risk: {indicator['risk_score']}, "
                f"Severity: {indicator['severity']}, "
                f"Confidence: {indicator['confidence']})\n"
            )

        return section

    def generate_text_report(self, output_file):

        content = ""
        content += self.generate_executive_summary()
        content += self.generate_severity_breakdown()
        content += self.generate_indicator_type_analysis()
        content += self.generate_top_threats()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

    def generate_html_report(self, output_file):

        html_content = f"""
<html>
<head>
    <title>Threat Intelligence Report</title>
    <style>
        body {{ font-family: Arial; margin: 40px; }}
        h1 {{ color: #2c3e50; }}
        table {{ border-collapse: collapse; width: 80%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>Threat Intelligence Report</h1>
    <pre>
{self.generate_executive_summary()}
{self.generate_severity_breakdown()}
{self.generate_indicator_type_analysis()}
{self.generate_top_threats()}
    </pre>
</body>
</html>
"""

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_content)

    def generate_json_report(self, output_file):

        severity_counts = Counter(i["severity"] for i in self.indicators)
        type_counts = Counter(i["type"] for i in self.indicators)

        report_data = {
            "generated_at": datetime.utcnow().isoformat(),
            "total_indicators": len(self.indicators),
            "severity_breakdown": dict(severity_counts),
            "type_breakdown": dict(type_counts),
            "top_threats": sorted(
                self.indicators,
                key=lambda x: x.get("risk_score", 0),
                reverse=True
            )[:10]
        }

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=4)


def main():

    print("Threat Intelligence Report Generator")
    print("=" * 50)

    try:
        data_files = sorted(
            [f for f in os.listdir("data") if f.startswith("normalized_")]
        )

        if not data_files:
            raise FileNotFoundError("No normalized data files found in data/")

        latest_file = os.path.join("data", data_files[-1])

        generator = ReportGenerator(latest_file)

        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")

        text_output = f"reports/threat_report_{timestamp}.txt"
        html_output = f"reports/threat_report_{timestamp}.html"
        json_output = f"reports/threat_report_{timestamp}.json"

        generator.generate_text_report(text_output)
        generator.generate_html_report(html_output)
        generator.generate_json_report(json_output)

        print("\nReports Generated Successfully:")
        print(f"Text Report: {text_output}")
        print(f"HTML Report: {html_output}")
        print(f"JSON Report: {json_output}")

    except Exception as e:
        print(f"Error during report generation: {e}")


if __name__ == "__main__":
    main()
