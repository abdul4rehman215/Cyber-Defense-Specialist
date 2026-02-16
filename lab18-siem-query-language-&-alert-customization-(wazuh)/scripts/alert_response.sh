#!/bin/bash

RULE_ID=$1
ALERT_LEVEL=$2
SOURCE_IP=$3
DESCRIPTION=$4

case $RULE_ID in
    100001|100003)
        echo "CRITICAL: Authentication attack detected from $SOURCE_IP"
        echo "Action: Blocking IP address"
        # In production, implement actual firewall block
        echo "iptables -A INPUT -s $SOURCE_IP -j DROP" >> /tmp/blocked_ips.log
        ;;
    101001)
        echo "CRITICAL: Critical file modification detected"
        echo "Action: Creating backup and alerting administrator"
        echo "$(date): Critical file alert - $DESCRIPTION" >> /tmp/critical_file_alerts.log
        ;;
    102001|102002)
        echo "WARNING: Network anomaly detected from $SOURCE_IP"
        echo "Action: Increasing monitoring for this IP"
        echo "$(date): Network alert - $DESCRIPTION" >> /tmp/network_alerts.log
        ;;
    *)
        echo "INFO: Custom alert triggered - Rule ID: $RULE_ID"
        ;;
esac
