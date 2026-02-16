# 🛠 Troubleshooting – Lab 18 - Lab 18 – SIEM Query Language & Alert Customization (Wazuh)

---

## Issue 1: Wazuh Services Not Starting

Check status:
```
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-indexer
```

Check logs:
```
sudo tail -f /var/ossec/logs/ossec.log
sudo journalctl -u wazuh-manager -f
```

Restart:
```
sudo systemctl restart wazuh-manager
```

---

## Issue 2: Query Execution Failures

Check cluster health:
```
curl -X GET "localhost:9200/_cluster/health" -u admin:admin
```

Check indices:
```
curl -X GET "localhost:9200/_cat/indices/wazuh-*" -u admin:admin
```

---

## Issue 3: Custom Rules Not Loading

Validate rules:
```
sudo /var/ossec/bin/wazuh-logtest -t
```

Check config:
```
sudo /var/ossec/bin/wazuh-control info
```

Restart manager after rule changes.

---

## Issue 4: No Alerts Generated

Check alert log:
```
sudo tail -f /var/ossec/logs/alerts/alerts.log
```

Test rule matching:
```
echo "test log entry" | sudo /var/ossec/bin/wazuh-logtest
```

---

## Issue 5: Query Performance Slow

Recommendations:
- Use filter instead of must
- Limit time range
- Use .keyword fields
- Use size: 0 for aggregations
- Avoid wildcard-heavy queries

---

## Issue 6: jq JSON Validation Fails

Check JSON syntax:
```
jq empty query.json
```

Fix missing commas, brackets, or invalid characters.

---

## Issue 7: Background Scripts Not Working

Ensure executable permissions:
```
chmod +x script.sh
```

Check process:
```
ps aux | grep script_name
```

Kill background jobs if stuck:
```
kill <PID>
```
