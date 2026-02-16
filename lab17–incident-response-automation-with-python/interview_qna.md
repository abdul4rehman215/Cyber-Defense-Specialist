# 📘 Interview Q&A – Lab 17: Incident Response Automation with Python

---

## Q1. What was the main objective of this lab?
**A:** To build a complete automated incident response framework using Python that integrates log collection, analysis, and automated response actions.

---

## Q2. What are the three main components of the automation system?
**A:**
1. Log Collection  
2. Log Analysis  
3. Automated Incident Response  

---

## Q3. How were security incidents detected in the logs?
**A:** Using regular expressions (regex) to match known attack patterns such as failed logins, SQL injection attempts, XSS attempts, and privilege escalation commands.

---

## Q4. How were incidents categorized by severity?
**A:** Each incident type was mapped to a predefined severity level:
- `failed_login` → medium  
- `sql_injection` → high  
- `xss_attempt` → medium  
- `privilege_escalation` → critical  

---

## Q5. What happens when a critical incident is detected?
**A:** The system:
- Simulates blocking the source IP
- Sends an alert notification
- Creates an incident ticket
- Backs up logs for forensic preservation

---

## Q6. How were incident tickets generated?
**A:** JSON-based ticket files were automatically created inside the `alerts/` directory with unique IDs formatted as:
INC-<timestamp>-<incident_type>

---

## Q7. Why was IP blocking simulated in this lab?
**A:** To safely demonstrate automation logic without modifying real firewall rules or affecting system connectivity.

---

## Q8. What is the purpose of backing up logs during critical incidents?
**A:** To preserve forensic evidence before additional system changes occur, ensuring data integrity for investigation.

---

## Q9. How does the integrated automation script work?
**A:** The script `automated_response.py` sequentially executes:
1. Log collection
2. Log analysis
3. Incident response  
All within a single execution workflow.

---

## Q10. Why is action logging important in incident response automation?
**A:** It creates a structured audit trail that supports:
- Accountability
- Compliance verification
- Post-incident forensic review
- Change tracking

---

## Q11. How does severity-based response improve SOC efficiency?
**A:** It ensures that high-risk incidents trigger stronger remediation actions, reducing response time and prioritizing critical threats.

---

## Q12. How can this framework be extended for production use?
**A:** By:
- Integrating real SIEM systems
- Connecting to SMTP servers for actual email alerts
- Using real firewall APIs for IP blocking
- Adding database storage for incident history
- Implementing dashboard visualization

---

# ✅ Key Interview Takeaway

This lab demonstrates how automation significantly reduces incident response time, improves consistency, and ensures reliable security enforcement in SOC environments.
