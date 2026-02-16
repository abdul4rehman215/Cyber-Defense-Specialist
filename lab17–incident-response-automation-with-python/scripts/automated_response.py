#!/usr/bin/env python3

import sys
import json
from pathlib import Path

BASE_DIR = Path.home() / "incident_response"
sys.path.insert(0, str(BASE_DIR / "scripts"))

from collection.log_collector import LogCollector
from analysis.log_analyzer import LogAnalyzer
from response.incident_responder import IncidentResponder


def main():

    print("=" * 60)
    print("AUTOMATED INCIDENT RESPONSE SYSTEM")
    print("=" * 60)

    # --------------------------------------------------
    # STEP 1 – Log Collection
    # --------------------------------------------------
    print("\n[STEP 1] Collecting logs...")
    collector = LogCollector()
    collector.run_collection()

    # --------------------------------------------------
    # STEP 2 – Log Analysis
    # --------------------------------------------------
    print("\n[STEP 2] Analyzing logs...")
    analyzer = LogAnalyzer()
    analyzer.run_analysis()

    # --------------------------------------------------
    # STEP 3 – Incident Response
    # --------------------------------------------------
    print("\n[STEP 3] Responding to incidents...")
    responder = IncidentResponder()

    reports_dir = BASE_DIR / "reports" / "incidents"
    report_files = sorted(reports_dir.glob("analysis_report_*.json"))

    if not report_files:
        print("No incidents detected.")
        return

    latest_report = report_files[-1]

    with open(latest_report, "r") as f:
        report_data = json.load(f)

    incidents = report_data.get("incidents", [])
    responder.respond_to_multiple_incidents(incidents)

    print("\n[INFO] Incident response automation completed")


if __name__ == "__main__":
    main()
