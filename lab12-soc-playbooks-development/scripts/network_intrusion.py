#!/usr/bin/env python3

import sys
import os
import re
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from base_playbook import BasePlaybook


class NetworkIntrusionPlaybook(BasePlaybook):

    def __init__(self):
        super().__init__("network_intrusion", "high")
        self.suspicious_ips = []
        self.blocked_ips = []
        self.suspicious_ports = []

    def analyze_connections(self):

        # Check listening ports
        success, output = self.execute_command(
            "netstat -tuln",
            "List Listening Ports"
        )

        if success:
            for line in output.splitlines():
                if any(port in line for port in ["1234", "4444", "31337"]):
                    port = re.findall(r":(\d+)", line)
                    if port:
                        self.suspicious_ports.append(port[0])

        # Check active connections
        success, output = self.execute_command(
            "netstat -tun",
            "List Active Connections"
        )

        ip_counter = defaultdict(int)

        if success:
            for line in output.splitlines():
                match = re.findall(r"(\d+\.\d+\.\d+\.\d+)", line)
                for ip in match:
                    ip_counter[ip] += 1

        for ip, count in ip_counter.items():
            if count > 10 and not self.is_private_ip(ip):
                self.suspicious_ips.append(ip)

        self.log_action(
            "Analyze Connections",
            "SUCCESS",
            f"Suspicious IPs: {len(self.suspicious_ips)}, Ports: {len(self.suspicious_ports)}"
        )

    def check_auth_logs(self):

        if not os.path.exists("/var/log/auth.log"):
            return

        ip_counter = defaultdict(int)

        with open("/var/log/auth.log", "r", errors="ignore") as f:
            for line in f:
                if "Failed password" in line:
                    match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)
                    if match:
                        ip_counter[match.group(1)] += 1

        for ip, count in ip_counter.items():
            if count >= 5:
                self.suspicious_ips.append(ip)

        self.log_action(
            "Check Auth Logs",
            "SUCCESS",
            f"Failed login IPs: {len(self.suspicious_ips)}"
        )

    def is_private_ip(self, ip):

        return (
            ip.startswith("10.") or
            ip.startswith("192.168.") or
            ip.startswith("172.16.") or
            ip.startswith("127.")
        )

    def block_ip(self, ip):

        if self.is_private_ip(ip):
            return False

        success, _ = self.execute_command(
            f"sudo iptables -A INPUT -s {ip} -j DROP",
            f"Block IP {ip}"
        )

        if success:
            self.blocked_ips.append(ip)

        return success

    def close_port(self, port):

        success, output = self.execute_command(
            f"lsof -ti:{port}",
            f"Find Process on Port {port}"
        )

        if success and output.strip():
            pid = output.strip()
            self.execute_command(
                f"kill -9 {pid}",
                f"Kill Process on Port {port}"
            )

    def generate_network_report(self):

        report = {
            "incident_id": self.incident_id,
            "suspicious_ips": self.suspicious_ips,
            "blocked_ips": self.blocked_ips,
            "suspicious_ports": self.suspicious_ports
        }

        report_path = f"logs/reports/network_report_{self.incident_id}.json"

        with open(report_path, "w") as f:
            import json
            json.dump(report, f, indent=4)

        self.log_action(
            "Generate Network Report",
            "SUCCESS",
            report_path
        )

    def run(self):

        self.log_action("Playbook Start", "STARTED")

        self.analyze_connections()
        self.check_auth_logs()

        if self.suspicious_ips or self.suspicious_ports:
            self.send_alert("Network intrusion detected!", "high")

        for ip in self.suspicious_ips:
            self.block_ip(ip)

        for port in self.suspicious_ports:
            self.close_port(port)

        self.generate_network_report()
        self.generate_report()

        self.log_action("Playbook Complete", "SUCCESS")


if __name__ == "__main__":
    playbook = NetworkIntrusionPlaybook()
    playbook.run()
