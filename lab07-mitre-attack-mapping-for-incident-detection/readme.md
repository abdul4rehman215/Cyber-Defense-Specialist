# 🧪 Lab 7: MITRE ATT&CK Mapping for Incident Detection

## 🔹 Lab Environment
- OS: Ubuntu Server 24.04 LTS  
- User: student  
- Shell: bash  
- Python: 3.x  
- Working Directory: /home/student/mitre-lab  

---

## 🎯 Objectives

This lab focused on applying the MITRE ATT&CK framework for structured incident detection and classification.

By completing this lab, I was able to:

- Understand the structure of the MITRE ATT&CK framework (Techniques & Tactics)
- Parse enterprise ATT&CK JSON data programmatically
- Analyze Windows, Linux, and network logs
- Map security events to ATT&CK techniques
- Automate detection rule creation
- Generate structured JSON-based incident reports

---

## 🧩 Tasks Performed

### 1️⃣ Environment Setup
- Created structured lab directory (data, logs, scripts, reports)
- Downloaded MITRE enterprise-attack.json dataset
- Installed required Python libraries (requests, pandas, stix2, pyyaml)

### 2️⃣ MITRE Parser Development
- Built a custom Python parser to extract:
  - Techniques (TIDs)
  - Tactics
  - Descriptions
  - Platforms
- Verified technique & tactic counts

### 3️⃣ Log Analysis & Detection Rules
- Created detection rules mapped to:
  - T1059.001 (PowerShell)
  - T1003.001 (Credential Dumping – LSASS)
  - T1543.003 (Create/Modify System Process)
  - T1071.001 (Web Protocol C2)
  - T1046 (Network Service Scanning)
- Parsed Windows, Linux, and network logs
- Generated structured findings report

### 4️⃣ Automated Incident Mapping
- Built auto-mapper module
- Mapped known indicators to ATT&CK techniques
- Generated machine-readable incident reports (JSON)

---

## 📊 Key Results

- Successfully loaded MITRE ATT&CK dataset
- Detected 7 mapped findings across logs
- Generated:
  - analysis_report.json
  - incident_report.json
- Applied industry-standard ATT&CK technique classification

---

## 🔐 Skills Demonstrated

- Threat Detection Engineering
- Log Pattern Recognition
- MITRE ATT&CK Mapping
- Regex-based detection rules
- Structured JSON reporting
- Incident Classification Automation

---

## 🧾 Conclusion

This lab strengthened practical understanding of the MITRE ATT&CK framework by integrating it directly into detection workflows.

Instead of manually reviewing logs, I implemented automated rule-based detection and mapped findings to standardized technique IDs.

This approach aligns with real-world SOC operations, threat intelligence workflows, and detection engineering practices.

MITRE ATT&CK mapping improves:
- Communication between analysts
- Detection rule standardization
- Incident reporting quality
- Threat hunting accuracy

---

## 🚀 Future Enhancements

- Integrate with SIEM tools
- Add tactic-level classification
- Expand detection rule coverage
- Build ATT&CK heatmap visualization
- Correlate multi-host incidents

---

Lab 7 successfully demonstrates automated MITRE ATT&CK-based incident detection and classification.
