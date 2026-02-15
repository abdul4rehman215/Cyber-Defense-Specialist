# 🛠 Troubleshooting – Lab 12: SOC Playbooks Development

---

## 1️⃣ Permission Errors

### ❌ Problem:
Commands like `iptables`, `systemctl`, or `netstat` fail with permission denied errors.

### ✅ Solution:
- Run playbooks with sudo if required:
```

sudo python3 scripts/system_isolation.py

```
- Ensure logs directory has correct permissions:
```

chmod -R 755 logs/

```
- Verify user has sudo privileges:
```

sudo -l

```

---

## 2️⃣ Import Errors (ModuleNotFoundError)

### ❌ Problem:
Error importing `base_playbook` in other scripts.

Example:
```

ModuleNotFoundError: No module named 'base_playbook'

````

### ✅ Solution:
- Verify this line exists in all playbooks:

```python
  sys.path.append(os.path.dirname(os.path.abspath(__file__)))
```
* Confirm `base_playbook.py` exists inside `scripts/`
* Ensure you are running from project root:

  ```
  cd ~/soc_playbooks
  python3 scripts/malware_detection.py
  ```

---

## 3️⃣ psutil Not Installed

### ❌ Problem:

```
ModuleNotFoundError: No module named 'psutil'
```

### ✅ Solution:

Install required dependency:

```
pip3 install psutil
```

Verify:

```
python3 -c "import psutil"
```

---

## 4️⃣ netstat or lsof Command Not Found

### ❌ Problem:

```
netstat: command not found
lsof: command not found
```

### ✅ Solution:

Install required packages:

```
sudo apt update
sudo apt install net-tools lsof -y
```

---

## 5️⃣ iptables Rules Not Applied

### ❌ Problem:

IP blocking or network isolation does not work.

### ✅ Solution:

* Ensure script is run with sudo:

  ```
  sudo python3 scripts/network_intrusion.py
  ```
* Verify iptables status:

  ```
  sudo iptables -L
  ```
* Confirm rules were added successfully.

---

## 6️⃣ No Threats Detected During Testing

### ❌ Problem:

Playbooks run successfully but no suspicious activity is detected.

### ✅ Solution:

### For Malware Detection:

Create test suspicious file:

```
echo "malicious content" > /tmp/malicious.sh
chmod 777 /tmp/malicious.sh
```

### For Network Intrusion:

Simulate suspicious connection:

```
nc -lvp 4444
```

### For Failed Login Simulation:

Trigger failed login attempts via SSH.

---

## 7️⃣ Logs Not Generated

### ❌ Problem:

No logs appear in logs/ directory.

### ✅ Solution:

* Ensure directories exist:

  ```
  tree logs/
  ```
* Confirm write permissions:

  ```
  ls -ld logs
  ```
* Verify logging setup in `BasePlaybook`.

---

## 8️⃣ System Isolation Breaks Network (Test Environment Only)

### ⚠ Warning:

The System Isolation Playbook sets:

```
iptables -P INPUT DROP
iptables -P OUTPUT DROP
```

This blocks all traffic.

### ✅ Solution:

Restore network:

```
sudo iptables-restore < logs/incidents/iptables_backup.rules
```

---

## 9️⃣ Quarantine Fails (File Not Found)

### ❌ Problem:

Error when moving suspicious files.

### ✅ Solution:

* Ensure file exists before quarantine
* Check file permissions
* Confirm path validity in scan results

---

## 🔟 Evidence Archive Not Created

### ❌ Problem:

ZIP file missing after isolation.

### ✅ Solution:

* Verify evidence directory exists:

  ```
  ls logs/incidents/
  ```
* Confirm shutil.make_archive executed successfully
* Check disk space:

  ```
  df -h
  ```

---

# 🔎 Debugging Tips

• Add temporary print statements inside playbook methods
• Run individual commands manually before automation
• Increase timeout in execute_command() if needed
• Check logs in logs/incidents/ for detailed error information

---

# ✅ Verification Checklist

Before final submission ensure:

* All scripts are executable:

  ```
  chmod +x scripts/*.py
  ```
* Logs generated inside:

  * logs/incidents/
  * logs/alerts/
  * logs/reports/
* JSON reports created successfully
* Quarantine and evidence directories created
* Alerts written to alerts.log

---

# 🎯 Final Reminder

⚠ Always test System Isolation Playbook in a controlled lab environment only.
⚠ Do NOT run destructive playbooks on production systems.

This troubleshooting guide ensures stable execution of SOC automation workflows.
Next lab when ready.
