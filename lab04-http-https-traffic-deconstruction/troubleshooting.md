# 🛠️ Troubleshooting – Lab 4: HTTP/HTTPS Traffic Deconstruction

---

## Issue 1: Permission Denied When Running tcpdump

### Symptoms
- tcpdump: You don't have permission to capture on that device
- Operation not permitted

### Cause
Packet capture requires elevated privileges or proper group permissions.

### Solution

Run tcpdump with sudo:
```
sudo tcpdump -i lo -w http_traffic.pcap port 8080
```
OR add user to pcap/wireshark group (if configured):
```
sudo usermod -a -G wireshark $USER
newgrp wireshark
```
Verify:
```
id
```
---

## Issue 2: No Traffic Captured in PCAP File

### Symptoms
- PCAP file exists but is empty
- File size remains 0 KB

### Possible Causes
- Wrong interface selected
- No traffic generated during capture
- Capture stopped too early

### Solution

Check active interfaces:
```
ip addr
```
Verify loopback interface is used for local server:
```
sudo tcpdump -i lo
```
Ensure traffic is generated during capture:
```
curl http://localhost:8080/
```
---

## Issue 3: HTTP Server Port Already in Use

### Symptoms
- OSError: [Errno 98] Address already in use

### Cause
Another process is already listening on port 8080.

### Solution

Check which process is using the port:
```
sudo lsof -i :8080
```
Kill the process:
```
kill <PID>
```

Or use a different port:

```
python3 -m http.server 9090
```
---

## Issue 4: Python Script Not Executing

### Symptoms
- `Permission denied`
- `command not found`
- `ModuleNotFoundError`

### Causes
- Script not executable
- Wrong shebang line
- Python not installed

### Solution

Ensure Python 3 is installed:

```
python3 --version
```

Make script executable:

```
chmod +x script_name.py
```

Verify shebang line:

```
#!/usr/bin/env python3
```

Run directly:

```
python3 script_name.py
```

---

## Issue 5: HTTP Parser Not Detecting Anomalies

### Symptoms
- Parser runs but no anomalies reported

### Causes
- Incorrect input file format
- HTTP requests not separated properly
- Suspicious payload not matching regex patterns

### Solution

Verify input file:
```
cat test_requests.txt
```

Ensure requests follow HTTP format:

```
GET /path HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
```

Test regex patterns manually:
```
grep -i "script" test_requests.txt
```

---

## Issue 6: OpenSSL Certificate Retrieval Fails

### Symptoms
- `Connection refused`
- `Handshake failure`
- No certificate output

### Causes
- Network connectivity issue
- Firewall blocking outbound HTTPS
- Incorrect hostname

### Solution
Test connectivity:

```
ping www.google.com
```

Test HTTPS manually:

```
curl https://www.google.com
```

Retry OpenSSL command:

```
openssl s_client -connect www.google.com:443
 -servername www.google.com
```

---

## Issue 7: TLS Version or Cipher Not Displayed

### Symptoms
- TLS version not shown
- Cipher output empty

### Cause
Host may enforce strict TLS settings or block negotiation.

### Solution

Use verbose OpenSSL:
```
openssl s_client -connect www.google.com:443
 -tls1_2
```

Or:
```
openssl s_client -connect www.google.com:443
 -tls1_3
```

---

## Issue 8: Monitoring Script Produces Empty Logs

### Symptoms
- `http_alerts.log` empty
- `https_connections.log` empty

### Causes
- No traffic during monitoring window
- Incorrect interface selected
- Monitoring duration too short

### Solution

Increase monitoring duration:

```DURATION=120```

Generate traffic during monitoring:

```
curl http://localhost:8080/../../etc/passwd
```

Verify correct interface:
```
ip route
```
---

## Issue 9: Alerts Not Triggered in alert_system.py

### Symptoms
- Script runs but no alerts generated

### Cause
Threshold values not exceeded in sample data.

### Solution
Verify sample_data values:
```
sample_data = {
'sql_injection': 2,
'xss': 0,
'path_traversal': 1,
'unusual_user_agent': 4
}
```
Ensure thresholds are met:

```
self.alert_threshold = {
'sql_injection': 1,
'xss': 1,
'path_traversal': 1,
'unusual_user_agent': 3
}
```

---

# ✅ Verification Checklist

- ✔ HTTP server running on correct port  
- ✔ tcpdump capturing correct interface  
- ✔ PCAP file contains packet data  
- ✔ HTTP parser executes successfully  
- ✔ TLS certificate retrieved properly  
- ✔ Monitoring logs populated  
- ✔ Alert system generating entries  

---

# 🎯 SOC Perspective

These troubleshooting steps reflect real-world blue team workflow:

- Validate traffic flow
- Verify capture points
- Confirm tool configuration
- Inspect logs
- Confirm detection logic

Proper troubleshooting ensures reliable monitoring and reduces false negatives in production environments.
