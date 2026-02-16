#!/bin/bash

# ==========================================
# Lab 17 – Incident Response Automation
# Commands Executed During Lab
# ==========================================


# --------------------------------------------------
# Environment Verification
# --------------------------------------------------

python3 --version


# --------------------------------------------------
# Task 1 – Setup Incident Response Framework
# --------------------------------------------------

mkdir -p ~/incident_response/{scripts,logs,reports,config,alerts}
cd ~/incident_response

mkdir -p logs/{system,security,application}
mkdir -p scripts/{collection,analysis,response}
mkdir -p reports/incidents

tree -L 2


# --------------------------------------------------
# Create Sample Log Files
# --------------------------------------------------

nano logs/system/syslog.log
nano logs/security/auth.log
nano logs/application/webapp.log

wc -l logs/system/syslog.log
wc -l logs/security/auth.log
wc -l logs/application/webapp.log


# --------------------------------------------------
# Create Response Configuration
# --------------------------------------------------

nano config/response_config.json


# --------------------------------------------------
# Task 2 – Log Collector
# --------------------------------------------------

nano scripts/collection/log_collector.py
chmod +x scripts/collection/log_collector.py

python3 scripts/collection/log_collector.py

cat reports/incidents/collection_report_*.json


# --------------------------------------------------
# Task 3 – Log Analyzer
# --------------------------------------------------

nano scripts/analysis/log_analyzer.py
chmod +x scripts/analysis/log_analyzer.py

python3 scripts/analysis/log_analyzer.py

ls -lh reports/incidents/


# --------------------------------------------------
# Task 4 – Incident Responder
# --------------------------------------------------

nano scripts/response/incident_responder.py
chmod +x scripts/response/incident_responder.py

python3 scripts/response/incident_responder.py

ls -lh alerts/
cat alerts/response_actions.log


# --------------------------------------------------
# Integrated Automation Script
# --------------------------------------------------

nano scripts/automated_response.py
chmod +x scripts/automated_response.py

python3 scripts/automated_response.py


# --------------------------------------------------
# Verification Commands
# --------------------------------------------------

ls -lh reports/incidents/
ls -lh alerts/
tail -n 10 alerts/response_actions.log
