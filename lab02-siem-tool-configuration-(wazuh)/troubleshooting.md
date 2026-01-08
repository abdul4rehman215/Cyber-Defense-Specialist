# 🛠️ Troubleshooting – Lab 02: SIEM Tool Configuration (Wazuh)

This document outlines common issues encountered during the deployment and operation of a Wazuh-based SIEM environment, along with the steps used to diagnose and resolve them.

---

## Issue 1: Wazuh Manager Service Fails to Start

### Symptoms
- `wazuh-manager` service is inactive or failed
- No alerts or logs being processed

### Diagnosis
- Check system resource availability
- Review Wazuh Manager logs

### Commands Used
```bash
free -h
df -h
sudo systemctl status wazuh-manager
sudo journalctl -u wazuh-manager -f
````

### Resolution

* Ensure sufficient RAM and disk space
* Fix configuration issues and restart service

```bash
sudo systemctl restart wazuh-manager
```

---

## Issue 2: Wazuh Agent Not Connecting to Manager

### Symptoms

* Agent status shows disconnected
* No data received from agent

### Diagnosis

* Verify manager IP configuration
* Check agent logs and connectivity

### Commands Used

```bash
sudo grep server /var/ossec/etc/ossec.conf
sudo systemctl status wazuh-agent
sudo netstat -tlnp | grep 1514
```

### Resolution

* Correct server IP in `ossec.conf`
* Restart agent service

```bash
sudo systemctl restart wazuh-agent
```

---

## Issue 3: Elasticsearch Service Not Starting

### Symptoms

* Elasticsearch fails to start
* SIEM dashboards not loading data

### Diagnosis

* Check Java installation
* Review Elasticsearch logs

### Commands Used

```bash
java -version
sudo systemctl status elasticsearch
sudo journalctl -u elasticsearch -f
```

### Resolution

* Ensure OpenJDK 11 is installed
* Fix YAML syntax errors in configuration

```bash
sudo systemctl restart elasticsearch
```

---

## Issue 4: Kibana Not Accessible on Port 5601

### Symptoms

* Browser connection refused or timeout
* Kibana dashboard does not load

### Diagnosis

* Check Kibana service status
* Verify port listening

### Commands Used

```bash
sudo systemctl status kibana
sudo netstat -tlnp | grep 5601
sudo journalctl -u kibana -f
```

### Resolution

* Correct `kibana.yml` configuration
* Restart Kibana service

```bash
sudo systemctl restart kibana
```

---

## Issue 5: No Alerts Visible in Wazuh Dashboard

### Symptoms

* Logs collected but no alerts triggered
* Dashboard appears empty

### Diagnosis

* Verify rule loading
* Check alert logs

### Commands Used

```bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
sudo tail -f /var/ossec/logs/ossec.log
```

### Resolution

* Reload rules and restart manager
* Generate new test events

```bash
sudo systemctl restart wazuh-manager
```

---

## Issue 6: Custom Rules Not Triggering

### Symptoms

* Test events generated but custom rules not firing

### Diagnosis

* Validate rule syntax
* Check rule IDs and severity levels

### Commands Used

```bash
sudo cat /var/ossec/etc/rules/local_rules.xml
```

### Resolution

* Fix XML syntax or rule conditions
* Restart Wazuh Manager

```bash
sudo systemctl restart wazuh-manager
```

---

## Issue 7: File Integrity Monitoring Not Detecting Changes

### Symptoms

* File changes not generating alerts

### Diagnosis

* Check monitored directories
* Verify syscheck configuration

### Commands Used

```bash
sudo grep syscheck /var/ossec/etc/ossec.conf
```

### Resolution

* Ensure directories are listed and enabled
* Restart Wazuh services

```bash
sudo systemctl restart wazuh-manager
sudo systemctl restart wazuh-agent
```

---

## Issue 8: Active Response Not Executing

### Symptoms

* Alerts generated but no automated response
* IPs not blocked

### Diagnosis

* Verify active response configuration
* Check active response logs

### Commands Used

```bash
sudo grep active-response /var/ossec/etc/ossec.conf
sudo tail -f /var/ossec/logs/ossec.log
```

### Resolution

* Enable active response and verify rule IDs
* Restart Wazuh Manager

```bash
sudo systemctl restart wazuh-manager
```

---

## Summary

Most issues encountered during this lab were related to:

* Service startup dependencies
* Configuration syntax errors
* Rule loading and alert thresholds
* Resource availability

Troubleshooting these issues reinforces real-world SOC skills such as service monitoring, log analysis, and incident diagnosis.
