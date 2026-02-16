#!/bin/bash

############################################################
# LAB 20 – Detect, Respond, and Recover
# Complete Command Execution Log
############################################################


###############################
# TASK 1 – SYSTEM PREPARATION
###############################

sudo apt update && sudo apt upgrade -y

sudo apt install -y curl wget gnupg python3 python3-pip git libpcap-dev net-tools sshpass

pip3 install pandas requests

mkdir -p ~/soc-lab/{logs,scripts,reports,evidence,attack-simulation}
cd ~/soc-lab


###############################
# INSTALL WAZUH MANAGER
###############################

curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | sudo gpg --dearmor -o /usr/share/keyrings/wazuh.gpg

echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list

sudo apt update
sudo apt install -y wazuh-manager

sudo systemctl enable wazuh-manager
sudo systemctl start wazuh-manager
sudo systemctl status wazuh-manager


###############################
# CONFIGURE LOG MONITORING
###############################

sudo cp /var/ossec/etc/ossec.conf /var/ossec/etc/ossec.conf.backup
sudo systemctl restart wazuh-manager

sudo nano /var/ossec/etc/rules/local_rules.xml
sudo systemctl restart wazuh-manager
sudo tail -5 /var/ossec/logs/ossec.log


###############################
# INSTALL ZEEK
###############################

sudo apt update
sudo apt install -y zeek zeek-aux

echo 'export PATH=/opt/zeek/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

zeek --version


###############################
# TASK 2 – CREATE PYTHON ANALYZERS
###############################

nano ~/soc-lab/scripts/wazuh_analyzer.py
chmod +x ~/soc-lab/scripts/wazuh_analyzer.py

nano ~/soc-lab/scripts/zeek_analyzer.py
chmod +x ~/soc-lab/scripts/zeek_analyzer.py

nano ~/soc-lab/scripts/incident_response.py
chmod +x ~/soc-lab/scripts/incident_response.py


###############################
# TASK 3 – ATTACK SIMULATION
###############################

nano ~/soc-lab/attack-simulation/ssh_bruteforce.sh
chmod +x ~/soc-lab/attack-simulation/ssh_bruteforce.sh

nano ~/soc-lab/attack-simulation/port_scan.sh
chmod +x ~/soc-lab/attack-simulation/port_scan.sh

cd ~/soc-lab/attack-simulation
./ssh_bruteforce.sh
./port_scan.sh

sleep 180


###############################
# TASK 4 – DETECT & ANALYZE
###############################

python3 ~/soc-lab/scripts/wazuh_analyzer.py
python3 ~/soc-lab/scripts/zeek_analyzer.py

ls -lh ~/soc-lab/reports/

cat ~/soc-lab/reports/wazuh_report.txt
cat ~/soc-lab/reports/zeek_report.txt


###############################
# RESPONSE ACTIONS
###############################

sudo iptables -A INPUT -s 127.0.0.1 -j DROP
sudo iptables -L -n | grep 127.0.0.1

sudo iptables-save > ~/soc-lab/evidence/iptables_backup.txt

netstat -tuln > ~/soc-lab/evidence/netstat_output.txt
ps aux > ~/soc-lab/evidence/process_list.txt
last -20 > ~/soc-lab/evidence/login_history.txt

sudo cp /var/ossec/logs/alerts/alerts.json ~/soc-lab/evidence/
sudo cp /opt/zeek/logs/current/conn.log ~/soc-lab/evidence/

tar -czf evidence_$(date +%Y%m%d_%H%M%S).tar.gz evidence/


###############################
# TASK 5 – RECOVERY & VALIDATION
###############################

sudo /var/ossec/bin/rootcheck
sudo /var/ossec/bin/syscheck

sudo iptables -L -n -v

sudo /var/ossec/bin/agent_control -l

netstat -tuln | grep ESTABLISHED


###############################
# CREATE FINAL INCIDENT REPORT
###############################

nano ~/soc-lab/reports/final_incident_report.md

sudo /var/ossec/bin/agent_control -l
netstat -tuln | grep ESTABLISHED
sudo iptables -L -n -v
ps aux | grep -Ei 'suspicious|malware|backdoor'


############################################################
# END OF LAB 20 COMMAND EXECUTION
############################################################
