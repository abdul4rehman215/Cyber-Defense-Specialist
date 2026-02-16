# 🌐 Lab 03: Analyzing Network Traffic with Wireshark

## 🧭 Lab Overview
This lab focuses on capturing and analyzing network traffic using **Wireshark and TShark** on Linux. The objective is to understand packet-level visibility and identify suspicious patterns in DNS, HTTP, and TLS traffic, simulating real SOC network investigations.

---

## 🎯 Objectives
- Install and configure Wireshark on Linux  
- Capture live network traffic safely as a non-root user  
- Analyze DNS, HTTP, and TLS traffic  
- Apply capture and display filters  
- Identify anomalies and suspicious patterns  
- Generate automated traffic analysis reports  

---

## 🧪 Lab Environment
- **Operating System:** Ubuntu Linux  
- **User:** toor  
- **Host:** ip-172-31-10-212  
- **Tools Used:** Wireshark, TShark, curl, dnsutils  

---

## 🛠️ Tasks Performed
- Installed Wireshark and configured non-root packet capture  
- Identified active network interfaces for monitoring  
- Captured live DNS, HTTP, and HTTPS traffic  
- Applied protocol-specific capture and display filters  
- Generated realistic traffic for analysis  
- Analyzed DNS queries for suspicious domains  
- Examined HTTP headers, methods, and user agents  
- Inspected TLS handshakes, cipher suites, and certificates  
- Created automated analysis and reporting scripts  

---

## 🔍 Security Analysis Performed
- Detection of suspicious DNS queries and NXDOMAIN responses  
- Identification of unusual HTTP User-Agent strings  
- Validation of TLS versions and encryption strength  
- Detection of certificate and handshake anomalies  

---

## 🧠 Skills Gained
- Packet-level network traffic analysis  
- Wireshark filtering techniques  
- Network-based threat detection  
- DNS, HTTP, and TLS security inspection  
- SOC-style investigation and reporting  

---

## ✅ Conclusion
This lab demonstrates practical **network traffic analysis skills** required in SOC environments. By inspecting packets at multiple protocol layers, it strengthens the ability to detect anomalies, investigate incidents, and understand attacker behavior at the network level.

---

📌 All commands, scripts, outputs, troubleshooting steps, and interview Q&A are included in this repository for complete lab traceability.
