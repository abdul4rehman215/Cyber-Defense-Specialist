# 📘 Interview Q&A – Lab 01: SOC Mission & Workflow Fundamentals

---

## Q1. What is the primary mission of a Security Operations Center (SOC)?
**Answer:**  
The primary mission of a SOC is to continuously monitor, detect, analyze, and respond to cybersecurity incidents in order to protect an organization’s information assets and ensure confidentiality, integrity, and availability.

---

## Q2. What are the core components of a SOC mission?
**Answer:**  
The core components of a SOC mission include prevention, detection, response, recovery, and continuous improvement.

---

## Q3. What SOC maturity level was implemented in this lab and what was the target level?
**Answer:**  
This lab implemented a Level 2 (Developing) SOC, with the target maturity level set to Level 3 (Defined).

---

## Q4. Which open-source SIEM platform was deployed in this lab?
**Answer:**  
The ELK stack was deployed, which consists of Elasticsearch, Logstash, and Kibana.

---

## Q5. What role does Elasticsearch play in a SOC environment?
**Answer:**  
Elasticsearch stores, indexes, and enables fast searching of security logs and events, making it a core component of SIEM platforms.

---

## Q6. Why is Logstash used in the SIEM architecture?
**Answer:**  
Logstash is used to collect, parse, and transform logs from multiple sources before sending them to Elasticsearch for indexing and analysis.

---

## Q7. What is the purpose of Kibana in this lab?
**Answer:**  
Kibana provides visualization, search, and analysis capabilities, allowing SOC analysts to explore logs, build dashboards, and investigate incidents.

---

## Q8. How were security events generated for testing purposes?
**Answer:**  
Security events were generated using a Bash script that utilized the `logger` command to simulate failed SSH logins, successful logins, firewall blocks, and system service events.

---

## Q9. What tool was used to implement alerting and what types of events did it detect?
**Answer:**  
ElastAlert was used to implement alerting. It detected events such as failed SSH login attempts and other suspicious system activities.

---

## Q10. Why is alerting important in a SOC environment?
**Answer:**  
Alerting enables SOC teams to quickly identify and respond to potential security incidents, reducing detection and response times.

---

## Q11. What is the significance of SOC documentation?
**Answer:**  
SOC documentation standardizes operational procedures, improves response consistency, and supports knowledge transfer among analysts.

---

## Q12. What KPIs were defined for measuring SOC performance in this lab?
**Answer:**  
Key performance indicators included Mean Time to Detection (MTTD), Mean Time to Response (MTTR), number of incidents detected and resolved, false positive rate, and system availability.

---

## Q13. How does SOC maturity improve security posture?
**Answer:**  
Higher SOC maturity introduces standardized processes, automation, advanced analytics, and proactive threat hunting, resulting in faster and more effective incident response.

---

## Q14. What real-world SOC skills were developed in this lab?
**Answer:**  
Skills developed include SIEM deployment, log analysis, alert configuration, incident detection, SOC documentation, and operational workflow design.

---

## Q15. How does this lab prepare someone for a SOC Analyst role?
**Answer:**  
The lab provides hands-on experience with real SOC tools and workflows, mirroring tasks performed by SOC analysts in enterprise environments, including monitoring, detection, alerting, and investigation.

---
