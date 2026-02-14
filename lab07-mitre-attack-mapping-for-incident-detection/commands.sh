#!/bin/bash

# ==============================
# Lab 7: MITRE ATT&CK Mapping
# ==============================

# Create lab directory structure
mkdir -p ~/mitre-lab/{data,scripts,logs,reports}
cd ~/mitre-lab

# Verify structure
tree

# Download MITRE ATT&CK Enterprise dataset
wget https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json -O data/enterprise-attack.json

# Install required Python libraries
pip3 install requests pandas stix2 pyyaml

# ------------------------------
# Create Sample Log Files
# ------------------------------

# Windows security log
nano logs/windows_security.log

# Linux authentication log
nano logs/linux_auth.log

# Network log
nano logs/network.log

# ------------------------------
# Create MITRE Parser
# ------------------------------

cd scripts
nano mitre_parser.py
chmod +x mitre_parser.py
python3 mitre_parser.py

# ------------------------------
# Create Log Analyzer
# ------------------------------

nano log_analyzer.py
chmod +x log_analyzer.py
python3 log_analyzer.py

# Verify generated report
cd ..
ls reports

# ------------------------------
# View Analysis Results
# ------------------------------

cd scripts
nano view_results.py
chmod +x view_results.py
python3 view_results.py

# ------------------------------
# Automated Incident Mapping
# ------------------------------

nano auto_mapper.py
chmod +x auto_mapper.py
python3 auto_mapper.py

# Verify incident report
cd ..
ls reports

# View generated JSON reports
cat reports/analysis_report.json
cat reports/incident_report.json

# ------------------------------
# Validate MITRE JSON structure (Troubleshooting)
# ------------------------------

python3 -m json.tool data/enterprise-attack.json | head

# End of Lab 7
