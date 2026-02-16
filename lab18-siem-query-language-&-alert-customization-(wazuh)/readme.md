# 🧪 Lab 18 – SIEM Query Language & Alert Customization (Wazuh)

---

## 📌 Lab Summary

This lab focuses on mastering Wazuh (Elasticsearch DSL-based) query language and implementing full SIEM customization.  

You designed, validated, optimized, and automated detection logic using:

- Custom Elasticsearch queries
- Custom Wazuh XML rules
- Alert monitoring scripts
- Automated response handlers
- Performance benchmarking tools
- Validation & testing framework

This lab models real-world SOC-level SIEM engineering tasks.

---

## 🎯 Objectives

- Understand Wazuh Query Language structure
- Write custom SIEM queries for authentication, syscheck, and firewall events
- Validate and test query execution
- Create and load custom Wazuh rules
- Automate alert processing and response
- Optimize Elasticsearch queries
- Benchmark query performance
- Validate complete SIEM customization workflow

---

## 📌 Prerequisites

- Basic Linux command-line knowledge
- Understanding of log analysis concepts
- Familiarity with JSON structure
- Knowledge of authentication & network security threats
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
3. Validate query syntax and execution  
4. Create and load custom Wazuh rules  
5. Restart Wazuh Manager  
6. Generate simulated attack events  
7. Monitor and process custom alerts  
8. Benchmark and optimize query performance  
9. Validate full lab setup  

---

## ✅ Expected Outcomes

- Custom queries execute successfully  
- Custom rules load without syntax errors  
- Custom alerts are triggered correctly  
- Automated response scripts execute actions  
- Query optimization improves performance (~43%)  
- Validation suite confirms full configuration  

---

# 🏁 Final Conclusion

You have successfully:

✔ Mastered Wazuh Query Language  
✔ Created custom authentication rules  
✔ Created syscheck rules  
✔ Created firewall/network rules  
✔ Implemented alert automation  
✔ Built custom response handlers  
✔ Simulated attack scenarios  
✔ Validated rule loading  
✔ Optimized query performance  
✔ Compared execution benchmarks  
✔ Created a lab validation suite  

This lab demonstrates complete SIEM customization from detection logic to automated response.

---

# 📚 What I Learned

- How Elasticsearch DSL queries work in Wazuh
- How to build detection logic using filters, ranges, and aggregations
- How to reduce false positives using precise rule conditions
- How to create and load custom Wazuh XML rules
- How to automate alert monitoring and response scripting
- How to benchmark and optimize query performance
- How to validate a full SIEM workflow in a controlled environment

---

# 🚨 Why This Matters

SIEM customization is critical in real cybersecurity environments.

Default SIEM rules often:

- Miss organization-specific threats
- Generate excessive false positives
- Cannot automate response actions
- Lack performance optimization

By mastering custom query creation and alert automation, you can:

- Detect threats specific to your environment  
- Reduce false positive alerts  
- Automate incident response workflows  
- Improve detection speed  
- Optimize monitoring performance  

---

# 🌍 Real-World Applications

The skills developed in this lab apply directly to:

- SOC (Security Operations Center) Analyst roles  
- SIEM Administrator positions  
- Incident Response teams  
- Threat Hunting operations  
- Compliance monitoring and reporting  

---

# 🚀 Real-World Impact

This lab demonstrates practical SOC-level SIEM engineering:

- Fine-tuned detection queries  
- Custom threat detection logic  
- Reduced alert fatigue  
- Automated response workflows  
- Performance tuning  
- Validation & testing framework  

These are real-world SIEM engineering and SOC automation skills used in enterprise security environments.

---

## 🏆 Result

Advanced Wazuh SIEM customization successfully implemented and validated.

Enterprise-grade detection and automation techniques demonstrated.
