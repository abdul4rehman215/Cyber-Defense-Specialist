#!/usr/bin/env python3

import subprocess
import datetime
import os


class IncidentResponder:

    def __init__(self):
        self.log_path = os.path.expanduser("~/soc-lab/reports/incident_actions.txt")

    def block_ip(self, ip_address):

        try:
            subprocess.run(
                ["sudo", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"],
                check=True
            )
            self.log_action(f"Blocked IP {ip_address}")
        except Exception as e:
            print("Failed to block IP:", e)

    def collect_evidence(self):

        evidence_dir = os.path.expanduser("~/soc-lab/evidence")
        os.makedirs(evidence_dir, exist_ok=True)

        with open(f"{evidence_dir}/netstat.txt", "w") as f:
            subprocess.run(["netstat", "-tuln"], stdout=f)

        with open(f"{evidence_dir}/processes.txt", "w") as f:
            subprocess.run(["ps", "aux"], stdout=f)

        with open(f"{evidence_dir}/login_history.txt", "w") as f:
            subprocess.run(["last", "-20"], stdout=f)

        self.log_action("Evidence collected.")

    def backup_firewall(self):

        evidence_dir = os.path.expanduser("~/soc-lab/evidence")
        subprocess.run(
            ["sudo", "iptables-save"],
            stdout=open(f"{evidence_dir}/iptables_backup.txt", "w")
        )
        self.log_action("Firewall backup saved.")

    def create_incident_report(self, incident_type, details):

        report_file = os.path.expanduser("~/soc-lab/reports/final_incident_report.txt")

        with open(report_file, "w") as f:
            f.write("INCIDENT REPORT\n")
            f.write("=================================\n")
            f.write(f"Time: {datetime.datetime.now()}\n")
            f.write(f"Type: {incident_type}\n")
            f.write(f"Details: {details}\n")

        self.log_action("Incident report created.")

    def log_action(self, message):

        with open(self.log_path, "a") as f:
            f.write(f"{datetime.datetime.now()} - {message}\n")


def main():

    responder = IncidentResponder()

    responder.collect_evidence()
    responder.backup_firewall()
    responder.create_incident_report(
        "Simulated Incident",
        "Detected SSH brute force and port scan"
    )


if __name__ == "__main__":
    main()
