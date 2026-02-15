# 📘 Interview Q&A – Lab 10 Identifying Malicious Attachments & URLs

---

### Q1. What was the main objective of this lab?

**Answer:**  
The main objective was to detect malicious characteristics in email attachments and URLs by performing static file analysis, URL structure inspection, risk scoring, and generating structured JSON security reports. The lab also implemented an integrated email security scanner to simulate real-world SOC workflows.

---

### Q2. Why are MD5 and SHA256 hashes calculated for attachments?

**Answer:**  
Hashes uniquely identify files and are essential for:

- Malware reputation checks  
- File integrity verification  
- Threat intelligence correlation  
- Incident response investigations  

MD5 provides fast identification, while SHA256 offers stronger cryptographic assurance.

---

### Q3. Why is a double extension like `invoice.pdf.exe` considered dangerous?

**Answer:**  
Attackers use double extensions to disguise executable malware as legitimate documents. Users may only see `invoice.pdf`, increasing the likelihood of execution. Double extensions are strong indicators of malicious intent.

---

### Q4. How does the attachment scanner determine file risk?

**Answer:**  
The scanner evaluates:

- Suspicious file extensions (.exe, .bat, .js, etc.)  
- MIME type detection using `python-magic`  
- Double extension presence  
- File size anomalies  
- Executable file descriptions  

Each factor contributes to a cumulative risk score that determines threat level.

---

### Q5. What URL characteristics increase phishing risk?

**Answer:**  
Risk increases when URLs contain:

- Direct IP addresses instead of domain names  
- URL shorteners (bit.ly, tinyurl)  
- Excessive subdomains  
- Suspicious keywords (login, verify, urgent, account)  
- Encoded characters or abnormal length  

These patterns are common in phishing campaigns.

---

### Q6. Why is using an IP address in a URL suspicious?

**Answer:**  
Legitimate organizations typically use branded domain names. Attackers often use IP addresses to:

- Avoid domain reputation checks  
- Bypass simple filtering mechanisms  
- Quickly rotate hosting infrastructure  

IP-based URLs are frequently linked to phishing or malware hosting.

---

### Q7. How does the URL analyzer detect phishing content?

**Answer:**  
It fetches webpage content and scans for phishing-related keywords such as:

- login  
- verify  
- account  
- urgent  
- suspended  

It also evaluates redirect chains and excessive form fields to detect credential harvesting pages.

---

### Q8. How is the threat level classified?

**Answer:**  
Threat level is determined by cumulative risk score:

- **HIGH** → Score ≥ 50  
- **MEDIUM** → Score ≥ 25  
- **LOW** → Score ≥ 10  
- **CLEAN** → Score < 10  

This scoring helps prioritize security incidents.

---

### Q9. What is the purpose of the integrated_scanner.py?

**Answer:**  
The integrated scanner combines:

- URL analysis  
- Attachment scanning  
- Risk aggregation  
- Overall email threat classification  

It simulates a real-world email security gateway performing multi-layered inspection.

---

### Q10. Why is integrated email analysis more effective than scanning individually?

**Answer:**  
Analyzing attachments or URLs separately may miss threats. Combining both provides:

- Better detection accuracy  
- Reduced false negatives  
- Holistic threat assessment  
- Improved SOC prioritization  

Integrated analysis mirrors enterprise-grade email security solutions.
