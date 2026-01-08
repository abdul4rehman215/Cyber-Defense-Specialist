#!/bin/bash
# ============================================================
# Script: realtime_alert_monitor.sh
# Purpose: Monitor Wazuh alerts in real-time
# ============================================================

echo "======================================"
echo " Real-Time Wazuh Alert Monitor"
echo "======================================"
echo " Press CTRL+C to exit"
echo ""

sudo tail -f /var/ossec/logs/alerts/alerts.log
