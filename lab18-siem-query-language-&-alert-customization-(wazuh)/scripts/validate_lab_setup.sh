#!/bin/bash

echo "=== Lab 18 Validation Script ==="
echo

# Test 1: Check Wazuh services
echo "1. Checking Wazuh services..."

if systemctl is-active --quiet wazuh-manager; then
    echo "   ✓ Wazuh Manager is running"
else
    echo "   ✗ Wazuh Manager is not running"
fi

if systemctl is-active --quiet wazuh-indexer; then
    echo "   ✓ Wazuh Indexer is running"
else
    echo "   ✗ Wazuh Indexer is not running"
fi

if systemctl is-active --quiet wazuh-dashboard; then
    echo "   ✓ Wazuh Dashboard is running"
else
    echo "   ✗ Wazuh Dashboard is not running"
fi

# Test 2: Validate custom rules
echo
echo "2. Validating custom rules..."

RULES_DIR="/var/ossec/etc/rules/custom"

if [ -f "$RULES_DIR/100-custom_auth_rules.xml" ]; then
    echo "   ✓ Authentication rules created"
else
    echo "   ✗ Authentication rules missing"
fi

if [ -f "$RULES_DIR/101-custom_syscheck_rules.xml" ]; then
    echo "   ✓ Syscheck rules created"
else
    echo "   ✗ Syscheck rules missing"
fi

if [ -f "$RULES_DIR/102-custom_network_rules.xml" ]; then
    echo "   ✓ Network rules created"
else
    echo "   ✗ Network rules missing"
fi

# Test 3: Elasticsearch connectivity
echo
echo "3. Testing Elasticsearch connectivity..."

if curl -s -X GET "localhost:9200/_cluster/health" -u admin:admin | grep -q "green\|yellow"; then
    echo "   ✓ Elasticsearch cluster is accessible"
else
    echo "   ✗ Elasticsearch cluster is not accessible"
fi

# Test 4: Script executables
echo
echo "4. Validating created scripts..."

SCRIPTS=(
"/tmp/test_query.sh"
"/tmp/validate_query.sh"
"/tmp/generate_test_events.sh"
"/tmp/monitor_alerts.sh"
"/tmp/process_alerts.sh"
"/tmp/query_performance.sh"
)

for script in "${SCRIPTS[@]}"; do
    if [ -x "$script" ]; then
        echo "   ✓ $(basename $script) is executable"
    else
        echo "   ✗ $(basename $script) missing or not executable"
    fi
done

echo
echo "=== Validation Complete ==="
