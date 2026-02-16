#!/bin/bash

# ================================
# Lab 18 – SIEM Query & Alert Customization
# ================================

# --------------------------------
# Task 1: Start Wazuh Services
# --------------------------------

sudo systemctl status wazuh-manager
sudo systemctl start wazuh-manager
sudo systemctl start wazuh-indexer
sudo systemctl start wazuh-dashboard
sudo systemctl status wazuh-manager

firefox http://localhost:5601 &

# --------------------------------
# Install Required Tools
# --------------------------------

sudo apt install jq -y
sudo apt install bc -y

# --------------------------------
# Task 1: Create Basic Query Files
# --------------------------------

nano queries/failed_login_query.json
nano queries/brute_force_query.json
nano queries/file_access_query.json
nano queries/network_anomaly_query.json
nano queries/optimized_brute_force_query.json

# --------------------------------
# Test Query Execution
# --------------------------------

curl -X POST "localhost:9200/wazuh-alerts-*/_search" \
  -H "Content-Type: application/json" \
  -u admin:admin \
  -d @queries/failed_login_query.json

# --------------------------------
# Create Query Testing Script
# --------------------------------

nano scripts/test_query.sh
chmod +x scripts/test_query.sh

./scripts/test_query.sh queries/failed_login_query.json

# --------------------------------
# Validate Queries
# --------------------------------

nano scripts/validate_query.sh
chmod +x scripts/validate_query.sh

./scripts/validate_query.sh queries/brute_force_query.json
./scripts/validate_query.sh queries/file_access_query.json
./scripts/validate_query.sh queries/network_anomaly_query.json

# --------------------------------
# Test Advanced Queries
# --------------------------------

echo "Testing Brute Force Query..."
./scripts/test_query.sh queries/brute_force_query.json > brute_force_results.json

echo "Testing File Access Query..."
./scripts/test_query.sh queries/file_access_query.json > file_access_results.json

echo "Testing Network Anomaly Query..."
./scripts/test_query.sh queries/network_anomaly_query.json > network_anomaly_results.json

# --------------------------------
# Task 3: Create Custom Rules
# --------------------------------

sudo mkdir -p /var/ossec/etc/rules/custom
sudo chown -R wazuh:wazuh /var/ossec/etc/rules/custom

sudo nano rules/100-custom_auth_rules.xml
sudo nano rules/101-custom_syscheck_rules.xml
sudo nano rules/102-custom_network_rules.xml

sudo cp rules/100-custom_auth_rules.xml /var/ossec/etc/rules/custom/
sudo cp rules/101-custom_syscheck_rules.xml /var/ossec/etc/rules/custom/
sudo cp rules/102-custom_network_rules.xml /var/ossec/etc/rules/custom/

sudo cp /var/ossec/etc/ossec.conf /var/ossec/etc/ossec.conf.backup

sudo sed -i '/<rules>/a\    <include>custom/100-custom_auth_rules.xml</include>' /var/ossec/etc/ossec.conf
sudo sed -i '/<rules>/a\    <include>custom/101-custom_syscheck_rules.xml</include>' /var/ossec/etc/ossec.conf
sudo sed -i '/<rules>/a\    <include>custom/102-custom_network_rules.xml</include>' /var/ossec/etc/ossec.conf

sudo /var/ossec/bin/wazuh-logtest -t
sudo systemctl restart wazuh-manager
sudo systemctl status wazuh-manager

# --------------------------------
# Task 4: Alert Automation Scripts
# --------------------------------

nano scripts/generate_test_events.sh
nano scripts/monitor_alerts.sh
nano scripts/alert_response.sh
nano scripts/process_alerts.sh

chmod +x scripts/generate_test_events.sh
chmod +x scripts/monitor_alerts.sh
chmod +x scripts/alert_response.sh
chmod +x scripts/process_alerts.sh

./scripts/monitor_alerts.sh &
./scripts/process_alerts.sh &

echo "Generating test events..."
./scripts/generate_test_events.sh

sleep 10

cat /tmp/custom_alerts.log
cat /tmp/processed_alerts.log
cat /tmp/blocked_ips.log

kill %1 %2 2>/dev/null

# --------------------------------
# Task 5: Query Performance Benchmark
# --------------------------------

nano scripts/query_performance.sh
chmod +x scripts/query_performance.sh

echo "Testing original brute force query..."
./scripts/query_performance.sh queries/brute_force_query.json

echo "Testing optimized brute force query..."
./scripts/query_performance.sh queries/optimized_brute_force_query.json

# --------------------------------
# Create Optimization Guide
# --------------------------------

nano query_optimization_tips.md

# --------------------------------
# Task 6: Validation Scripts
# --------------------------------

nano scripts/validate_lab_setup.sh
chmod +x scripts/validate_lab_setup.sh
./scripts/validate_lab_setup.sh

nano scripts/final_test_scenario.sh
chmod +x scripts/final_test_scenario.sh
./scripts/final_test_scenario.sh

tail -5 /tmp/custom_alerts.log

# --------------------------------
# End of Lab 18 Commands
# --------------------------------
