# 🧪 Lab 18 – SIEM Query Language & Alert Customization (Wazuh)

---

## 📌 Lab Summary

This lab focuses on writing and validating custom Wazuh (Elasticsearch DSL) queries, creating custom detection rules, automating alert handling, optimizing query performance, and validating the entire SIEM workflow.

The lab demonstrates:

- Custom query creation
- Advanced threat detection logic
- Custom Wazuh rule development
- Alert monitoring & automation
- Performance benchmarking
- Validation and testing framework

---

## 🎯 Objectives

- Understand Wazuh Query Language structure
- Write custom SIEM queries for authentication, syscheck, and firewall events
- Validate and test query execution
- Create and load custom Wazuh rules
- Automate alert processing and response
- Optimize Elasticsearch queries
- Benchmark query performance
- Validate complete SIEM customization

---

## 📌 Prerequisites

- Basic Linux command-line knowledge
- Understanding of log analysis concepts
- Familiarity with JSON structure
- Knowledge of basic security threats
- Wazuh installed and accessible

---

## 🖥 Environment

- Ubuntu 20.04 LTS
- Wazuh Manager
- Wazuh Indexer (Elasticsearch)
- Wazuh Dashboard
- jq
- bc
- User: toor
- Host: ip-172-31-10-214

---

## 📁 Project Structure (Repository Format)

```
lab18-siem-customization/
│
├── queries/
│   ├── failed_login_query.json
│   ├── brute_force_query.json
│   ├── optimized_brute_force_query.json
│   ├── file_access_query.json
│   └── network_anomaly_query.json
│
├── scripts/
│   ├── test_query.sh
│   ├── validate_query.sh
│   ├── generate_test_events.sh
│   ├── monitor_alerts.sh
│   ├── alert_response.sh
│   ├── process_alerts.sh
│   ├── query_performance.sh
│   ├── validate_lab_setup.sh
│   └── final_test_scenario.sh
│
├── rules/
│   ├── 100-custom_auth_rules.xml
│   ├── 101-custom_syscheck_rules.xml
│   └── 102-custom_network_rules.xml
│
├── commands.sh
├── output.txt
├── interview_qna.md
└── troubleshooting.md
```

---

## ▶ Execution Flow

1. Start Wazuh services
2. Create & test custom queries
3. Validate queries
4. Create custom rules
5. Restart Wazuh Manager
6. Generate test events
7. Monitor & process alerts
8. Benchmark performance
9. Run validation scripts

---

## ✅ Expected Outcomes

- Custom queries execute successfully
- Custom rules load without errors
- Custom alerts triggered
- Automated response executed
- Performance improvement measured (~43%)
- Full lab validation successful

---

## 🏁 Result

This lab successfully demonstrated:

- Advanced Wazuh query writing
- SIEM rule customization
- Alert automation scripting
- Performance optimization techniques
- Complete validation workflow

Real SOC-level SIEM engineering skills implemented.
