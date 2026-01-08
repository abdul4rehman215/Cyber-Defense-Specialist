# 🛡️ Lab 02: SIEM Tool Configuration (Wazuh)

## 🧭 Lab Overview
This lab focuses on deploying and configuring **Wazuh SIEM** on a Linux system to collect, analyze, and respond to security events. It simulates real-world SOC activities such as log ingestion, alerting, file integrity monitoring, and automated response.

---

## 🎯 Objectives
- Understand SIEM fundamentals and SOC workflows  
- Install and configure Wazuh Manager and Agent  
- Collect authentication, system, and application logs  
- Configure log analysis and detection rules  
- Generate and analyze alerts using the Wazuh dashboard  
- Implement basic threat detection and response on Linux  

---

## 🧪 Lab Environment
- **Operating System:** Ubuntu 24.04.1 LTS  
- **User:** toor  
- **SIEM Stack:** Wazuh, Elasticsearch, Kibana  
- **Deployment Model:** Single-node (Manager + Agent)

---

## 🛠️ Tasks Performed
- Installed Wazuh Manager and Wazuh Agent  
- Integrated Elasticsearch for log storage  
- Configured Kibana with the Wazuh plugin  
- Enabled log collection for authentication, system, and Apache logs  
- Implemented File Integrity Monitoring (FIM)  
- Created custom detection rules  
- Generated real security events for validation  
- Enabled active response and alerting mechanisms  

---

## 🔍 Security Use Cases Demonstrated
- Detection of multiple failed login attempts  
- Monitoring unauthorized file changes in `/etc`  
- Real-time alert generation and analysis  
- Automated response to suspicious activity  

---

## 📊 Validation & Monitoring
- Verified all SIEM components are running  
- Confirmed agent connectivity and log ingestion  
- Observed alerts in the Wazuh dashboard  
- Monitored real-time security events  

---

## 🧠 Skills Gained
- SIEM deployment and configuration  
- Log analysis and correlation  
- Threat detection and alert tuning  
- SOC monitoring workflows  
- Linux security monitoring fundamentals  

---

## ✅ Conclusion
This lab demonstrates a complete **Wazuh-based SIEM deployment**, covering log collection, detection, alerting, and response. The workflow closely mirrors real-world SOC operations and strengthens practical security monitoring skills.

---

## 🚀 Next Enhancements
- Enable vulnerability detection modules  
- Add compliance and policy monitoring  
- Integrate threat intelligence feeds  
- Scale to multi-agent environments  

---

📌 All commands, scripts, outputs, troubleshooting steps, and interview Q&A are documented in this repository for full traceability.
