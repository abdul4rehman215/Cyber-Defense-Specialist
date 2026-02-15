# 📘 Interview Q&A – Lab 11: Incident Triage with Python Automation

---

## Q1. What was the primary objective of the Incident Triage Engine?
**Answer:**  
To automate the analysis, classification, and prioritization of security alerts using rule-based scoring and whitelist filtering within a SOC-style workflow.

---

## Q2. How does the system identify false positives?
**Answer:**  
It compares alert attributes (user, source IP, asset) against a predefined whitelist in `triage_rules.json`. If matched, the alert is marked as `FALSE_POSITIVE`.

---

## Q3. How is the priority score calculated?
**Answer:**  
The priority score is calculated by combining:
- Severity weight  
- Alert type weight  
- Event count threshold bonus  
- External IP bonus  

These values are defined in the triage rules configuration.

---

## Q4. Why are internal IP addresses treated differently?
**Answer:**  
Internal IP ranges (192.168.x.x, 10.x.x.x, 172.16.x.x) are considered lower risk because they typically represent internal network activity rather than external threats.

---

## Q5. What is the purpose of the AlertEnricher module?
**Answer:**  
The AlertEnricher adds contextual intelligence such as:
- IP reputation
- Malicious indicators
- External threat classification

This improves investigation accuracy.

---

## Q6. How are high-priority alerts determined?
**Answer:**  
Alerts with a priority level of `CRITICAL` or `HIGH` are classified as high-priority and are passed to the automated response module.

---

## Q7. What automated actions are triggered for CRITICAL alerts?
**Answer:**  
For CRITICAL alerts, the system:
- Isolates the affected host
- Notifies the SOC team
- Creates an incident ticket automatically

---

## Q8. Why is whitelist-based filtering important in SOC operations?
**Answer:**  
It reduces alert fatigue by filtering known legitimate or expected activities, allowing analysts to focus on real threats.

---

## Q9. What reports are generated after triage processing?
**Answer:**  
The system generates:
- `processed_alerts.json`
- `false_positives.json`
- `high_priority_alerts.json`
- `triage_summary.txt`
- `response_log.json`

---

## Q10. Why is modular design important in this automation system?
**Answer:**  
Modular design allows:
- Scalability
- Easier maintenance
- Independent testing of components
- Integration with additional enrichment or response modules
- Real-world SOC pipeline expansion
