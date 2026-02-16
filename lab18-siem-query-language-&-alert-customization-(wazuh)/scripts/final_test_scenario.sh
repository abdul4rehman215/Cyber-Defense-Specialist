#!/bin/bash

echo "=== Final Test Scenario for Lab 18 ==="
echo

# Scenario 1: Brute Force Simulation
echo "Scenario 1: Simulating brute force attack..."
for i in {1..10}; do
    logger -p auth.info "sshd[$(($RANDOM + 1000))]: Failed password for admin from 10.0.0.50 port 22 ssh2"
    sleep 0.5
done
echo "   ✓ Brute force simulation complete"

# Scenario 2: Critical File Access
echo
echo "Scenario 2: Simulating critical file access..."
sudo touch /etc/test_passwd_access
sudo rm /etc/test_passwd_access
echo "   ✓ Critical file access simulation complete"

# Scenario 3: Query Test
echo
echo "Scenario 3: Testing brute force query..."

if [ -f /tmp/brute_force_query.json ]; then
    RESULT=$(curl -s -X POST "localhost:9200/wazuh-alerts-*/_search" \
      -H "Content-Type: application/json" \
      -u admin:admin \
      -d @/tmp/brute_force_query.json)

    HITS=$(echo "$RESULT" | jq -r '.hits.total.value // 0')
    echo "   ✓ Brute force query returned $HITS hits"
else
    echo "   ✗ Query file not found"
fi

# Scenario 4: Alert Check
echo
echo "Scenario 4: Checking recent alerts..."
sleep 5

if [ -f /var/ossec/logs/alerts/alerts.log ]; then
    RECENT=$(tail -20 /var/ossec/logs/alerts/alerts.log | grep -c "Rule:")
    echo "   ✓ Found $RECENT recent alerts"
else
    echo "   ✗ Alert log not found"
fi

echo
echo "=== Final Test Completed ==="
echo "Check:"
echo " - /tmp/custom_alerts.log"
echo " - /tmp/processed_alerts.log"
