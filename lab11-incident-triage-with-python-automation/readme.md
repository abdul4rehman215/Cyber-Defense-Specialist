# 🧪 Lab 11: Incident Triage with Python Automation

---

## 🔹 Lab Environment

| Component | Details |
|------------|----------|
| OS | Ubuntu 24.04.1 LTS (EC2 – Alnafi Cloud) |
| User | toor |
| Interface | ens5 |
| Working Directory | /home/toor/incident_triage_lab |
| Python Version | 3.12.x |

---

## 🎯 Objectives

✔ Automate security alert triage  
✔ Implement whitelist-based false positive filtering  
✔ Apply rule-based priority scoring  
✔ Enrich alerts with threat intelligence  
✔ Automate response actions & ticket creation  
✔ Build complete SOC-style workflow  

---

## 📁 Project Structure

```
incident_triage_lab/
│
├── data/
│   └── sample_alerts.json
│
├── rules/
│   └── triage_rules.json
│
├── scripts/
│   ├── incident_triage.py
│   ├── alert_enrichment.py
│   ├── automated_response.py
│   └── complete_workflow.py
│
├── reports/
│   ├── processed_alerts.json
│   ├── false_positives.json
│   ├── high_priority_alerts.json
│   ├── triage_summary.txt
│   └── response_log.json
│
├── commands.sh
├── output.txt
├── interviewqna.md
└── troubleshooting.md
```

---

## 🛠 Lab Workflow Overview

This lab simulates a Security Operations Center (SOC) triage pipeline.

### Phase 1 – Alert Processing
- Load JSON alerts
- Apply whitelist filtering
- Calculate rule-based priority score
- Classify alert severity

### Phase 2 – Alert Enrichment
- Add IP reputation
- Identify malicious indicators
- Determine internal vs external threat

### Phase 3 – Automated Response
- Generate SOC response actions
- Create incident tickets
- Send security notifications

### Phase 4 – Full SOC Workflow
- Execute triage
- Enrich alerts
- Trigger automated response
- Generate reports

---

## ⚙️ Core Components

### 🔹 1. IncidentTriageEngine
- Loads rules
- Filters false positives
- Calculates priority score
- Categorizes alerts

### 🔹 2. AlertEnricher
- Adds IP reputation
- Detects malicious indicators
- Flags external threats

### 🔹 3. AutomatedResponder
- Generates response actions
- Creates SOC-style tickets
- Logs automated responses

### 🔹 4. Complete Workflow
- Integrates triage + enrichment + response
- Produces structured JSON and text reports

---

## 📊 Alert Classification Logic

Priority score is calculated using:

- Severity weight
- Alert type weight
- Event count
- External source IP bonus

### Priority Levels

| Score Range | Priority |
|-------------|----------|
| ≥ 15 | CRITICAL |
| ≥ 10 | HIGH |
| ≥ 5 | MEDIUM |
| < 5 | LOW |

---

## 🧠 False Positive Filtering

Alerts are automatically marked FALSE_POSITIVE if:

- User is whitelisted
- Source IP is whitelisted
- Asset is whitelisted

This prevents alert fatigue in SOC operations.

---

## 📈 Reports Generated

After execution, the following files are created:

- processed_alerts.json
- false_positives.json
- high_priority_alerts.json
- triage_summary.txt
- response_log.json

---

## 🚀 How to Run

```bash
chmod +x scripts/*.py

python3 scripts/incident_triage.py
python3 scripts/alert_enrichment.py
python3 scripts/automated_response.py
python3 scripts/complete_workflow.py
```

---

## 🔐 Security Insight

This lab demonstrates how real SOC teams:

- Reduce alert fatigue
- Automate prioritization
- Enrich alerts with intelligence
- Trigger automated containment
- Generate structured reports

Automation dramatically improves incident response efficiency and scalability.

---

## ✅ Expected Outcomes

- ✔ 5 alerts processed  
- ✔ False positives filtered  
- ✔ High-priority alerts identified  
- ✔ Threat enrichment applied  
- ✔ Incident tickets generated  
- ✔ JSON & text reports created  
- ✔ Complete SOC-style automation pipeline implemented  

---

## 🏁 Conclusion

This lab implemented a fully automated SOC triage workflow including:

- Rule-based triage
- Threat intelligence enrichment
- Automated response
- Ticket generation
- Structured reporting

It simulates enterprise-level incident response automation pipelines used in modern Security Operations Centers.
