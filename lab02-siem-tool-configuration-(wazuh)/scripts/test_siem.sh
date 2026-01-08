#!/bin/bash
# ============================================================
# Script: test_siem.sh
# Lab: SIEM Tool Configuration (Wazuh)
# Purpose: Generate comprehensive security events
# ============================================================

echo "======================================"
echo " Running Comprehensive SIEM Test"
echo "======================================"

# ------------------------------------------------------------
# Authentication Failure Events
# ------------------------------------------------------------
echo "[+] Generating failed authentication attempts..."

for i in {1..3}; do
  echo "wrong_password" | su - testuser 2>/dev/null || true
  sleep 1
done

# ------------------------------------------------------------
# File Integrity Monitoring Events
# ------------------------------------------------------------
echo "[+] Generating file integrity events..."

sudo touch /etc/critical_file_$(date +%s)
echo "test modification" | sudo tee /etc/test_config_change > /dev/null

# Restore permissions after intentional misconfiguration
sudo chmod 777 /etc/passwd 2>/dev/null || true
sudo chmod 644 /etc/passwd

# ------------------------------------------------------------
# Network Activity Events
# ------------------------------------------------------------
echo "[+] Generating network activity..."

curl -s http://httpbin.org/ip > /dev/null
ping -c 3 8.8.8.8 > /dev/null

# ------------------------------------------------------------
# Port Scan Simulation
# ------------------------------------------------------------
echo "[+] Simulating port scanning activity..."

nmap -sS 127.0.0.1 -p 22,80,443 > /dev/null 2>&1 || true

echo "======================================"
echo " SIEM test events generated successfully"
echo " Check Wazuh dashboard for alerts"
echo "======================================"
