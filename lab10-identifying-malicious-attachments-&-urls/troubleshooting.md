# 🛠 Troubleshooting Guide – Lab 10 - Identifying Malicious Attachments & URLs

---

## 1️⃣ Import Errors (Module Not Found)

### Issue:
```
ModuleNotFoundError: No module named 'magic'
ModuleNotFoundError: No module named 'requests'
ModuleNotFoundError: No module named 'bs4'
```

### Solution:

Upgrade or reinstall required Python packages:

```bash
pip3 install --upgrade python-magic requests beautifulsoup4
```

If using system-wide installation:

```bash
sudo pip3 install python-magic requests beautifulsoup4
```

---

## 2️⃣ Magic Library Errors (MIME Detection Issues)

### Issue:
```
ImportError: failed to find libmagic
```

### Cause:
System-level `libmagic` dependency is missing.

### Solution:

Install required system packages:

```bash
sudo apt update
sudo apt install libmagic1 python3-magic file -y
```

Verify installation:

```bash
file samples/document.txt
```

---

## 3️⃣ Permission Denied Errors

### Issue:
```
Permission denied: attachment_scanner.py
```

### Solution:

Make Python scripts executable:

```bash
chmod +x ~/malware_lab/*.py
```

If sample files have restricted permissions:

```bash
chmod 644 samples/*
```

---

## 4️⃣ Network Timeout During URL Scanning

### Issue:
```
requests.exceptions.ConnectTimeout
requests.exceptions.ReadTimeout
```

### Cause:
- Slow internet
- Firewall restrictions
- Target site blocking requests

### Solution:

1. Increase timeout in `url_analyzer.py`:
```python
response = requests.get(url, headers=headers, timeout=10)
```

2. Verify internet connectivity:
```bash
ping 8.8.8.8
```

3. Test DNS resolution:
```bash
nslookup google.com
```

---

## 5️⃣ File Not Found Error

### Issue:
```
File not found.
Invalid target.
```

### Solution:

Verify correct file paths:

```bash
ls -lh
ls -lh samples/
```

Ensure you are inside:

```bash
cd ~/malware_lab
```

---

## 6️⃣ JSON Report Not Generated

### Issue:
Reports folder missing or report not saved.

### Cause:
Directory does not exist.

### Solution:

Create reports directory manually:

```bash
mkdir -p reports
```

Re-run the scanner.

---

## 7️⃣ Integrated Scanner Import Error

### Issue:
```
ModuleNotFoundError: No module named 'attachment_scanner'
```

### Cause:
Running script from wrong directory.

### Solution:

Run from inside `malware_lab` directory:

```bash
cd ~/malware_lab
python3 integrated_scanner.py sample_email.txt samples/
```

---

## 8️⃣ Incorrect MIME Detection

### Issue:
File extension does not match MIME type.

### Explanation:
This may indicate:
- Disguised executable
- Corrupted file
- Incorrect file signature

### Recommended Action:
Treat mismatched MIME types as suspicious and increase risk scoring.

---

## 9️⃣ Excessive False Positives

### Cause:
Small files or simple scripts may trigger low risk warnings.

### Solution:
Adjust scoring thresholds inside:

- `attachment_scanner.py`
- `url_analyzer.py`

Modify risk scoring logic if needed.

---

## 🔐 Security Best Practices

- Never open suspicious attachments directly.
- Always verify file hashes before execution.
- Avoid clicking IP-based URLs.
- Treat double extensions as HIGH risk.
- Combine attachment and URL analysis for better detection accuracy.
- Validate network connectivity before large-scale URL scanning.

---

## ✅ Validation Checklist

Before submission, verify:

- [ ] Attachment scanner runs successfully
- [ ] URL analyzer fetches content correctly
- [ ] Integrated scanner generates overall report
- [ ] JSON reports saved inside `/reports`
- [ ] No import or permission errors
- [ ] Risk scoring matches expected outputs

---

### Final Recommendation

In real-world environments, enhance this lab implementation with:

- VirusTotal API integration
- WHOIS domain age analysis
- TLS certificate inspection
- Sandbox execution engines
- Threat intelligence feed integration
- SIEM logging integration
