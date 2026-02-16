# 🛠 Troubleshooting Guide - Lab 20 – Detect, Respond, and Recover

---

# 1️⃣ Wazuh Service Issues

## Issue: Wazuh Manager Not Starting

### Symptoms
- `systemctl status wazuh-manager` shows failed
- No alerts generated
- No logs updating in `/var/ossec/logs/`

### Troubleshooting Steps

```bash
sudo systemctl status wazuh-manager
sudo journalctl -u wazuh-manager -xe
sudo tail -f /var/ossec/logs/ossec.log
```

### Solutions

- Verify configuration syntax:
```bash
sudo /var/ossec/bin/ossec-control status
```

- Restart service:
```bash
sudo systemctl restart wazuh-manager
```

- Ensure rules are valid:
```bash
sudo /var/ossec/bin/wazuh-logtest -t
```

---

# 2️⃣ No Alerts Generated

## Symptoms
- SSH brute force simulation ran
- No entries in alerts.json
- Analyzer reports zero high priority alerts

### Possible Causes

- Wazuh not monitoring correct log file
- Log file permissions incorrect
- Attack simulation failed

### Troubleshooting

```bash
sudo tail -f /var/log/auth.log
sudo tail -f /var/ossec/logs/alerts/alerts.json
```

Verify Wazuh configuration includes:

```xml
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/auth.log</location>
</localfile>
```

Wait 2–3 minutes for log processing after simulation.

---

# 3️⃣ Zeek Not Capturing Traffic

## Symptoms
- conn.log not updating
- Zeek analyzer shows no port scanners
- No large transfer detection

### Troubleshooting Steps

Check interface:

```bash
ip link show
```

Verify Zeek running:

```bash
ps aux | grep zeek
```

Check Zeek logs:

```bash
ls -lh /opt/zeek/logs/current/
```

Run manual capture:

```bash
sudo tcpdump -i lo
```

### Common Fixes

- Ensure correct interface configured
- Restart Zeek:
```bash
sudo systemctl restart zeek
```
- Confirm `/opt/zeek/bin` is in PATH

---

# 4️⃣ Python Script Errors

## Issue: Module Not Found

### Solution

Check Python version:

```bash
python3 --version
```

Install missing dependencies:

```bash
pip3 install pandas requests
```

Verify permissions:

```bash
ls -l ~/soc-lab/scripts/
chmod +x script_name.py
```

---

## Issue: JSON Decode Errors

### Cause
Corrupted or incomplete alert lines in alerts.json.

### Fix
Skip malformed lines (already implemented in analyzer).

Check file manually:

```bash
head -20 /var/ossec/logs/alerts/alerts.json
```

---

# 5️⃣ iptables Blocking Issues

## Issue: IP Not Blocked

### Check Rules

```bash
sudo iptables -L -n -v
```

### Verify Rule Exists

```bash
sudo iptables -L -n | grep <IP_ADDRESS>
```

### Restore Firewall If Needed

```bash
sudo iptables-save > backup.txt
sudo iptables-restore < backup.txt
```

---

# 6️⃣ Evidence Collection Failures

## Issue: Evidence Directory Missing

### Fix

```bash
mkdir -p ~/soc-lab/evidence
```

---

## Issue: Permission Denied Copying Logs

Use sudo:

```bash
sudo cp /var/ossec/logs/alerts/alerts.json ~/soc-lab/evidence/
```

---

# 7️⃣ Rootcheck / Syscheck Errors

## Rootcheck Not Running

```bash
sudo /var/ossec/bin/rootcheck
```

If permission denied:

```bash
sudo chmod +x /var/ossec/bin/rootcheck
```

---

## Syscheck Not Running

```bash
sudo /var/ossec/bin/syscheck
```

If configuration error:

```bash
sudo nano /var/ossec/etc/ossec.conf
```

Validate XML syntax carefully.

---

# 8️⃣ No Suspicious Connections Found

## Possible Causes

- Simulation did not run properly
- Logs cleared
- Monitoring delay

Re-run simulations:

```bash
./ssh_bruteforce.sh
./port_scan.sh
sleep 180
```

Then re-run analyzers.

---

# 9️⃣ Firewall Blocks Localhost Accidentally

Blocking `127.0.0.1` can break local services.

### Remove Rule

```bash
sudo iptables -D INPUT -s 127.0.0.1 -j DROP
```

Always validate firewall rules carefully in production.

---

# 🔟 Log File Not Found

Verify existence:

```bash
ls -lh /var/ossec/logs/
ls -lh /opt/zeek/logs/current/
```

Ensure services are running before expecting logs.

---

# 🧠 Best Practices Learned

- Always verify monitoring tools are running
- Validate configurations before restarting services
- Archive firewall rules before modifying
- Never block localhost in production environments
- Collect evidence before remediation
- Always verify recovery steps

---

# ✅ Final Verification Checklist

Before declaring incident closed:

```bash
sudo /var/ossec/bin/agent_control -l
netstat -tuln | grep ESTABLISHED
sudo iptables -L -n -v
ps aux | grep -Ei 'suspicious|malware|backdoor'
```

All checks should confirm:

✔ No active malicious connections  
✔ Firewall rules applied correctly  
✔ Monitoring services running  
✔ No unauthorized system changes  

---

# 🏁 Final Note

This lab simulated a complete SOC workflow.  
If issues occur, troubleshoot layer-by-layer:

1. Service Layer (Wazuh / Zeek)
2. Log Layer
3. Detection Script Layer
4. Response Layer
5. Verification Layer

Systematic troubleshooting ensures faster incident resolution and better operational stability.
