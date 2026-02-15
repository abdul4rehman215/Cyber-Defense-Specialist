# 🧪 Lab 09: Email Header Analysis for Threats

---

## 🎯 Objectives

✔ Parse and analyze email headers  
✔ Detect spoofing and phishing indicators  
✔ Implement SPF validation  
✔ Implement DKIM validation  
✔ Implement DMARC policy checks  
✔ Build automated threat scoring system  
✔ Generate structured JSON threat reports  

## 📌 Prerequisites
- Basic Python programming skills
- Understanding of email protocols (SMTP, IMAP)
- Familiarity with DNS concepts
- Linux command line experience
- Basic cybersecurity knowledge

---

## 🖥 Lab Environment

- **OS:** Ubuntu 24.04.1 LTS (EC2 Cloud Environment)
- **User:** toor
- **Python Version:** 3.12.x
- **Libraries Used:** dnspython, email-validator
- **Network Interface:** ens5

---

## 📂 Lab Structure

This lab is organized into:

- `samples/` → Test email header samples
- `scripts/` → Python-based analysis modules
- `output/` → Generated JSON threat reports
- `commands.sh` → All executed commands
- `output.txt` → Full execution output logs
- `interview.md` → Technical interview Q&A
- `troubleshooting.md` → Issues and resolutions

---

## 🔍 What Was Implemented

### 1️⃣ Email Header Parsing
- Extracted critical fields (From, Reply-To, Return-Path, Received)
- Identified routing path and suspicious IPs

### 2️⃣ Spoofing Detection
- Compared From vs Reply-To domains
- Compared From vs Return-Path domains
- Detected impersonation indicators

### 3️⃣ SPF Validation
- Queried DNS TXT records
- Parsed SPF mechanisms
- Validated sender IP authorization

### 4️⃣ DKIM Verification
- Extracted DKIM signature
- Retrieved public key from DNS
- Verified domain selector logic

### 5️⃣ DMARC Policy Enforcement
- Retrieved DMARC record
- Evaluated policy action (none/quarantine/reject)
- Combined SPF + DKIM alignment logic

### 6️⃣ Integrated Threat Scoring Engine
- Combined:
  - Header indicators
  - SPF result
  - DKIM result
  - DMARC enforcement
- Generated risk levels:
  - MINIMAL
  - LOW
  - MEDIUM
  - HIGH

### 7️⃣ Structured JSON Reporting
Each analyzed email produced:
- Authentication results
- Threat score
- Threat level
- SOC recommendations

---

## 📊 Final Results Summary

| Email Sample | Threat Score | Threat Level |
|--------------|-------------|--------------|
| legitimate.eml | LOW | Low Risk |
| phishing.eml | HIGH | High Risk |
| malware.eml | HIGH | High Risk |

---

## 🔐 Security Insights

- Email authentication headers are critical forensic artifacts.
- SPF alone does not guarantee legitimacy.
- DKIM validates integrity but not sender identity.
- DMARC enforces alignment policy.
- Combining authentication + behavior scoring improves SOC prioritization.
- Automated analysis significantly reduces manual triage time.

---

## 🏁 Conclusion

This lab demonstrated practical email header forensics by:

- Parsing SMTP headers
- Detecting spoofing indicators
- Implementing SPF, DKIM, and DMARC logic
- Creating a weighted threat scoring engine
- Automating structured reporting

The implementation mirrors real-world SOC workflows for phishing detection and email threat triage.

---

🔐 **Key Security Principle:**  
Email authentication must be validated holistically — SPF, DKIM, and DMARC together — combined with contextual header analysis.

---
