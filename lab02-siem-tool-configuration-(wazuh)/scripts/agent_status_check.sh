#!/bin/bash
# ============================================================
# Script: agent_status_check.sh
# Purpose: Check Wazuh agent status and statistics
# ============================================================

echo "======================================"
echo " Wazuh Agent Status"
echo "======================================"

sudo /var/ossec/bin/agent_control -l
echo ""
sudo /var/ossec/bin/agent_control -s
