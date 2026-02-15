# 🛠 Troubleshooting Guide – Lab 11: Incident Triage with Python Automation

---

## Issue 1: JSON Parsing Errors

### Symptoms
- Script fails with JSONDecodeError
- Unexpected syntax errors when loading alerts or rules

### Solution
Validate JSON files:

```bash
python3 -m json.tool data/sample_alerts.json
python3 -m json.tool rules/triage_rules.json
```

Check for:
- Missing commas
- Incorrect brackets
- Improper quotes
- Invalid UTF-8 encoding

---

## Issue 2: All Alerts Marked as False Positives

### Possible Causes
- Whitelist configuration too broad
- Incorrect field names in whitelist
- is_whitelisted() logic matching unintended fields

### Solution
Review whitelist settings:

```bash
cat rules/triage_rules.json
```

Ensure:
- Only intended users are whitelisted
- IPs are correctly defined
- Asset names match alert data exactly

---

## Issue 3: Incorrect Priority Scores

### Possible Causes
- Misconfigured severity_weights
- Missing alert_type_weights
- Scoring logic not applied correctly

### Solution
Verify scoring rules:

```bash
cat rules/triage_rules.json
```

Add debug print statements inside:

```python
print("Calculated Score:", score)
```

Confirm event_count and external IP logic are triggering correctly.

---

## Issue 4: File Not Found Errors

### Symptoms
- Alerts file not found
- Rules file not found
- Reports directory missing

### Solution
Verify current working directory:

```bash
pwd
```

It should be:

```
/home/toor/incident_triage_lab
```

If needed, use absolute paths:

```python
os.path.join(os.getcwd(), "data", "sample_alerts.json")
```

---

## Issue 5: Enrichment Not Detecting Malicious IPs

### Possible Causes
- IP not present in threat_intel list
- Typo in threat intelligence data

### Solution
Check enrichment module:

```bash
nano scripts/alert_enrichment.py
```

Verify malicious IP list contains expected values.

---

## Issue 6: Automated Response Not Generating Tickets

### Possible Causes
- No alerts classified as HIGH or CRITICAL
- high_priority_alerts.json is empty

### Solution
Verify high priority alerts:

```bash
cat reports/high_priority_alerts.json
```

Ensure priority_level values are:
- CRITICAL
- HIGH

---

## Issue 7: Permission Denied Errors

### Solution

Make scripts executable:

```bash
chmod +x scripts/*.py
```

If necessary:

```bash
chmod -R 755 ~/incident_triage_lab
```

---

## Final Validation Checklist

Run full workflow:

```bash
python3 scripts/incident_triage.py
python3 scripts/alert_enrichment.py
python3 scripts/automated_response.py
python3 scripts/complete_workflow.py
```

Verify reports:

```bash
ls -lh reports/
```

Expected files:

- processed_alerts.json
- false_positives.json
- high_priority_alerts.json
- triage_summary.txt
- response_log.json

---

## Security Best Practice Reminder

- Always validate input JSON files
- Keep whitelist minimal
- Continuously update threat intelligence data
- Log all automated actions
- Review high-priority alerts manually before containment
