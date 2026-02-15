# 🧪 Lab 12: SOC Playbooks Development

---

## 🎯 Objectives

✔ Design reusable SOC playbook framework  
✔ Implement malware detection & quarantine  
✔ Implement network intrusion response  
✔ Perform system isolation & evidence collection  
✔ Implement structured logging & alerting  
✔ Generate incident reports  

---

## 📌 Prerequisites

- Basic Python programming skills  
- Understanding of cybersecurity incident response concepts  
- Familiarity with Linux command line  
- Knowledge of network security fundamentals  
- Basic understanding of log analysis  

---

## 🔹 Lab Environment

- **OS:** Ubuntu 24.04.1 LTS (EC2 – Al Nafi Cloud)
- **User:** toor
- **Interface:** ens5
- **Python:** 3.12.x
- **Working Directory:** /home/toor/soc_playbooks

---

# 🛠 Task 1: Base Playbook Framework

## Step 1: Create Project Structure

```bash
mkdir -p ~/soc_playbooks/{scripts,logs,config,evidence}
cd ~/soc_playbooks
mkdir -p logs/{incidents,alerts,reports}
```

### Verify Structure

```bash
tree -L 2
```

Expected:

```
.
├── config
├── evidence
├── logs
│   ├── alerts
│   ├── incidents
│   └── reports
└── scripts
```

---

## Step 2: Create Base Playbook Class

File:

```
scripts/base_playbook.py
```

This class provides:

- Incident ID generation
- Structured logging
- Command execution wrapper
- Alert logging
- JSON report generation
- Action tracking

This becomes the reusable foundation for all SOC playbooks.

---

# 🛠 Task 2: Malware Detection Playbook

File:

```
scripts/malware_detection.py
```

### Capabilities:

- Suspicious process detection
- Detection of execution from `/tmp` or `/dev/shm`
- Reverse shell indicators
- Suspicious script detection
- World-writable file detection
- SHA256 hash calculation
- File quarantine
- Process termination
- Incident report generation

---

# 🛠 Task 3: Network Intrusion Response Playbook

File:

```
scripts/network_intrusion.py
```

### Capabilities:

- Active & listening port analysis (netstat)
- Detection of suspicious ports (1234, 4444, 31337)
- Failed SSH login detection from auth logs
- External IP reputation analysis
- Automatic IP blocking (iptables)
- Process termination on suspicious ports
- Network incident report generation

---

# 🛠 Task 4: System Isolation Playbook

File:

```
scripts/system_isolation.py
```

### Capabilities:

- System forensic data collection
- Process & network snapshot
- Login history collection
- Environment capture
- Memory & CPU info capture
- iptables backup
- Full network isolation
- Service shutdown
- Evidence archiving
- Structured incident reporting

---

# 🚀 Final Testing

Make all scripts executable:

```bash
chmod +x scripts/*.py
```

Run playbooks:

```bash
python3 scripts/malware_detection.py
python3 scripts/network_intrusion.py
python3 scripts/system_isolation.py
```

---

# 📂 Generated Artifacts

```
logs/
├── alerts/
├── incidents/
│   ├── quarantine_*
│   ├── evidence_*
│   └── *.log
└── reports/
    ├── malware_detection_*.json
    ├── network_report_*.json
    └── system_isolation_*.json
```

---

# ✅ Expected Outcomes

✔ Structured incident logs generated  
✔ Alerts written to logs/alerts  
✔ JSON reports stored in logs/reports  
✔ Quarantine directory created  
✔ Suspicious process terminated  
✔ Malicious IP blocked  
✔ Evidence archive generated  
✔ Network isolation simulated  

---

# 🔐 Key Security Takeaways

- Modular playbook architecture improves scalability
- Automation reduces SOC response time
- Quarantine prevents malware propagation
- Network isolation preserves forensic integrity
- Structured logging ensures audit compliance
- SOC automation simulates real-world orchestration pipelines

---

# 🏁 Conclusion

This lab demonstrated the implementation of reusable SOC playbooks capable of:

- Malware detection & containment
- Network intrusion response
- System isolation & evidence collection
- Structured logging & reporting

These playbooks simulate real-world SOC automation workflows used in modern security operations centers.
