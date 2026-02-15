#!/usr/bin/env python3

import logging
import datetime
import json
import os
import subprocess


class BasePlaybook:

    def __init__(self, playbook_name, severity="medium"):

        self.playbook_name = playbook_name
        self.severity = severity
        self.start_time = datetime.datetime.now()
        self.incident_id = self._generate_incident_id()
        self.actions_log = []

        self._setup_logging()

    def _generate_incident_id(self):
        return f"INC-{datetime.datetime.now().strftime('%Y%m%d-%H%M%S')}"

    def _setup_logging(self):

        os.makedirs("logs/incidents", exist_ok=True)

        log_file = f"logs/incidents/{self.playbook_name}_{self.incident_id}.log"

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger(self.playbook_name)

    def log_action(self, action, status, details=""):

        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "incident_id": self.incident_id,
            "action": action,
            "status": status,
            "details": details
        }

        self.actions_log.append(entry)
        self.logger.info(json.dumps(entry))

    def execute_command(self, command, description=""):

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )

            success = result.returncode == 0
            output = result.stdout if success else result.stderr

            self.log_action(
                description or command,
                "SUCCESS" if success else "FAILED",
                output.strip()
            )

            return success, output

        except Exception as e:
            self.log_action(command, "ERROR", str(e))
            return False, str(e)

    def send_alert(self, message, priority="normal"):

        os.makedirs("logs/alerts", exist_ok=True)

        alert_entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "incident_id": self.incident_id,
            "priority": priority,
            "message": message
        }

        with open("logs/alerts/alerts.log", "a") as f:
            f.write(json.dumps(alert_entry) + "\n")

        self.log_action("Send Alert", "SUCCESS", message)

    def generate_report(self):

        os.makedirs("logs/reports", exist_ok=True)

        duration = (datetime.datetime.now() - self.start_time).total_seconds()

        report = {
            "incident_id": self.incident_id,
            "playbook": self.playbook_name,
            "severity": self.severity,
            "start_time": self.start_time.isoformat(),
            "duration_seconds": duration,
            "actions": self.actions_log
        }

        report_path = f"logs/reports/{self.playbook_name}_{self.incident_id}.json"

        with open(report_path, "w") as f:
            json.dump(report, f, indent=4)

        self.log_action("Generate Report", "SUCCESS", report_path)

        return report_path
