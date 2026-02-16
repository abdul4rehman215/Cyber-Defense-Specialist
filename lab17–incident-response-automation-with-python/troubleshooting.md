# 🛠 Troubleshooting – Lab 17: Incident Response Automation

---

## Issue 1: Permission Denied When Running Scripts

### Symptoms
`
Permission denied
`

### Solution
- Ensure scripts are executable:
```

chmod +x script_name.py

```
- Verify file ownership:
```

ls -l scripts/

```
- Run using:
```

python3 script_name.py

```

---

## Issue 2: Module Import Errors

### Symptoms
`
ModuleNotFoundError: No module named 'collection'
`

### Solution
- Verify directory structure matches expected layout.
- Ensure `sys.path` includes the `scripts/` directory.
- Confirm correct import paths:

```python
  from collection.log_collector import LogCollector
```

* Run script from project root directory.

---

## Issue 3: No Incidents Detected

### Possible Causes

* Log files missing
* Regex patterns not matching log format
* Incorrect file paths

### Solution

* Verify log files exist:

  ```
  ls logs/system/
  ls logs/security/
  ls logs/application/
  ```
* Validate regex patterns match actual log entries.
* Print log contents manually for debugging.

---

## Issue 4: iptables Commands Fail

### Symptoms

`Permission denied`
`iptables not found`


### Solution

* Requires sudo privileges:

  ```
  sudo python3 script_name.py
  ```
* Check if iptables is installed:

  ```
  which iptables
  ```
* For safe testing, keep:

  ```
  "use_iptables": false
  ```

  in `response_config.json`

---

## Issue 5: No Tickets Generated

### Solution

* Confirm analysis report exists in:

  ```
  reports/incidents/
  ```
* Ensure incidents are present inside JSON report.
* Check that severity mappings are correctly configured.

---

## Issue 6: Logs Not Backed Up

### Solution

* Verify write permissions for `alerts/` directory:

  ```
  ls -la alerts/
  ```
* Ensure sufficient disk space:

  ```
  df -h
  ```

---

# 🏁 Final Conclusion

This lab successfully demonstrated a complete Incident Response Automation Framework built entirely with Python on Ubuntu 24.04.

### Implemented Capabilities:

* Automated multi-source log collection
* Regex-based threat detection engine
* Severity-based response workflows
* Simulated IP blocking
* Email alert simulation
* Incident ticket generation
* Log forensic backup
* Centralized response action logging
* Fully integrated automation pipeline

---

# 🔐 Key Takeaways

* Automation significantly reduces incident response time.
* Severity levels help prioritize response actions effectively.
* Logging all actions ensures auditability and compliance.
* Structured JSON reporting enables SOC scalability.
* Modular design improves maintainability and extensibility.

---

This framework models a simplified SOC automation engine and demonstrates how structured automation enhances security posture, consistency, and operational efficiency.
