#!/usr/bin/env python3

from incident_triage import IncidentTriageEngine
from automated_response import AutomatedResponder
import os


def run_complete_workflow():

    print("=== Complete Incident Triage Workflow ===\n")

    engine = IncidentTriageEngine("rules/triage_rules.json")
    alerts = engine.load_alerts("data/sample_alerts.json")

    engine.process_alerts(alerts)

    print(engine.generate_summary_report())

    engine.save_results("reports")

    responder = AutomatedResponder()
    responder.process_high_priority_alerts(engine.high_priority_alerts)
    responder.save_response_log("reports/response_log.json")

    print("\nWorkflow completed successfully.")


if __name__ == "__main__":
    run_complete_workflow()
