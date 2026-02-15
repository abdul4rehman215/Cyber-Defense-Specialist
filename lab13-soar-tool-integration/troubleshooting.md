# 🛠 Troubleshooting Guide – Lab 13: SOAR Tool Integration

---

## 1. Docker Containers Not Starting

### Symptoms
- `docker compose up -d` fails
- Containers exit immediately
- `docker compose ps` shows "Exited"

### Solutions
- Check disk space:
```
df -h
```
- Verify Docker service:
```
sudo systemctl status docker
```
- Restart Docker:
```
sudo systemctl restart docker
```
- Inspect logs:
```
docker compose logs
```
```
docker compose logs wazuh-manager
```
```
docker compose logs thehive
```
```
docker compose logs cortex
```
---

## 2. Wazuh Authentication Failure

### Symptoms
- WazuhConnector.authenticate() returns False
- main.py exits with "Wazuh authentication failed"

### Solutions
- Ensure Wazuh is fully initialized (wait 5–10 minutes after deployment)
- Verify credentials in config.yaml
- Test API manually:
```
curl -k -u wazuh:wazuh https://localhost:55000/security/user/authenticate
```
- Check if port 55000 is listening:
```
sudo netstat -tulnp | grep 55000
```
---

## 3. TheHive Login Failure

### Symptoms
- TheHiveConnector.login() returns False
- Case creation fails

### Solutions
- Confirm TheHive UI is accessible:
```
http://localhost:9000
```
- Verify credentials in config.yaml
- Check TheHive container logs:
```
docker compose logs thehive
```
- Ensure Elasticsearch is running:
```
docker compose ps
```
---

## 4. Alerts Not Being Retrieved

### Symptoms
- No cases created
- Orchestrator running but no activity

### Solutions
- Verify min_alert_level in config.yaml
- Lower threshold temporarily to test:
  `min_alert_level: 3`

- Test Wazuh alert API manually:
```
curl -k -H "Authorization: Bearer <TOKEN>" https://localhost:55000/alerts
```
- Confirm Wazuh is generating alerts in dashboard

---

## 5. Playbooks Not Executing

### Symptoms
- Alert pulled but no playbook triggered
- No case created in TheHive

### Solutions
- Verify rule IDs in config.yaml match actual Wazuh rule IDs
- Print alert rule ID inside orchestrator for debugging
- Check logs:
```
tail -f logs/soar_integration.log
```
---

## 6. TheHive Case Creation Fails

### Symptoms
- Case ID is None
- No case visible in dashboard

### Solutions
- Verify session authentication is valid
- Confirm correct API endpoint:
```
/api/case
```
- Check TheHive logs:
```
docker compose logs thehive
```
- Ensure Elasticsearch container is healthy

---

## 7. iptables Command Failures

### Symptoms
- Playbook returns FAILED during IP blocking

### Solutions
- Run scripts with sudo
- Verify iptables exists:
```
which iptables
```
- Check firewall rules:
```
sudo iptables -L
```
⚠ In cloud environments, iptables may be restricted.

---

## 8. ClamAV Scan Fails in Malware Playbook

### Symptoms
- scan_system() returns error

### Solutions
- Install ClamAV:
```
sudo apt install clamav -y
```
- Update signatures:
```
sudo freshclam
```
- Verify command works:
```
clamscan -r /tmp
```
---

## 9. YAML Configuration Errors

### Symptoms
- "Configuration error: Missing section"

### Solutions
- Validate YAML syntax:
```
python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

- Ensure indentation uses spaces (not tabs)
- Verify required sections:
`wazuh
thehive
playbooks
logging`

---

## 10. Integration Tests Failing

### Symptoms
- unittest returns FAILED

### Solutions
- Ensure services are running before tests
- Confirm ports:
- `55000 (Wazuh API)`
- `9000 (TheHive)`
- `9001 (Cortex)`

- Restart stack if needed:
```
docker compose down
docker compose up -d
```

---

# 🔎 Debugging Best Practices

- Always verify container health first
- Test APIs manually before automation
- Use logging to trace failures
- Validate configuration files
- Run playbooks independently for testing

---

# 🧪 Final Validation Checklist

✔ Docker services running  
✔ Wazuh dashboard accessible  
✔ TheHive dashboard accessible  
✔ Cortex accessible  
✔ API authentication successful  
✔ Alerts retrieved from Wazuh  
✔ Playbooks triggered  
✔ Cases created in TheHive  
✔ Observables added  
✔ Logs generated  


Proper troubleshooting ensures stable and reliable SOAR automation before production deployment.
