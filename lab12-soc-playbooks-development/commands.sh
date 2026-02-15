#!/bin/bash

# ==========================================
# Lab 12: SOC Playbooks Development
# All Commands Executed During Lab
# ==========================================

# ---- Create Project Structure ----
mkdir -p ~/soc_playbooks/{scripts,logs,config,evidence}
cd ~/soc_playbooks
mkdir -p logs/{incidents,alerts,reports}

# ---- Verify Structure ----
tree -L 2

# ---- Make Scripts Executable ----
chmod +x scripts/base_playbook.py
chmod +x scripts/malware_detection.py
chmod +x scripts/network_intrusion.py
chmod +x scripts/system_isolation.py
chmod +x scripts/*.py

# ---- Run Malware Detection Playbook ----
python3 scripts/malware_detection.py

# ---- Run Network Intrusion Playbook ----
python3 scripts/network_intrusion.py

# ---- Run System Isolation Playbook ----
python3 scripts/system_isolation.py

# ---- Verify Generated Logs and Reports ----
ls -R logs/

# ---- Manual Testing Commands (if needed) ----
ps aux
netstat -tuln
netstat -tun
last -n 50
env
lsmod

# ---- iptables Commands Used Internally ----
sudo iptables-save > logs/incidents/iptables_backup.rules
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
sudo iptables -A INPUT -s <malicious_ip> -j DROP
sudo iptables-restore < logs/incidents/iptables_backup.rules

# ---- Service Management Commands ----
sudo systemctl stop apache2
sudo systemctl stop nginx
sudo systemctl stop mysql
