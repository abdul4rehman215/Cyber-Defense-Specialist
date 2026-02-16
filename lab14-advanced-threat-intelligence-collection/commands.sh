#!/bin/bash
# Lab 14 – Advanced Threat Intelligence Collection
# Commands Executed

# =========================
# Task 1: Environment Setup
# =========================

mkdir -p ~/threat_intel/{scripts,data,reports,config,logs}
cd ~/threat_intel
python3 --version

# =========================
# Create Configuration File
# =========================

nano config/sources.json

# =========================
# Create Sample Threat Data
# =========================

nano data/malware_domains.txt
nano data/suspicious_ips.txt

# =========================
# Task 2: Threat Collector
# =========================

nano scripts/threat_collector.py
chmod +x scripts/threat_collector.py
python3 scripts/threat_collector.py

# =========================
# Task 3: Data Normalizer
# =========================

nano scripts/data_normalizer.py
chmod +x scripts/data_normalizer.py
python3 scripts/data_normalizer.py

ls -lh data/

# =========================
# Task 4: Report Generator
# =========================

nano scripts/report_generator.py
chmod +x scripts/report_generator.py
python3 scripts/report_generator.py

ls -lh reports/
cat reports/threat_report_20260216_144421.txt

# =========================
# Automated Pipeline
# =========================

nano scripts/run_pipeline.sh
chmod +x scripts/run_pipeline.sh
./scripts/run_pipeline.sh

ls -lh data/
ls -lh reports/

# =========================
# Validation & Troubleshooting Checks
# =========================

python3 -m json.tool data/normalized_20260216_150212.json > /dev/null
tail -n 5 logs/collection.log
