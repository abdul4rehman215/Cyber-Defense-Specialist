# 🛠️ Troubleshooting – Lab 01: SOC Mission & Workflow Fundamentals

This document captures common issues encountered during the lab and the steps taken to diagnose and resolve them. These scenarios reflect realistic problems faced in SOC and SIEM deployments.

---

## Issue 1: Elasticsearch Service Fails to Start

### Symptoms
- Elasticsearch service does not start
- `systemctl status elasticsearch` shows failed state
- Connection to `localhost:9200` fails

### Diagnosis
- Verify Java installation
- Check Elasticsearch service logs

### Commands Used
```bash
java -version
sudo systemctl status elasticsearch
sudo journalctl -u elasticsearch -f
````

### Resolution

* Ensure OpenJDK 11 is installed and active
* Restart the Elasticsearch service after fixing configuration issues

```bash
sudo systemctl restart elasticsearch
```

---

## Issue 2: Kibana Not Accessible on Port 5601

### Symptoms

* Unable to access Kibana via browser
* Connection timeout on port 5601

### Diagnosis

* Check Kibana service status
* Verify server host configuration

### Commands Used

```bash
sudo systemctl status kibana
sudo grep server.host /etc/kibana/kibana.yml
```

### Resolution

* Set `server.host` to `0.0.0.0` or `localhost`
* Restart Kibana service

```bash
sudo systemctl restart kibana
```

---

## Issue 3: No Logs Appearing in Elasticsearch

### Symptoms

* `soc-logs-*` index not created
* Kibana Discover shows no data

### Diagnosis

* Verify Logstash service status
* Inspect Logstash pipeline configuration
* Review Logstash logs

### Commands Used

```bash
sudo systemctl status logstash
sudo journalctl -u logstash -f
```

### Resolution

* Correct Grok patterns if parsing fails
* Restart Logstash after configuration updates

```bash
sudo systemctl restart logstash
```

---

## Issue 4: Elasticsearch Indices Exist but No Search Results

### Symptoms

* Indices are present
* Search queries return empty results

### Diagnosis

* Confirm events are being generated
* Verify time range in queries and Kibana

### Commands Used

```bash
curl -X GET "localhost:9200/_cat/indices?v"
curl -X GET "localhost:9200/soc-logs-*/_search?pretty"
```

### Resolution

* Re-run event generation script
* Adjust time filters in Kibana Discover

```bash
~/soc-lab/scripts/generate-events.sh
```

---

## Issue 5: ElastAlert Not Running or Not Triggering Alerts

### Symptoms

* No alerts generated
* ElastAlert process not running
* Empty ElastAlert logs

### Diagnosis

* Check if ElastAlert process is running
* Review ElastAlert configuration and logs

### Commands Used

```bash
pgrep -f elastalert
tail -f /var/log/elastalert/elastalert.log
```

### Resolution

* Start ElastAlert manually if not running
* Ensure Elasticsearch connection details are correct

```bash
nohup elastalert --config /etc/elastalert/config.yaml --verbose \
> /var/log/elastalert/elastalert.log 2>&1 &
```

---

## Issue 6: SOC Dashboard Script Displays Incomplete Data

### Symptoms

* Dashboard shows missing services
* No recent events displayed

### Diagnosis

* Verify SIEM services are active
* Confirm log files exist and contain events

### Commands Used

```bash
systemctl is-active elasticsearch
systemctl is-active kibana
systemctl is-active logstash
ls -l /var/log/auth.log /var/log/syslog
```

### Resolution

* Restart inactive services
* Regenerate sample security events

```bash
sudo systemctl restart elasticsearch kibana logstash
~/soc-lab/scripts/generate-events.sh
```

---

## Issue 7: Permission Denied When Running Scripts

### Symptoms

* Script execution fails with permission denied error

### Diagnosis

* Check file permissions

### Commands Used

```bash
ls -l ~/soc-lab/scripts/
```

### Resolution

* Make scripts executable

```bash
chmod +x ~/soc-lab/scripts/*.sh
```

---

## Summary

Most issues encountered in this lab were related to:

* Service startup order
* Configuration file changes not followed by restarts
* Log ingestion delays
* Alerting service not running in background

These troubleshooting steps mirror real-world SOC challenges and reinforce the importance of monitoring service health, validating configurations, and verifying end-to-end data flow.
