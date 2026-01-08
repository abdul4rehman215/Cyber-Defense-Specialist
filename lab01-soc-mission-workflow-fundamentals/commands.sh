#!/bin/bash
# ============================================================
# Lab 01: SOC Mission & Workflow Fundamentals
# File: commands.sh
# Purpose: Complete command history executed during the lab
# Environment: Ubuntu 24.04.1 LTS
# User: toor
# ============================================================

# ------------------------------------------------------------
# Task 1: SOC Documentation Setup
# ------------------------------------------------------------

mkdir -p ~/soc-lab/documentation

cat > ~/soc-lab/documentation/soc-mission.txt << 'EOF'
SOC MISSION STATEMENT
====================
Mission: To provide continuous monitoring, detection, and response to cybersecurity
threats while maintaining the confidentiality, integrity, and availability of
organizational assets.

Core Objectives:
1. Monitor network traffic and system logs 24/7
2. Detect and analyze security incidents
3. Respond to threats in a timely manner
4. Document and report security events
5. Continuously improve security posture

Key Performance Indicators:
- Mean Time to Detection (MTTD)
- Mean Time to Response (MTTR)
- Number of incidents detected and resolved
- False positive rate
- System availability percentage

SOC Maturity Level: Level 2 (Developing)
Target Maturity Level: Level 3 (Defined)
EOF

cat ~/soc-lab/documentation/soc-mission.txt

# ------------------------------------------------------------
# Task 2: System Update & Java Installation
# ------------------------------------------------------------

sudo apt update
sudo apt install -y openjdk-11-jdk
java -version

# ------------------------------------------------------------
# Task 3: Elasticsearch Installation & Configuration
# ------------------------------------------------------------

wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" \
| sudo tee /etc/apt/sources.list.d/elastic7.x.list

sudo apt update
sudo apt install -y elasticsearch

sudo sed -i 's/#network.host: 192.168.0.1/network.host: localhost/' \
/etc/elasticsearch/elasticsearch.yml

sudo sed -i 's/#http.port: 9200/http.port: 9200/' \
/etc/elasticsearch/elasticsearch.yml

sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch

sleep 30
curl -X GET "localhost:9200/"

# ------------------------------------------------------------
# Task 4: Kibana Installation & Configuration
# ------------------------------------------------------------

sudo apt install -y kibana

sudo sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/' \
/etc/kibana/kibana.yml

sudo sed -i 's/#elasticsearch.hosts:/elasticsearch.hosts:/' \
/etc/kibana/kibana.yml

sudo systemctl start kibana
sudo systemctl enable kibana

sleep 60

# ------------------------------------------------------------
# Task 5: Logstash Installation & Configuration
# ------------------------------------------------------------

sudo apt install -y logstash
sudo mkdir -p /etc/logstash/conf.d

cat > /tmp/logstash-syslog.conf << 'EOF'
input {
 file {
   path => "/var/log/syslog"
   start_position => "beginning"
   type => "syslog"
 }
 file {
   path => "/var/log/auth.log"
   start_position => "beginning"
   type => "auth"
 }
}

filter {
 if [type] == "syslog" {
   grok {
     match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{IPORHOST:host} %{DATA:program}(?:\\[%{POSINT:pid}\\])?: %{GREEDYDATA:message}" }
   }
 }

 if [type] == "auth" {
   grok {
     match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{IPORHOST:host} %{DATA:program}(?:\\[%{POSINT:pid}\\])?: %{GREEDYDATA:auth_message}" }
   }
 }
}

output {
 elasticsearch {
   hosts => ["localhost:9200"]
   index => "soc-logs-%{+YYYY.MM.dd}"
 }
 stdout { codec => rubydebug }
}
EOF

sudo mv /tmp/logstash-syslog.conf /etc/logstash/conf.d/

sudo systemctl start logstash
sudo systemctl enable logstash

# ------------------------------------------------------------
# Task 6: Generate Sample Security Events
# ------------------------------------------------------------

mkdir -p ~/soc-lab/scripts

cat > ~/soc-lab/scripts/generate-events.sh << 'EOF'
#!/bin/bash

logger -p auth.warning "sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2"
logger -p auth.warning "sshd[1235]: Failed password for invalid user root from 10.0.0.50 port 22 ssh2"
logger -p auth.info "sshd[1236]: Accepted password for user from 192.168.1.10 port 22 ssh2"
logger -p daemon.warning "kernel: [UFW BLOCK] IN=ens5 SRC=192.168.1.200 DST=192.168.1.1 PROTO=TCP DPT=22"
logger -p daemon.info "systemd[1]: Started Security monitoring service"
logger -p daemon.warning "systemd[1]: Failed to start suspicious-service.service"

echo "Sample security events generated and logged"
EOF

chmod +x ~/soc-lab/scripts/generate-events.sh
~/soc-lab/scripts/generate-events.sh

# ------------------------------------------------------------
# Task 7: Elasticsearch Data Verification
# ------------------------------------------------------------

sleep 60
curl -X GET "localhost:9200/_cat/indices?v"

curl -X GET "localhost:9200/soc-logs-*/_search?pretty" \
-H 'Content-Type: application/json' -d'
{
  "query": { "match_all": {} },
  "size": 5,
  "sort": [
    { "@timestamp": { "order": "desc" } }
  ]
}
'

# ------------------------------------------------------------
# Task 8: ElastAlert Installation & Configuration
# ------------------------------------------------------------

sudo apt install -y python3-pip
sudo pip3 install elastalert

sudo mkdir -p /etc/elastalert/rules
sudo mkdir -p /var/log/elastalert

cat > /tmp/elastalert-config.yaml << 'EOF'
rules_folder: /etc/elastalert/rules
run_every:
  minutes: 1
buffer_time:
  minutes: 15
es_host: localhost
es_port: 9200
writeback_index: elastalert_status
alert_time_limit:
  days: 2
EOF

sudo mv /tmp/elastalert-config.yaml /etc/elastalert/config.yaml

# ------------------------------------------------------------
# Task 9: Service Health Checks
# ------------------------------------------------------------

sudo systemctl status elasticsearch --no-pager | grep Active
sudo systemctl status kibana --no-pager | grep Active
sudo systemctl status logstash --no-pager | grep Active

if pgrep -f elastalert > /dev/null; then
  echo "ElastAlert is RUNNING"
else
  echo "ElastAlert is STOPPED - Starting it now..."
  nohup elastalert --config /etc/elastalert/config.yaml --verbose \
  > /var/log/elastalert/elastalert.log 2>&1 &
  sleep 5
  echo "ElastAlert started"
fi

curl -s "localhost:9200/_cluster/health?pretty" | grep status
curl -s "localhost:9200/_cat/indices?v" | grep soc-logs

# ------------------------------------------------------------
# End of commands.sh
# ------------------------------------------------------------
