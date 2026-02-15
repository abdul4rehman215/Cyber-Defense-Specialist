# 🛠 Troubleshooting Guide – Lab 09  
## Email Header Analysis for Threats

---

## 1️⃣ DNS Resolution Issues

### ❌ Problem:
SPF, DKIM, or DMARC validation returns:

```
DNS Error: The DNS response does not contain an answer.
```

### 🔍 Possible Causes:
- No internet connectivity
- Incorrect DNS configuration
- Target domain has no SPF/DKIM/DMARC record
- EC2 DNS resolver misconfiguration

### ✅ Solution:

Check network connectivity:
```
ping 8.8.8.8
```

Temporarily fix DNS:
```
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

Test DNS resolution manually:
```
dig company.com TXT
dig _dmarc.company.com TXT
```

---

## 2️⃣ Module Import Errors

### ❌ Problem:
```
ModuleNotFoundError: No module named 'dns'
```

### 🔍 Cause:
Required Python libraries not installed.

### ✅ Solution:

Verify installed packages:
```
pip3 list
```

Reinstall dependencies:
```
pip3 install --upgrade dnspython email-validator
```

If virtual environment is used:
```
source venv/bin/activate
pip install dnspython email-validator
```

---

## 3️⃣ Permission Denied Errors

### ❌ Problem:
```
Permission denied: scripts/header_analyzer.py
```

### 🔍 Cause:
Script not executable.

### ✅ Solution:
```
chmod +x scripts/*.py
```

For sample files:
```
chmod 644 samples/*.eml
```

---

## 4️⃣ Incorrect File Paths

### ❌ Problem:
```
FileNotFoundError: samples/legitimate.eml not found
```

### 🔍 Cause:
Running script from incorrect directory.

### ✅ Solution:

Ensure working directory:
```
cd ~/email_lab
```

Run script using correct relative path:
```
python3 scripts/threat_reporter.py
```

Or use absolute path:
```
python3 ~/email_lab/scripts/threat_reporter.py
```

---

## 5️⃣ SPF Record Not Found

### ❌ Problem:
SPF returns "None".

### 🔍 Cause:
The domain may not publish SPF.

### ✅ Solution:

Verify manually:
```
dig company.com TXT | grep spf
```

If absent, create test record (for lab simulation):
```
v=spf1 ip4:192.0.2.0/24 -all
```

---

## 6️⃣ DKIM Validation Always False

### ❌ Problem:
```
Public key not found.
```

### 🔍 Cause:
- DNS does not contain DKIM selector record
- Domain is fictional (lab environment)
- Network blocked DNS TXT queries

### ✅ Solution:

Verify manually:
```
dig default._domainkey.company.com TXT
```

Ensure selector and domain match DKIM header.

---

## 7️⃣ DMARC Record Missing

### ❌ Problem:
```
No DMARC record found.
```

### 🔍 Cause:
Domain does not publish DMARC policy.

### ✅ Solution:

Verify:
```
dig _dmarc.company.com TXT
```

Example DMARC record:
```
v=DMARC1; p=quarantine; pct=100;
```

---

## 8️⃣ Threat Score Seems Unexpected

### ❌ Problem:
Legitimate email shows LOW instead of MINIMAL.

### 🔍 Explanation:
Threat score also accounts for:
- Missing SPF
- Missing DKIM
- Missing DMARC alignment

Even clean headers may receive minor scoring penalties.

---

## 9️⃣ JSON Report Not Generated

### ❌ Problem:
No file appears in `output/` directory.

### 🔍 Cause:
Output directory not created automatically.

### ✅ Solution:

Create manually:
```
mkdir -p output
```

Re-run reporter:
```
python3 scripts/threat_reporter.py
```

---

## 🔟 General Debugging Tips

Enable verbose debugging inside scripts:
```python
print(variable_name)
```

Check Python version:
```
python3 --version
```

Check working directory:
```
pwd
```

List directory contents:
```
ls -lah
```

---

# 🔐 Security Best Practices Reminder

- Never open suspicious `.eml` attachments directly.
- Validate authentication records before trusting sender.
- Always verify DNS resolution.
- Combine SPF + DKIM + DMARC for reliable detection.
- Automate scoring to reduce human error.

---

# ✅ Lab Validation Checklist

✔ Header parser working  
✔ Spoofing detection functional  
✔ SPF validation tested  
✔ DKIM validation tested  
✔ DMARC policy logic tested  
✔ Integrated threat scoring verified  
✔ JSON report generation confirmed  

---

