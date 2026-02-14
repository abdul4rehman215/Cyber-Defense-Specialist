# 🌐 Lab 04: HTTP/HTTPS Traffic Deconstruction

## 🧭 Overview
This lab demonstrates how to capture, deconstruct, and analyze HTTP and HTTPS traffic using command-line tools. It simulates common web-based attacks and implements automated detection mechanisms to mimic real SOC monitoring workflows.

---

## 🎯 Objectives
- Capture and analyze HTTP/HTTPS traffic using command-line tools
- Parse HTTP headers and identify request/response components
- Detect suspicious patterns and anomalies in web traffic
- Analyze HTTPS metadata and connection characteristics
- Create automated scripts for traffic analysis
- Apply traffic analysis techniques for security monitoring

---

## 🖥️ Lab Environment
- Ubuntu Server 24.04 LTS
- Local Python HTTP server (Port 8080)
- tcpdump for packet capture
- OpenSSL for TLS inspection
- Custom Python and Bash scripts for automation

---

## 🧪 Tasks Performed

### 1️⃣ HTTP Traffic Capture
- Created a local Python HTTP server
- Captured traffic using tcpdump
- Generated normal and malicious HTTP requests
- Extracted raw HTTP payloads from PCAP

### 2️⃣ HTTP Traffic Parsing & Detection
- Developed a custom Python HTTP parser
- Detected:
  - SQL Injection attempts
  - XSS payloads
  - Path traversal
  - Suspicious User-Agent
  - Proxy header usage

### 3️⃣ HTTPS Metadata Analysis
- Inspected TLS certificates using OpenSSL
- Extracted protocol version and cipher details
- Measured DNS, TCP, TLS, and total request timing

### 4️⃣ Automated Monitoring & Alerting
- Built real-time traffic monitoring script
- Implemented threshold-based alert system
- Logged suspicious activity automatically

---

## 📊 Key Outcomes
- Successfully captured and parsed HTTP traffic
- Identified simulated web attack patterns
- Analyzed TLS protocol and cipher strength
- Implemented automated web traffic monitoring
- Built reusable SOC-style detection scripts

---

## 🧠 Skills Demonstrated
- Packet-level web traffic inspection
- HTTP header and method analysis
- Web attack pattern detection
- TLS certificate inspection
- Bash & Python automation for SOC workflows

---

## ✅ Verification Checklist
✔ HTTP server running locally  
✔ Traffic captured in PCAP format  
✔ HTTP requests extracted successfully  
✔ Anomalies detected via parser  
✔ TLS certificate inspected  
✔ Timing metrics collected  
✔ Alerts triggered automatically  

---

## 🏁 Conclusion
This lab provided practical experience in HTTP/HTTPS traffic deconstruction.  
It strengthened foundational skills required for:

- Network security monitoring
- Web application attack detection
- SOC operations
- Blue team traffic inspection

The developed scripts and workflows replicate real-world security monitoring scenarios.
