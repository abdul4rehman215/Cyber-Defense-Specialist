# 📘 Interview Q&A – Lab 12: SOC Playbooks Development

---

### Q1. What is the purpose of the BasePlaybook class?

**Answer:**  
The BasePlaybook class provides a reusable framework for SOC automation. It handles structured logging, command execution, alert generation, incident ID creation, and report generation. All other playbooks inherit from this base class.

---

### Q2. How are incident IDs generated in the framework?

**Answer:**  
Incident IDs are automatically generated using a timestamp format:
INC-YYYYMMDD-HHMMSS
This ensures uniqueness and traceability of each incident.

---

### Q3. What indicators does the Malware Detection Playbook use to detect threats?

**Answer:**  
It detects:
- Processes running from `/tmp` or `/dev/shm`
- Suspicious command-line patterns like `nc` or reverse shells
- Script files in temporary directories
- World-writable files

---

### Q4. How are malicious files handled in the malware playbook?

**Answer:**  
Suspicious files are:
1. Hashed using SHA256
2. Moved to a quarantine directory
3. Logged in structured incident logs

---

### Q5. What actions are performed during a Network Intrusion response?

**Answer:**  
The playbook:
- Lists listening ports
- Analyzes active network connections
- Detects repeated IP connections
- Checks authentication logs for failed logins
- Blocks malicious IPs using iptables
- Terminates processes on suspicious ports

---

### Q6. How does the playbook differentiate private and external IP addresses?

**Answer:**  
It checks whether an IP starts with:
- `10.`
- `192.168.`
- `172.16.`
- `127.`

If not, it is treated as external and potentially suspicious.

---

### Q7. What is the purpose of the System Isolation Playbook?

**Answer:**  
The System Isolation Playbook:
- Collects forensic evidence
- Captures system and memory information
- Backs up firewall rules
- Blocks incoming and outgoing traffic
- Stops critical services
- Creates an evidence archive

---

### Q8. How is network isolation implemented?

**Answer:**  
Network isolation is implemented using `iptables`:
- Setting INPUT policy to DROP
- Setting OUTPUT policy to DROP
- Backing up existing firewall rules before modification

---

### Q9. Why is structured logging important in SOC automation?

**Answer:**  
Structured logging ensures:
- Auditability
- Traceability of actions
- Incident documentation
- Easier investigation and reporting

Logs are stored in JSON format for consistency.

---

### Q10. What are the advantages of modular SOC playbooks?

**Answer:**  
Modular playbooks:
- Allow code reuse
- Improve scalability
- Enable easier maintenance
- Support automation workflows
- Simulate real-world SOC orchestration pipelines
