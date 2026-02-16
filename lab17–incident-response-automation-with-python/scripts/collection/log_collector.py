#!/usr/bin/env python3

import os
import shutil
import datetime
import json
from pathlib import Path


class LogCollector:

    def __init__(self):
        self.base_dir = Path.home() / "incident_response"
        self.logs_dir = self.base_dir / "logs"
        self.reports_dir = self.base_dir / "reports" / "incidents"
        self.timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    def collect_system_logs(self):

        collected = {}
        source_file = self.logs_dir / "system" / "syslog.log"

        if source_file.exists():
            dest = self.logs_dir / "system" / f"syslog_{self.timestamp}.log"
            shutil.copy(source_file, dest)
            collected["system"] = str(dest)

        return collected

    def collect_security_logs(self):

        collected = {}
        source_file = self.logs_dir / "security" / "auth.log"

        if source_file.exists():
            dest = self.logs_dir / "security" / f"auth_{self.timestamp}.log"
            shutil.copy(source_file, dest)
            collected["security"] = str(dest)

        return collected

    def collect_application_logs(self):

        collected = {}
        app_dir = self.logs_dir / "application"

        for file in app_dir.glob("*.log"):
            dest = app_dir / f"{file.stem}_{self.timestamp}.log"
            shutil.copy(file, dest)
            collected[file.name] = str(dest)

        return collected

    def generate_collection_report(self, collected_data):

        report = {
            "timestamp": self.timestamp,
            "collected_files": collected_data
        }

        report_file = self.reports_dir / f"collection_report_{self.timestamp}.json"

        with open(report_file, "w") as f:
            json.dump(report, f, indent=4)

        return str(report_file)

    def run_collection(self):

        print("[INFO] Starting log collection")

        collected = {}
        collected.update(self.collect_system_logs())
        collected.update(self.collect_security_logs())
        collected.update(self.collect_application_logs())

        report_path = self.generate_collection_report(collected)

        print(f"[INFO] Collected {len(collected)} log sources")
        print(f"[INFO] Report saved to {report_path}")


if __name__ == "__main__":
    collector = LogCollector()
    collector.run_collection()
