# 🧪 Lab 20 – Final Lab: Detect, Respond, and Recover

---

## 📌 Lab Summary

This final lab integrates host-based monitoring (Wazuh), network monitoring (Zeek), automated log analysis using Python, attack simulation, incident response procedures, evidence collection, recovery validation, and professional documentation.

It demonstrates a complete SOC (Security Operations Center) workflow:

Detect → Analyze → Respond → Recover → Document → Verify

This lab simulates real-world security operations in an enterprise environment.

---

## 🎯 Objectives

By completing this lab, you achieved the ability to:

- Deploy and configure Wazuh Manager
- Install and configure Zeek Network Security Monitor
- Develop automated Python log analysis tools
- Simulate real-world attack scenarios
- Detect SSH brute force attacks
- Detect port scanning behavior
- Perform firewall containment actions
- Collect forensic evidence
- Execute recovery validation procedures
- Produce professional incident response documentation

---

## 📌 Prerequisites

- Basic Linux command-line knowledge
- TCP/IP networking fundamentals
- Understanding of SSH, ports, and protocols
- Basic Python scripting knowledge
- Familiarity with cybersecurity attack patterns

---

## 🖥 Lab Environment

- Ubuntu 24.04 LTS
- 8GB RAM
- User: `toor`
- Host: `ip-172-31-18-144`

Installed Components:
- Wazuh Manager 4.7.x
- Zeek 6.0.0
- Python 3
- pandas
- requests
- iptables
- tcpdump

---

## 📁 Repository Structure

```
lab20-detect-respond-recover/
│
├── soc-lab/
│   ├── logs/
│   ├── reports/
│   ├── evidence/
│   ├── scripts/
│   │   ├── wazuh_analyzer.py
│   │   ├── zeek_analyzer.py
│   │   ├── incident_response.py
│   │
│   ├── attack-simulation/
│   │   ├── ssh_bruteforce.sh
│   │   └── port_scan.sh
│
├── commands.sh
├── output.txt
├── interview_qna.md
└── troubleshooting.md
```

---

## 🔎 What This Lab Demonstrates

### 1️⃣ Host-Based Monitoring (Wazuh)
- Authentication failure detection
- High-severity alert monitoring
- Rootcheck and syscheck validation
- Log analysis automation

### 2️⃣ Network-Based Monitoring (Zeek)
- Port scan detection
- Traffic analysis via conn.log
- Network behavior correlation

### 3️⃣ Attack Simulation
- SSH brute force attack
- Port scan attack

### 4️⃣ Automated Analysis
- Severity classification
- Brute force IP detection
- Port scanner identification
- Traffic volume analysis

### 5️⃣ Incident Response
- IP containment via iptables
- Firewall verification
- Evidence collection
- Log backup
- System integrity validation

### 6️⃣ Recovery & Validation
- Rootkit scan
- File integrity check
- Active connection review
- Firewall verification

---

## ▶ Execution Flow

1. Install dependencies
2. Install Wazuh Manager
3. Install Zeek
4. Create SOC structure
5. Deploy Python analyzers
6. Simulate attacks
7. Run analyzers
8. Contain malicious IP
9. Collect forensic evidence
10. Archive evidence
11. Verify system integrity
12. Create final incident report
13. Validate security posture

---

## 📊 Detection Results

Detected:

- SSH brute force attempts
- High-severity authentication alerts
- Port scan (>20 ports)
- Suspicious IP activity

---

## 🛡 Response Actions Performed

- Blocked malicious IP using iptables
- Backed up firewall configuration
- Collected:
  - Wazuh alerts
  - Zeek connection logs
  - Process list
  - Netstat output
  - Login history
- Archived forensic evidence
- Verified system integrity

---

## 📄 Final Outcome

This lab successfully demonstrated a complete SOC lifecycle:

✔ Monitoring Infrastructure Deployment  
✔ Automated Threat Detection  
✔ Attack Simulation  
✔ Containment & Mitigation  
✔ Evidence Collection  
✔ Recovery Validation  
✔ Professional Reporting  

---

## 🎯 Real-World Relevance

This lab mirrors real SOC operations including:

- Incident triage
- Log correlation
- Automated analysis
- Forensic evidence handling
- Incident documentation
- Post-incident verification

It reflects enterprise-grade detection engineering and incident response practices.

---

## 🧠 Key Takeaways

- Host + Network monitoring provides full visibility
- Automation reduces detection time
- Incident documentation is critical
- Containment must be verified
- Evidence preservation is mandatory
- Recovery validation ensures full mitigation

---

Lab 20 represents a complete operational SOC workflow.
