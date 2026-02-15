# 📘 Interview Q&A – Lab 13: SOAR Tool Integration

## 1. What is SOAR in cybersecurity?
SOAR (Security Orchestration, Automation, and Response) is a platform that integrates security tools, automates incident response workflows, and orchestrates actions across multiple systems to reduce manual effort and improve response speed.

---

## 2. Why were Wazuh, TheHive, and Cortex integrated in this lab?
- **Wazuh** provides SIEM alert generation.
- **TheHive** manages cases and investigations.
- **Cortex** performs automated analysis.
Together, they create a complete automated SOC workflow.

---

## 3. What is the role of the WazuhConnector?
The WazuhConnector:
- Authenticates with the Wazuh API
- Retrieves alerts based on severity level
- Provides agent information for enrichment

It acts as the SIEM ingestion component of the SOAR system.

---

## 4. What is the function of the TheHiveConnector?
The TheHiveConnector:
- Logs into TheHive API
- Creates incident cases
- Adds observables (e.g., IP addresses)
- Updates case status

It bridges automation to case management.

---

## 5. How does the orchestrator decide which playbook to run?
The orchestrator:
- Reads rule IDs from Wazuh alerts
- Compares them against rule IDs defined in `config.yaml`
- Routes alerts to the appropriate playbook (malware or brute force)

This is rule-based alert routing.

---

## 6. What happens after a playbook executes?
After execution:
- Playbook returns structured results
- A case is automatically created in TheHive
- Observables (e.g., source IP) are added
- Actions are logged for auditing

---

## 7. Why is Docker used in this deployment?
Docker provides:
- Service isolation
- Easy deployment and rollback
- Reproducible environments
- Reduced dependency conflicts

It ensures stable SOAR infrastructure.

---

## 8. Why is authentication validated before starting the workflow loop?
Authentication is validated to:
- Ensure APIs are reachable
- Confirm credentials are correct
- Prevent runtime failures
- Avoid endless alert polling failures

---

## 9. How does SOAR improve SOC efficiency?
SOAR:
- Automates repetitive tasks
- Reduces mean time to respond (MTTR)
- Ensures consistent response procedures
- Minimizes analyst workload
- Enables 24/7 automated monitoring

---

## 10. Why is logging critical in SOAR systems?
Logging provides:
- Audit trail of automated actions
- Troubleshooting visibility
- Compliance evidence
- Detection of automation failures
- Operational transparency
