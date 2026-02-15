#!/usr/bin/env python3

import json
import uuid
from typing import Dict, Any, List


class AutomatedResponder:

    def __init__(self):
        self.response_log = []

    def generate_response_actions(self, alert: Dict[str, Any]) -> List[str]:

        level = alert.get("priority_level", "LOW")

        if level == "CRITICAL":
            return [
                "Isolate affected host",
                "Notify SOC immediately",
                "Create incident ticket"
            ]

        if level == "HIGH":
            return [
                "Notify security analyst",
                "Create incident ticket",
                "Collect forensic data"
            ]

        if level == "MEDIUM":
            return [
                "Create investigation ticket",
                "Add to investigation queue"
            ]

        return ["Log for review"]

    def create_incident_ticket(self, alert: Dict[str, Any]) -> Dict[str, Any]:

        ticket = {
            "ticket_id": f"TKT-{uuid.uuid4().hex[:8].upper()}",
            "title": f"{alert.get('alert_type')} detected",
            "description": f"""
Alert ID: {alert.get('alert_id')}
Severity: {alert.get('severity')}
Asset: {alert.get('asset')}
Source IP: {alert.get('source_ip')}
Destination IP: {alert.get('destination_ip')}
""",
            "priority": alert.get("priority_level")
        }

        return ticket

    def generate_notification(self, alert: Dict[str, Any]) -> str:

        return f"""
=== Security Alert Notification ===
Alert ID: {alert.get('alert_id')}
Priority: {alert.get('priority_level')}
Type: {alert.get('alert_type')}
Asset: {alert.get('asset')}
Source IP: {alert.get('source_ip')}
"""

    def process_high_priority_alerts(self, alerts: List[Dict[str, Any]]) -> None:

        for alert in alerts:

            actions = self.generate_response_actions(alert)
            ticket = self.create_incident_ticket(alert)
            notification = self.generate_notification(alert)

            log_entry = {
                "alert_id": alert.get("alert_id"),
                "actions": actions,
                "ticket": ticket,
                "notification": notification
            }

            self.response_log.append(log_entry)

            print(notification)
            print("Actions:", actions)
            print("Ticket Created:", ticket["ticket_id"])
            print("-" * 50)

    def save_response_log(self, output_file: str) -> None:

        with open(output_file, "w") as f:
            json.dump(self.response_log, f, indent=4)


def main():

    print("=== Automated Response Test ===")

    with open("reports/high_priority_alerts.json", "r") as f:
        alerts = json.load(f)

    responder = AutomatedResponder()
    responder.process_high_priority_alerts(alerts)
    responder.save_response_log("reports/response_log.json")


if __name__ == "__main__":
    main()
