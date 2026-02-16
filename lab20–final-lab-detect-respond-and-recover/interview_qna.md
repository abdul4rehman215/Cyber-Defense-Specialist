# 📘 Interview Q&A - Lab 20 – Final Lab: Detect, Respond, and Recover

---

## 1️⃣ What was the main objective of Lab 20?

The main objective was to implement a complete Security Operations Center (SOC) workflow by integrating:

- Host-based monitoring (Wazuh)
- Network monitoring (Zeek)
- Automated Python-based detection scripts
- Attack simulation
- Incident response procedures
- Evidence collection and reporting

The lab demonstrated the full lifecycle:  
**Detect → Analyze → Respond → Recover → Document → Verify**

---

## 2️⃣ Why were both Wazuh and Zeek used together?

Wazuh provides **host-based detection**, including:

- Authentication failures
- File integrity monitoring
- Rootkit detection
- Log-based alerting

Zeek provides **network-based detection**, including:

- Port scanning behavior
- Abnormal traffic patterns
- Large data transfers
- Connection analysis

Using both tools together eliminates blind spots and improves overall visibility across host and network layers.

---

## 3️⃣ How was the SSH brute force attack detected?

The brute force simulation generated multiple failed login attempts.

Detection occurred via:

- Wazuh monitoring `/var/log/auth.log`
- High-severity authentication failure alerts
- Custom Python analyzer identifying ≥5 failed attempts from the same IP
- Suspicious IP flagged as `127.0.0.1`

---

## 4️⃣ How was port scanning detected?

Zeek analyzed `conn.log` and:

- Counted unique destination ports per source IP
- Flagged IPs connecting to more than 20 unique ports
- Identified `127.0.0.1` as a port scanner

The Zeek analyzer script automated this detection.

---

## 5️⃣ What automation components were implemented?

Three automation layers were built:

### 1️⃣ Wazuh Analyzer Script
- Parses alerts.json
- Counts alert severity
- Detects brute force patterns

### 2️⃣ Zeek Analyzer Script
- Parses conn.log
- Detects port scanning
- Identifies abnormal traffic volumes

### 3️⃣ Incident Response Script
- Blocks malicious IP via iptables
- Collects forensic evidence
- Generates incident report

---

## 6️⃣ What response actions were executed?

After confirming malicious behavior:

- Blocked suspicious IP using `iptables`
- Backed up firewall rules
- Collected evidence:
  - alerts.json
  - conn.log
  - netstat output
  - process list
  - login history
- Archived evidence securely
- Generated professional incident report

---

## 7️⃣ How was system integrity verified after response?

Post-response verification included:

- Wazuh Rootcheck (rootkit detection)
- Wazuh Syscheck (file integrity monitoring)
- Review of active connections
- Firewall rule validation
- Process inspection

No unauthorized modifications were detected.

---

## 8️⃣ What forensic evidence was collected?

Evidence included:

- `/var/ossec/logs/alerts/alerts.json`
- `/opt/zeek/logs/current/conn.log`
- `netstat` output
- `ps aux` process list
- Login history (`last -20`)
- Firewall configuration backup

All evidence was archived into a compressed file.

---

## 9️⃣ Why is documentation critical in incident response?

Documentation ensures:

- Legal defensibility
- Audit compliance
- Knowledge retention
- Post-incident review
- Improved future response
- Professional reporting standards

A structured incident report was created following SOC best practices.

---

## 🔟 What SOC lifecycle was demonstrated?

The complete SOC workflow was implemented:

**Detect → Analyze → Respond → Recover → Document → Verify**

This mirrors real-world Security Operations Center operations.

---

# ✅ Final Takeaway

In Lab 20, you demonstrated:

✔ Host-based monitoring (Wazuh)  
✔ Network traffic analysis (Zeek)  
✔ Automated threat detection with Python  
✔ Incident containment (iptables blocking)  
✔ Forensic evidence collection  
✔ Recovery validation  
✔ Professional documentation  

These are real-world **SOC Analyst** and **Incident Responder** skills.
