# 🧪 Lab 14 – Advanced Threat Intelligence Collection

---

## 📌 Lab Environment

- **Operating System:** Ubuntu 24.04.1 LTS (Cloud VM)
- **User:** toor
- **Python Version:** 3.12.x
- **Project Directory:** ~/threat_intel

---

## 🎯 Objectives

By completing this lab, the following capabilities were implemented:

- Collect threat intelligence indicators from local data sources
- Validate IP addresses, domains, and file hashes
- Enrich indicators with metadata
- Calculate risk scores based on indicator type
- Normalize threat intelligence datasets
- Deduplicate indicators
- Assign severity levels
- Generate automated threat intelligence reports
- Build a complete end-to-end threat intelligence pipeline

---

## 📚 Prerequisites

- Basic Python programming (functions, loops, dictionaries)
- Understanding of cybersecurity threat indicators
- Familiarity with JSON format
- Basic Linux CLI usage

---

## 📂 Project Structure

```
threat_intel/
├── config/
│ └── sources.json
├── data/
│ ├── malware_domains.txt
│ ├── suspicious_ips.txt
│ ├── collected_.json
│ └── normalized_.json
├── logs/
│ └── collection.log
├── reports/
│ ├── threat_report_.txt
│ ├── threat_report_.html
│ └── threat_report_*.json
└── scripts/
├── threat_collector.py
├── data_normalizer.py
├── report_generator.py
└── run_pipeline.sh
```


---

## 🧩 Lab Tasks Overview

### Task 1 – Environment Setup
- Created project directory structure
- Verified Python installation
- Configured data source settings
- Created sample threat feeds

### Task 2 – Threat Collection
- Implemented indicator validation
- Enriched indicators with metadata
- Applied risk scoring logic
- Stored collected indicators in JSON format
- Implemented structured logging

### Task 3 – Data Normalization
- Standardized confidence values
- Assigned severity levels
- Normalized tags
- Removed duplicates
- Generated normalization statistics

### Task 4 – Reporting
- Generated reports in:
  - Text format (.txt)
  - HTML format (.html)
  - JSON format (.json)
- Ranked threats by risk score
- Produced executive summary and breakdown analysis

### Task 5 – Automated Pipeline
- Created bash script to automate:
  1. Collection
  2. Normalization
  3. Report generation

---

## ✅ Outcomes

- 7 total threat indicators collected
- IP and domain validation functioning
- Risk scoring applied automatically
- Severity classification working
- Multi-format reports generated
- Logs stored in logs/collection.log
- Automated pipeline executed successfully

---

## 🎯 Key Deliverables

- scripts/threat_collector.py
- scripts/data_normalizer.py
- scripts/report_generator.py
- scripts/run_pipeline.sh
- data/collected_*.json
- data/normalized_*.json
- reports/threat_report_*.txt
- reports/threat_report_*.html
- reports/threat_report_*.json
- logs/collection.log

---

## 🏁 Conclusion

This lab implemented a complete automated Threat Intelligence Processing Pipeline including collection, validation, enrichment, normalization, reporting, and workflow automation.

The project simulates a foundational SOC-level threat intelligence system and provides a structured base for integrating real-world threat feeds and enterprise-scale intelligence platforms.
