#!/bin/bash

ALERT_LOG="/var/ossec/logs/alerts/alerts.log"
PROCESSED_ALERTS="/tmp/processed_alerts.log"

process_alert() {
    local alert_line="$1"

    # Extract rule ID
    RULE_ID=$(echo "$alert_line" | grep -oP 'Rule: \K\d+')

    # Extract alert level
    ALERT_LEVEL=$(echo "$alert_line" | grep -oP 'Level: \K\d+')

    # Extract source IP
    SOURCE_IP=$(echo "$alert_line" | grep -oP 'srcip: \K[0-9.]+' || echo "N/A")

    # Extract description
    DESCRIPTION=$(echo "$alert_line" | grep -oP 'Description: \K.*' || echo "No description")

    if [[ $RULE_ID =~ ^(100|101|102) ]]; then
        echo "Processing custom alert: Rule $RULE_ID, Level $ALERT_LEVEL"
        /tmp/alert_response.sh "$RULE_ID" "$ALERT_LEVEL" "$SOURCE_IP" "$DESCRIPTION"
        echo "$(date): Processed Rule $RULE_ID - $DESCRIPTION" >> "$PROCESSED_ALERTS"
    fi
}

echo "Starting automated alert processing..."

tail -f "$ALERT_LOG" | while read line; do
    if echo "$line" | grep -E "Rule: (100|101|102)" > /dev/null; then
        process_alert "$line"
    fi
done
