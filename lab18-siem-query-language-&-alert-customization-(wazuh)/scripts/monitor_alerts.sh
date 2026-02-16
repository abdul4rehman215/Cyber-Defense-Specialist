#!/bin/bash

ALERT_LOG="/var/ossec/logs/alerts/alerts.log"
CUSTOM_ALERT_LOG="/tmp/custom_alerts.log"

echo "Monitoring custom alerts... (Press Ctrl+C to stop)"
echo "Custom alerts will be logged to: $CUSTOM_ALERT_LOG"

tail -f "$ALERT_LOG" | while read line; do
    if echo "$line" | grep -E "(Rule: 100|Rule: 101|Rule: 102)" > /dev/null; then
        echo "$(date): $line" | tee -a "$CUSTOM_ALERT_LOG"
    fi
done
