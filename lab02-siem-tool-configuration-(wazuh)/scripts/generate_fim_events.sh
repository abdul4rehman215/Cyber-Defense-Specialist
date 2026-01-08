#!/bin/bash
# ============================================================
# Script: generate_fim_events.sh
# Purpose: Trigger File Integrity Monitoring alerts
# ============================================================

echo "[+] Generating file integrity events..."

sudo touch /etc/fim_test_file_$(date +%s)
echo "unauthorized change" | sudo tee /etc/fim_modified_file > /dev/null

echo "[+] File integrity monitoring events generated"
