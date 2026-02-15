# 🧪 Lab 13: SOAR Tool Integration

---

# 🎯 Objectives

- Install and configure Wazuh SIEM
- Deploy TheHive case management platform
- Deploy Cortex analysis engine
- Integrate systems via Python API connectors
- Build automated response playbooks
- Implement workflow orchestration
- Validate automated SOAR execution

---

## 📌 Prerequisites

- Basic Linux command line proficiency
- Understanding of security incident response concepts
- Familiarity with SIEM systems and log analysis
- Basic Python scripting knowledge
- Understanding of JSON and YAML formats

---

## 🔹 Lab Environment

| Component | Value |
|------------|--------|
| OS | Ubuntu 24.04 LTS (Cloud VM) |
| User | toor |
| Docker | Engine + Compose Plugin |
| Working Directory | /home/toor |
| Deployment Model | All services containerized |

All services were deployed using Docker for isolation, portability, and simplified management.

---

# 🏗️ Architecture Overview

This lab simulates a real-world SOAR architecture where:

- **Wazuh** generates security alerts
- A **Python Orchestrator** pulls alerts via API
- Alerts are routed to automated **response playbooks**
- Cases are created automatically in **TheHive**
- Observables (IPs, hashes, etc.) are added to cases
- Logging and monitoring track execution flow

```
Wazuh → Python Orchestrator → Playbooks → TheHive
                                      ↘ Cortex
```

---

# 🛠 Task 1: Deploy SOAR Core Components

### Purpose

To build the foundational SOAR stack using open-source tools deployed in Docker containers.

### What Was Performed

- Docker installation and verification
- Deployment of **Wazuh SIEM**
- Deployment of **TheHive** case management platform
- Deployment of **Cortex** analysis engine
- Verification that all containers were running
- Validation of web dashboards accessibility

This task establishes the operational SOAR environment.

---

# 🛠 Task 2: Develop SOAR Integration Framework

### Purpose

To create Python-based API connectors that allow communication between:

- Wazuh (alert source)
- TheHive (case management)
- Playbook modules

### What Was Implemented

- Wazuh API authentication and alert retrieval connector
- TheHive API login and case creation connector
- Configuration file (`config.yaml`) for routing and thresholds
- Logging system for SOAR operations

This task enables automated alert ingestion and case management.

---

# 🛠 Task 3: Implement Automated Response Playbooks

### Purpose

To automate security response actions based on alert type.

### Playbooks Created

- **Malware Response Playbook**
  - Host isolation
  - Forensic data collection
  - Antivirus scan execution
  - IOC sharing

- **Brute Force Response Playbook**
  - Source IP blocking
  - Attack pattern analysis
  - Account compromise check
  - Policy enforcement

These playbooks simulate real SOC response procedures.

---

# 🛠 Task 4: Workflow Orchestration Engine

### Purpose

To automate end-to-end incident handling.

### What the Orchestrator Does

- Continuously polls Wazuh for alerts
- Routes alerts based on rule IDs
- Executes corresponding playbooks
- Creates cases in TheHive automatically
- Adds observables (e.g., IP addresses)
- Logs all activities

This represents the core SOAR automation logic.

---

# 🛠 Task 5: Integration Testing & Validation

### Purpose

To ensure the integration works correctly before production deployment.

### Validation Performed

- Wazuh API authentication tested
- TheHive login verified
- Automated case creation confirmed
- Playbook execution validated
- Logging verified
- Docker container health confirmed

---

# 📂 Directory Structure

```
soar-integration/
├──commands.sh
├──output.txt
├──interviewqna.md
├──troubleshooting.md
├──scripts/
├── test
├── config.yaml
└── main.py
   ├── connectors/
   ├── playbooks/
   ├── workflows/
   ├── logs/
```

---

# 🚀 Platform Execution Flow

1. Start orchestration engine
2. Authenticate with Wazuh
3. Authenticate with TheHive
4. Pull alerts
5. Route to playbooks
6. Execute automated response
7. Create case in TheHive
8. Add observables
9. Log results
10. Continue monitoring loop

---

# ✅ Final Validation

✔ Wazuh operational  
✔ TheHive operational  
✔ Cortex operational  
✔ API connectors functional  
✔ Playbooks triggered automatically  
✔ Alerts routed correctly  
✔ Cases created automatically  
✔ Observables added automatically  
✔ Logging operational  

---

# 🔐 Security Relevance

This lab demonstrates how modern Security Operations Centers:

- Reduce manual workload through automation
- Improve response time
- Standardize incident handling
- Integrate SIEM and case management systems
- Build scalable SOAR architectures

It reflects enterprise-level SOAR implementation design.
