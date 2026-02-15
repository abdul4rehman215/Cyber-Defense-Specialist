#!/bin/bash

# ================================
# SYSTEM UPDATE & DOCKER SETUP
# ================================

sudo apt update && sudo apt upgrade -y
sudo apt install docker.io docker-compose-plugin -y

docker --version
docker compose version

sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker


# ================================
# WAZUH DEPLOYMENT
# ================================

mkdir -p ~/wazuh-soar-lab
cd ~/wazuh-soar-lab

curl -so docker-compose.yml https://raw.githubusercontent.com/wazuh/wazuh-docker/v4.7.0/singlenode/docker-compose.yml

docker compose up -d

sleep 300

docker compose ps


# ================================
# THEHIVE DEPLOYMENT
# ================================

mkdir -p ~/thehive-soar
cd ~/thehive-soar

nano docker-compose.yml

docker compose up -d

sleep 120

docker compose ps


# ================================
# CORTEX DEPLOYMENT
# ================================

mkdir -p ~/cortex-soar
cd ~/cortex-soar

nano docker-compose.yml

docker compose up -d

sleep 90

docker compose ps


# ================================
# SOAR INTEGRATION FRAMEWORK
# ================================

mkdir -p ~/soar-integration/{connectors,playbooks,workflows,logs,tests}
cd ~/soar-integration

pip3 install requests urllib3 pyyaml


# ================================
# CONNECTORS
# ================================

nano connectors/wazuh_connector.py
nano connectors/thehive_connector.py


# ================================
# PLAYBOOKS
# ================================

nano playbooks/malware_response.py
nano playbooks/bruteforce_response.py


# ================================
# WORKFLOW ENGINE
# ================================

nano workflows/orchestrator.py
nano config.yaml
nano main.py


# ================================
# PERMISSIONS
# ================================

chmod +x main.py
chmod +x workflows/orchestrator.py
chmod +x playbooks/*.py
chmod +x connectors/*.py


# ================================
# INTEGRATION TESTING
# ================================

mkdir -p tests
nano tests/test_integration.py

python3 -m unittest tests/test_integration.py


# ================================
# RUN SOAR PLATFORM
# ================================

cd ~/soar-integration
python3 main.py

tail -f logs/soar_integration.log

ls logs/
