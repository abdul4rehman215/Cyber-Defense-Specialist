#!/usr/bin/env python3

import os
from collections import defaultdict


class ZeekAnalyzer:

    def __init__(self, log_dir="/opt/zeek/logs/current"):
        self.log_dir = log_dir
        self.connections = []
        self.port_scanners = []
        self.large_transfers = []

    def load_conn_log(self):

        conn_file = os.path.join(self.log_dir, "conn.log")

        if not os.path.exists(conn_file):
            print("conn.log not found.")
            return

        with open(conn_file, "r") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                parts = line.strip().split("\t")
                if len(parts) > 10:
                    self.connections.append(parts)

    def detect_port_scan(self):

        ip_ports = defaultdict(set)

        for conn in self.connections:
            try:
                src_ip = conn[2]
                dst_port = conn[4]
                ip_ports[src_ip].add(dst_port)
            except IndexError:
                continue

        for ip, ports in ip_ports.items():
            if len(ports) > 20:
                self.port_scanners.append(ip)

    def analyze_traffic_volume(self):

        for conn in self.connections:
            try:
                orig_bytes = int(conn[8])
                resp_bytes = int(conn[9])

                if orig_bytes + resp_bytes > 10000000:
                    self.large_transfers.append({
                        "src": conn[2],
                        "dst": conn[4],
                        "total_bytes": orig_bytes + resp_bytes
                    })

            except:
                continue

    def generate_report(self):

        report_path = os.path.expanduser("~/soc-lab/reports/zeek_report.txt")

        with open(report_path, "w") as f:
            f.write("ZEEK NETWORK ANALYSIS REPORT\n")
            f.write("=================================\n\n")

            f.write(f"Port Scanners Detected: {self.port_scanners}\n")
            f.write(f"Large Transfers Detected: {len(self.large_transfers)}\n\n")

            if self.large_transfers:
                f.write("Large Transfer Details:\n")
                for transfer in self.large_transfers:
                    f.write(f"{transfer}\n")

        print("Zeek report generated.")


def main():

    analyzer = ZeekAnalyzer()
    analyzer.load_conn_log()
    analyzer.detect_port_scan()
    analyzer.analyze_traffic_volume()
    analyzer.generate_report()


if __name__ == "__main__":
    main()
