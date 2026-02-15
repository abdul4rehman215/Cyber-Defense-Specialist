#!/usr/bin/env python3

import sys
import os
import logging
import time
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from connectors.wazuh_connector import WazuhConnector
from connectors.thehive_connector import TheHiveConnector
from playbooks.malware_response import MalwareResponsePlaybook
from playbooks.bruteforce_response import BruteForceResponsePlaybook


class WorkflowOrchestrator:

    def __init__(self, config: dict):

        self.config = config

        self.wazuh = WazuhConnector(
            config["wazuh"]["url"],
            config["wazuh"]["username"],
            config["wazuh"]["password"]
        )

        self.thehive = TheHiveConnector(
            config["thehive"]["url"]
        )

        self.malware_playbook = MalwareResponsePlaybook()
        self.bruteforce_playbook = BruteForceResponsePlaybook()

        logging.info("Workflow Orchestrator initialized")

    def process_alerts(self, poll_interval: int = 60):

        logging.info("Starting alert processing loop")

        while True:
            try:
                alerts = self.wazuh.get_alerts(
                    limit=10,
                    min_level=self.config["wazuh"]["min_alert_level"]
                )

                for alert in alerts:

                    playbook_name = self.route_alert(alert)

                    if not playbook_name:
                        continue

                    results = self.execute_playbook(playbook_name, alert)

                    case_id = self.create_case_from_alert(alert, results)

                    logging.info(f"Created case {case_id} for alert")

                time.sleep(poll_interval)

            except KeyboardInterrupt:
                logging.info("Graceful shutdown requested")
                break

            except Exception as e:
                logging.error(f"Processing error: {e}")
                time.sleep(poll_interval)

    def route_alert(self, alert: dict) -> str:

        rule_id = alert.get("rule", {}).get("id")

        if rule_id in self.config["playbooks"]["malware_detection"]["rule_ids"]:
            return "malware_detection"

        if rule_id in self.config["playbooks"]["brute_force"]["rule_ids"]:
            return "brute_force"

        return None

    def execute_playbook(self, playbook_name: str, alert: dict) -> dict:

        try:
            if playbook_name == "malware_detection":
                return self.malware_playbook.execute(alert)

            elif playbook_name == "brute_force":
                return self.bruteforce_playbook.execute(alert)

            else:
                logging.warning("Unknown playbook requested")
                return {}

        except Exception as e:
            logging.error(f"Playbook execution error: {e}")
            return {}

    def create_case_from_alert(self, alert: dict, playbook_results: dict) -> str:

        title = f"Alert {alert.get('rule', {}).get('description', 'Unknown')}"

        description = f"""
Alert Details:
Agent: {alert.get('agent', {}).get('name')}
Rule ID: {alert.get('rule', {}).get('id')}
Severity: {alert.get('rule', {}).get('level')}

Playbook Results:
{playbook_results}
"""

        case_id = self.thehive.create_case(
            title=title,
            description=description,
            severity=3,
            tags=["SOAR", "Automated"]
        )

        if case_id:
            src_ip = alert.get("data", {}).get("srcip")
            if src_ip:
                self.thehive.add_observable(case_id, "ip", src_ip)

        return case_id
