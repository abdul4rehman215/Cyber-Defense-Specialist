# 🧪 Lab 10: Identifying Malicious Attachments & URLs

## 🔹 Lab Overview

This lab focuses on identifying malicious email attachments and detecting phishing URLs using static analysis, structural inspection, and risk scoring methodologies.

The lab demonstrates how combining attachment scanning and URL inspection improves overall email threat detection accuracy.

---

## 🎯 Objectives

- Analyze email attachments for malicious characteristics  
- Detect phishing and suspicious URLs  
- Calculate MD5 and SHA256 file hashes  
- Identify double extensions and executable files  
- Apply structured risk scoring methodology  
- Generate JSON-based security reports  
- Implement integrated email security scanner  

---

## 📌 Prerequisites
- Basic Python programming knowledge
- Familiarity with Linux command line
- Understanding of file systems and file types
- Basic cybersecurity concepts (malware, phishing)

---

## 🖥 Lab Environment

| Component | Details |
|------------|----------|
| OS | Ubuntu 24.04.1 LTS (Cloud Environment) |
| User | toor |
| Interface | ens5 |
| Python | 3.12.x |
| Working Directory | /home/toor/malware_lab |

---

## 📂 Directory Structure

```
malware_lab/
│
├── attachment_scanner.py
├── url_analyzer.py
├── integrated_scanner.py
│
├── samples/
├── attachments/
├── urls/
├── reports/
│
├── test_urls.txt
└── sample_email.txt
```

---

## 🔎 Lab Modules

### 1️⃣ Attachment Scanner
- Detects suspicious extensions (.exe, .bat, .js, etc.)
- Identifies double extensions
- Uses python-magic for MIME detection
- Calculates file hashes
- Applies risk scoring logic
- Generates JSON report

---

### 2️⃣ URL Analyzer
- Detects:
  - IP-based URLs
  - URL shorteners
  - Suspicious keywords
  - Excessive subdomains
  - Long URLs
- Performs lightweight content inspection
- Generates structured JSON report

---

### 3️⃣ Integrated Email Security Scanner
- Extracts URLs from email content
- Scans attachments
- Calculates overall email risk score
- Generates integrated JSON security report

---

## 📊 Risk Classification Model

| Score Range | Threat Level |
|-------------|-------------|
| 0–9 | CLEAN |
| 10–24 | LOW |
| 25–49 | MEDIUM |
| 50+ | HIGH |

---

## 📁 Reports Generated

All reports are stored inside:

```
reports/
```

- attachment_report_*.json
- url_report_*.json
- integrated_report_*.json

---

## 🔐 Key Security Insight

- Double extensions are strong malware indicators.
- IP-based URLs increase phishing likelihood.
- URL shorteners can hide malicious destinations.
- Hashing enables malware reputation lookup.
- Integrated scanning improves detection accuracy.
- Risk scoring enhances SOC prioritization.

---

## ✅ Expected Outcomes

✔ Attachment scanner detecting suspicious extensions  
✔ Hash calculation (MD5 & SHA256)  
✔ Double extension detection  
✔ URL structural risk detection  
✔ Keyword-based phishing detection  
✔ Automated JSON reporting  
✔ Integrated email security scanner  

---

## 🏁 Conclusion

This lab provided hands-on implementation of:

- File integrity validation
- MIME-based detection
- URL structural analysis
- Content-based phishing detection
- Combined email security scanning

Combining attachment and URL analysis significantly improves detection coverage in real-world SOC environments.

---

