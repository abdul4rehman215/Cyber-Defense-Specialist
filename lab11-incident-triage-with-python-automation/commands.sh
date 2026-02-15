#!/bin/bash

# Create project directory structure
mkdir -p ~/incident_triage_lab/{data,scripts,reports,rules}

# Navigate to project directory
cd ~/incident_triage_lab

# Verify current working directory
pwd

# Create sample alerts JSON file
nano data/sample_alerts.json

# Validate alerts JSON
python3 -m json.tool data/sample_alerts.json

# Create triage rules configuration
nano rules/triage_rules.json

# Validate rules JSON
python3 -m json.tool rules/triage_rules.json

# Create main triage engine script
nano scripts/incident_triage.py

# Create alert enrichment module
nano scripts/alert_enrichment.py

# Create automated response script
nano scripts/automated_response.py

# Create complete workflow script
nano scripts/complete_workflow.py

# Make all scripts executable
chmod +x scripts/*.py

# Run core triage engine
python3 scripts/incident_triage.py

# Test enrichment module separately
python3 scripts/alert_enrichment.py

# Run automated response module
python3 scripts/automated_response.py

# Run full SOC workflow
python3 scripts/complete_workflow.py

# Verify generated reports
ls -lh reports/
