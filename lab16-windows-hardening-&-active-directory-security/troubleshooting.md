# 🛠 Troubleshooting Guide – Lab 16 - Windows Hardening & Active Directory Security

---

## Issue 1: PowerShell script fails to execute

### Possible Causes
- Script does not have execute permission
- PowerShell Core not installed
- Incorrect script path

### Solutions
```bash
chmod +x scripts/*.ps1
pwsh --version
pwsh scripts/ad-security-automation.ps1
````

Verify PowerShell is installed and accessible.

---

## Issue 2: Configuration file not found

### Possible Causes

* Incorrect relative path
* File not created inside configs directory
* Typo in filename

### Solutions

```bash
ls configs/
cat configs/ad-config.json
```

Ensure the script path matches the file structure.

---

## Issue 3: JSON parsing errors

### Possible Causes

* Missing comma
* Incorrect bracket structure
* Invalid JSON formatting

### Solutions

```bash
cat configs/ad-config.json | jq
```

Or validate using an online JSON validator.

---

## Issue 4: Log files not being created

### Possible Causes

* logs directory missing
* Insufficient write permissions

### Solutions

```bash
mkdir -p logs
ls -la logs
```

Ensure the script has permission to write inside the logs directory.

---

## Issue 5: Security Monitor fails with missing file error

### Possible Causes

* AD automation script not executed first
* Registry hardening script not executed

### Correct Execution Order

```bash
pwsh scripts/ad-security-automation.ps1
pwsh scripts/registry-hardening.ps1
pwsh scripts/security-monitor.ps1
pwsh scripts/generate-report.ps1
```

The monitor depends on previous reports.

---

## Issue 6: HTML report not generated

### Possible Causes

* security-monitor-summary.json missing
* File path incorrect

### Solutions

```bash
ls logs/
pwsh scripts/generate-report.ps1
```

Confirm required JSON summary files exist before generating the report.

---

## Issue 7: Compliance score incorrect

### Possible Causes

* JSON configuration changed
* Policy values outside expected thresholds

### Solution

Review:

* configs/ad-config.json
* configs/registry/security-registry.json

Ensure policy values meet required security standards.

---

## Best Practice Recommendations

* Always validate JSON configuration before execution.
* Run scripts in defined order.
* Keep backup copies of configuration files.
* Use structured logging for audit tracking.
* Regularly review compliance reports.

---

## Final Validation Checklist

✔ PowerShell Core installed
✔ AD automation executed successfully
✔ Registry compliance at expected percentage
✔ Security monitor score calculated
✔ HTML report generated
✔ All logs saved in logs/ directory
