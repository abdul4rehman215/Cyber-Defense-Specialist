#!/usr/bin/env python3

import sys
import os
import shutil

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_playbook import BasePlaybook


class SystemIsolationPlaybook(BasePlaybook):

    def __init__(self):
        super().__init__("system_isolation", "critical")
        self.evidence_files = []
        self.network_isolated = False

    def collect_system_info(self):

        evidence_dir = f"logs/incidents/evidence_{self.incident_id}"
        os.makedirs(evidence_dir, exist_ok=True)

        commands = {
            "processes.txt": "ps aux",
            "network.txt": "netstat -tuln",
            "logins.txt": "last -n 50",
            "env.txt": "env"
        }

        for filename, command in commands.items():
            success, output = self.execute_command(
                command,
                f"Collect {filename}"
            )

            if success:
                file_path = os.path.join(evidence_dir, filename)
                with open(file_path, "w") as f:
                    f.write(output)
                self.evidence_files.append(file_path)

        if os.path.exists("/var/log/auth.log"):
            shutil.copy("/var/log/auth.log", evidence_dir)
            self.evidence_files.append(
                os.path.join(evidence_dir, "auth.log")
            )

        self.log_action("Collect System Info", "SUCCESS")

    def collect_memory_info(self):

        evidence_dir = f"logs/incidents/evidence_{self.incident_id}"

        files = ["/proc/meminfo", "/proc/cpuinfo"]

        for file in files:
            if os.path.exists(file):
                shutil.copy(file, evidence_dir)
                self.evidence_files.append(
                    os.path.join(evidence_dir, os.path.basename(file))
                )

        self.execute_command("lsmod", "Collect Kernel Modules")

        self.log_action("Collect Memory Info", "SUCCESS")

    def isolate_network(self):

        # Backup current iptables
        self.execute_command(
            "sudo iptables-save > logs/incidents/iptables_backup.rules",
            "Backup iptables"
        )

        # Block incoming and outgoing traffic
        self.execute_command(
            "sudo iptables -P INPUT DROP",
            "Block Incoming Traffic"
        )

        self.execute_command(
            "sudo iptables -P OUTPUT DROP",
            "Block Outgoing Traffic"
        )

        self.network_isolated = True
        self.log_action("Network Isolation", "SUCCESS")

    def disable_services(self, services=['apache2', 'nginx', 'mysql']):

        for service in services:
            self.execute_command(
                f"sudo systemctl stop {service}",
                f"Stop Service {service}"
            )

        self.log_action("Disable Services", "SUCCESS")

    def create_evidence_archive(self):

        evidence_dir = f"logs/incidents/evidence_{self.incident_id}"
        archive_path = f"logs/incidents/evidence_{self.incident_id}"

        shutil.make_archive(archive_path, 'zip', evidence_dir)

        self.log_action(
            "Create Evidence Archive",
            "SUCCESS",
            archive_path + ".zip"
        )

        return archive_path + ".zip"

    def restore_network(self):

        self.execute_command(
            "sudo iptables-restore < logs/incidents/iptables_backup.rules",
            "Restore iptables"
        )

        self.network_isolated = False
        self.log_action("Restore Network", "SUCCESS")

    def run(self):

        self.log_action("Playbook Start", "STARTED")

        self.send_alert(
            "CRITICAL INCIDENT - System Isolation Initiated",
            "critical"
        )

        self.collect_system_info()
        self.collect_memory_info()
        self.isolate_network()
        self.disable_services()

        archive = self.create_evidence_archive()

        self.generate_report()

        self.send_alert(
            f"System isolated. Evidence stored at {archive}",
            "critical"
        )

        self.log_action("Playbook Complete", "SUCCESS")


if __name__ == "__main__":
    playbook = SystemIsolationPlaybook()
    playbook.run()
