#!/bin/bash
# ============================================================
# Script: soc-dashboard.sh
# Purpose: SOC Monitoring Dashboard
# ============================================================

clear
echo "=================================="
echo "        SOC MONITORING DASHBOARD   "
echo "=================================="
echo ""

echo "SYSTEM STATUS:"
echo "--------------"

if systemctl is-active --quiet elasticsearch; then
  echo "- Elasticsearch: active"
else
  echo "- Elasticsearch: inactive"
fi

if systemctl is-active --quiet kibana; then
  echo "- Kibana: active"
else
  echo "- Kibana: inactive"
fi

if systemctl is-active --quiet logstash; then
  echo "- Logstash: active"
else
  echo "- Logstash: inactive"
fi

echo ""
echo "RECENT SECURITY EVENTS (Last 10):"
echo "--------------------------------"
grep -E "Failed password|Accepted password|UFW BLOCK" \
/var/log/auth.log /var/log/syslog 2>/dev/null | tail -10

echo ""
echo "ALERT SYSTEM STATUS:"
echo "--------------------"
if pgrep -f elastalert > /dev/null; then
  echo "- ElastAlert: RUNNING"
  alert_count=$(grep -c "Alert" /var/log/elastalert/elastalert.log 2>/dev/null)
  echo "- Recent alerts: $alert_count"
else
  echo "- ElastAlert: NOT RUNNING"
fi

echo ""
echo "ELASTICSEARCH INDICES:"
echo "----------------------"
curl -s "localhost:9200/_cat/indices?v" | grep soc-logs || echo "No SOC indices found"

echo ""
echo "Last Updated: $(date)"
echo "=================================="
