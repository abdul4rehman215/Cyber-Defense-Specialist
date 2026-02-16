#!/usr/bin/env python3

import json
import datetime
import subprocess
import shutil
from pathlib import Path


class IncidentResponder:

    def __init__(self):
        self.base_dir = Path.home() / "incident_response"
        self.config_dir = self.base_dir / "config"
        self.alerts_dir = self.base_dir / "alerts"
        self.logs_dir = self.base_dir / "logs"

        self.alerts_dir.mkdir(exist_ok=True)

        self.load_config()

        self.response_actions = {
            "critical": ["block_ip", "send_alert", "create_ticket", "backup_logs"],
            "high": ["block_ip", "send_alert", "create_ticket"],
            "medium": ["log_incident", "send_notification"],
            "low": ["log_incident"]
        }

    def load_config(self):

        config_file = self.config_dir / "response_config.json"

        if not config_file.exists():
            raise FileNotFoundError("response_config.json not found")

        with open(config_file, "r") as f:
            self.config = json.load(f)

    def block_source_ip(self, ip_address):

        if ip_address in self.config["blocking"]["whitelist_ips"]:
            return False

        if not self.config["blocking"]["use_iptables"]:
            print(f"[SIMULATION] Blocking IP {ip_address}")
            return True

        try:
            subprocess.run(
                ["sudo", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"],
                check=True
            )
            return True
        except Exception:
            return False

    def send_alert_email(self, incident_data):

        print("\n=== ALERT EMAIL ===")
        print(f"Incident Type: {incident_data['incident_type']}")
        print(f"Severity: {incident_data['severity']}")
        print(f"Source IP: {incident_data['source_ip']}")
        print(f"Log: {incident_data['raw_log']}")
        print("===================\n")

        return True

    def create_incident_ticket(self, incident_data):

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        ticket_id = f"INC-{timestamp}-{incident_data['incident_type'].upper()}"

        ticket = {
            "ticket_id": ticket_id,
            "created_at": timestamp,
            "incident": incident_data
        }

        ticket_file = self.alerts_dir / f"{ticket_id}.json"

        with open(ticket_file, "w") as f:
            json.dump(ticket, f, indent=4)

        print(f"[INFO] Ticket created: {ticket_id}")

        return ticket_id

    def backup_logs(self):

        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = self.alerts_dir / f"log_backup_{timestamp}"

        shutil.copytree(self.logs_dir, backup_dir)

        print(f"[INFO] Logs backed up to {backup_dir}")

        return str(backup_dir)

    def log_response_action(self, action_type, action_data):

        log_file = self.alerts_dir / "response_actions.log"

        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": action_type,
            "details": action_data
        }

        with open(log_file, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def respond_to_incident(self, incident):

        severity = incident["severity"]
        actions = self.response_actions.get(severity, [])

        results = {"incident": incident, "actions_taken": []}

        for action in actions:

            if action == "block_ip":
                success = self.block_source_ip(incident["source_ip"])
                self.log_response_action("block_ip", incident["source_ip"])
                results["actions_taken"].append("block_ip")

            elif action == "send_alert":
                self.send_alert_email(incident)
                self.log_response_action("send_alert", incident["incident_type"])
                results["actions_taken"].append("send_alert")

            elif action == "create_ticket":
                ticket_id = self.create_incident_ticket(incident)
                self.log_response_action("create_ticket", ticket_id)
                results["actions_taken"].append("create_ticket")

            elif action == "backup_logs":
                backup_path = self.backup_logs()
                self.log_response_action("backup_logs", backup_path)
                results["actions_taken"].append("backup_logs")

            elif action == "log_incident":
                self.log_response_action("log_incident", incident["incident_type"])
                results["actions_taken"].append("log_incident")

            elif action == "send_notification":
                print(f"[INFO] Notification sent for {incident['incident_type']}")
                self.log_response_action("send_notification", incident["incident_type"])
                results["actions_taken"].append("send_notification")

        return results

    def respond_to_multiple_incidents(self, incidents):

        total_actions = 0

        for incident in incidents:
            result = self.respond_to_incident(incident)
            total_actions += len(result["actions_taken"])

        print(f"[INFO] Total response actions executed: {total_actions}")


if __name__ == "__main__":

    responder = IncidentResponder()

    reports_dir = Path.home() / "incident_response" / "reports" / "incidents"
    report_files = sorted(reports_dir.glob("analysis_report_*.json"))

    if not report_files:
        print("No analysis reports found.")
        exit(1)

    latest_report = report_files[-1]

    with open(latest_report, "r") as f:
        report_data = json.load(f)

    incidents = report_data.get("incidents", [])

    responder.respond_to_multiple_incidents(incidents)
