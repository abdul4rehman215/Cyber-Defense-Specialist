# 📘 Lab 7: MITRE ATT&CK Mapping for Incident Detection

<br>

### Q1. What is the MITRE ATT&CK framework?

**Answer:**
The MITRE ATT&CK framework is a globally recognized knowledge base that documents adversary tactics and techniques based on real-world observations. It provides a standardized structure for understanding attacker behavior across the attack lifecycle.

---

### Q2. Why was the MITRE ATT&CK JSON file downloaded in this lab?

**Answer:**
The JSON file contains structured data about techniques, tactics, and relationships within the framework. It was downloaded to allow programmatic parsing and automated mapping of security events to ATT&CK techniques.

---

### Q3. What types of logs were analyzed during this lab?

**Answer:**

* Windows Security Logs
* Linux Authentication Logs
* Network Traffic Logs

These logs were analyzed to detect attack patterns and map them to MITRE ATT&CK techniques.

---

### Q4. What does technique ID T1059.001 represent?

**Answer:**
T1059.001 represents **PowerShell execution**, a technique commonly used by attackers to execute malicious scripts or payloads on Windows systems.

---

### Q5. Why was mimikatz activity mapped to T1003.001?

**Answer:**
T1003.001 corresponds to **Credential Dumping from LSASS Memory**. Mimikatz is a well-known tool used to extract credentials from LSASS, making it a direct match to this technique.

---

### Q6. How were detection rules implemented in the log analyzer?

**Answer:**
Detection rules were implemented using **regular expressions (regex)** mapped to specific MITRE ATT&CK technique IDs. When log entries matched these patterns, findings were recorded and associated with the corresponding technique.

---

### Q7. What is the advantage of mapping incidents to MITRE ATT&CK techniques?

**Answer:**
It standardizes incident classification, improves communication across teams, enhances threat intelligence alignment, and supports consistent detection engineering practices.

---

### Q8. What was the role of the AutoMapper script?

**Answer:**
The AutoMapper script automatically mapped known indicators (e.g., powershell.exe, mimikatz.exe) to predefined MITRE ATT&CK techniques and generated a structured JSON incident report.

---

### Q9. Why is automated MITRE mapping valuable for SOC teams?

**Answer:**
Automation accelerates incident classification, reduces manual analysis effort, ensures consistency, and enables scalable detection engineering aligned with industry standards.

---

### Q10. What were the final deliverables of this lab?

**Answer:**

* Parsed MITRE ATT&CK dataset
* Automated log analyzer
* Technique-mapped analysis report (analysis_report.json)
* Incident classification report (incident_report.json)
* Structured MITRE-based detection workflow

---

## Bonus Technical Question

### Q11. How can MITRE ATT&CK mapping improve detection engineering?

**Answer:**
By identifying coverage gaps in detection capabilities, aligning alerts to specific tactics and techniques, and enabling structured threat modeling across environments.
