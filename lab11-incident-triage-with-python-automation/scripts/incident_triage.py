#!/usr/bin/env python3

import json
import datetime
import os
from typing import List, Dict, Any
from alert_enrichment import AlertEnricher


class IncidentTriageEngine:

    def __init__(self, rules_file: str):
        self.rules = self.load_rules(rules_file)
        self.processed_alerts = []
        self.false_positives = []
        self.high_priority_alerts = []
        self.enricher = AlertEnricher()

    def load_rules(self, rules_file: str) -> Dict[str, Any]:
        try:
            with open(rules_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Rules file not found. Using default rules.")
            return {
                "whitelist": {"users": [], "source_ips": [], "assets": []},
                "severity_weights": {},
                "alert_type_weights": {}
            }

    def load_alerts(self, alerts_file: str) -> List[Dict[str, Any]]:
        try:
            with open(alerts_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Alerts file not found.")
            return []

    def is_whitelisted(self, alert: Dict[str, Any]) -> bool:

        whitelist = self.rules.get("whitelist", {})

        if alert.get("user") in whitelist.get("users", []):
            return True

        if alert.get("source_ip") in whitelist.get("source_ips", []):
            return True

        if alert.get("asset") in whitelist.get("assets", []):
            return True

        return False

    def calculate_priority_score(self, alert: Dict[str, Any]) -> int:

        score = 0

        severity_weights = self.rules.get("severity_weights", {})
        alert_type_weights = self.rules.get("alert_type_weights", {})

        score += severity_weights.get(alert.get("severity"), 0)
        score += alert_type_weights.get(alert.get("alert_type"), 0)

        if alert.get("event_count", 0) > 10:
            score += 2

        source_ip = alert.get("source_ip", "")
        if not (source_ip.startswith("192.168.") or
                source_ip.startswith("10.") or
                source_ip.startswith("172.16.")):
            score += 3

        return score

    def triage_alert(self, alert: Dict[str, Any]) -> Dict[str, Any]:

        triage_result = alert.copy()
        triage_result['triage_timestamp'] = datetime.datetime.now().isoformat()

        if self.is_whitelisted(alert):
            triage_result['triage_status'] = "FALSE_POSITIVE"
            triage_result['priority_score'] = 0
            triage_result['priority_level'] = "NONE"
        else:
            score = self.calculate_priority_score(alert)
            triage_result['priority_score'] = score
            triage_result['triage_status'] = "LEGITIMATE"

            if score >= 15:
                triage_result['priority_level'] = "CRITICAL"
            elif score >= 10:
                triage_result['priority_level'] = "HIGH"
            elif score >= 5:
                triage_result['priority_level'] = "MEDIUM"
            else:
                triage_result['priority_level'] = "LOW"

        return triage_result

    def process_alerts(self, alerts: List[Dict[str, Any]]) -> None:

        print(f"Processing {len(alerts)} alerts...")

        for alert in alerts:

            enriched_alert = self.enricher.enrich_alert(alert)
            triaged = self.triage_alert(enriched_alert)

            self.processed_alerts.append(triaged)

            if triaged['triage_status'] == "FALSE_POSITIVE":
                self.false_positives.append(triaged)

            if triaged.get("priority_level") in ["CRITICAL", "HIGH"]:
                self.high_priority_alerts.append(triaged)

        print(f"Triage complete. Found {len(self.false_positives)} false positives")

    def generate_summary_report(self) -> str:

        total = len(self.processed_alerts)
        false_pos = len(self.false_positives)
        legit = total - false_pos

        priority_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}

        for alert in self.processed_alerts:
            level = alert.get("priority_level")
            if level in priority_counts:
                priority_counts[level] += 1

        report = f"""
=== Incident Triage Summary ===
Total Alerts: {total}
False Positives: {false_pos}
Legitimate Alerts: {legit}

Priority Breakdown:
CRITICAL: {priority_counts['CRITICAL']}
HIGH: {priority_counts['HIGH']}
MEDIUM: {priority_counts['MEDIUM']}
LOW: {priority_counts['LOW']}

High Priority Alerts:
"""

        for alert in self.high_priority_alerts:
            report += f"- {alert['alert_id']} ({alert['alert_type']}) [{alert['priority_level']}]\n"

        return report

    def save_results(self, output_dir: str) -> None:

        os.makedirs(output_dir, exist_ok=True)

        with open(os.path.join(output_dir, "processed_alerts.json"), "w") as f:
            json.dump(self.processed_alerts, f, indent=4)

        with open(os.path.join(output_dir, "false_positives.json"), "w") as f:
            json.dump(self.false_positives, f, indent=4)

        with open(os.path.join(output_dir, "high_priority_alerts.json"), "w") as f:
            json.dump(self.high_priority_alerts, f, indent=4)

        with open(os.path.join(output_dir, "triage_summary.txt"), "w") as f:
            f.write(self.generate_summary_report())


def main():

    print("=== Incident Triage Automation System ===")

    engine = IncidentTriageEngine("rules/triage_rules.json")

    alerts = engine.load_alerts("data/sample_alerts.json")

    engine.process_alerts(alerts)

    summary = engine.generate_summary_report()
    print(summary)

    engine.save_results("reports")

    print("\nTriage automation complete!")


if __name__ == "__main__":
    main()
