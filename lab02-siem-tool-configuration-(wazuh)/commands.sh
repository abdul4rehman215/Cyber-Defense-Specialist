#!/bin/bash
# ------------------------------------------------------------
# Task 1: System Preparation and Updates
# ------------------------------------------------------------

sudo apt update && sudo apt upgrade -y

sudo apt install -y \
  curl \
  apt-transport-https \
  lsb-release \
  gnupg2 \
  software-properties-common

uname -a
cat /etc/os-release

# ------------------------------------------------------------
# Task 2: Install Wazuh Repository
# ------------------------------------------------------------

curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | \
gpg --no-default-keyring \
--keyring gnupgring:/usr/share/keyrings/wazuh.gpg --import

sudo chmod 644 /usr/share/keyrings/wazuh.gpg

echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | \
sudo tee /etc/apt/sources.list.d/wazuh.list

sudo apt update

# ------------------------------------------------------------
# Task 3: Install Wazuh Manager
# ------------------------------------------------------------

sudo apt install -y wazuh-manager

sudo systemctl daemon-reload
sudo systemctl enable wazuh-manager
sudo systemctl start wazuh-manager

sudo systemctl status wazuh-manager

# ------------------------------------------------------------
# Task 4: Install and Configure Wazuh Agent (Local)
# ------------------------------------------------------------

sudo apt install -y wazuh-agent

sudo sed -i \
's/<server>.*<\/server>/<server>127.0.0.1<\/server>/' \
/var/ossec/etc/ossec.conf

echo "WAZUH_MANAGER='127.0.0.1'" | sudo tee /var/ossec/etc/preloaded-vars.conf
echo "WAZUH_AGENT_NAME='local-agent'" | sudo tee -a /var/ossec/etc/preloaded-vars.conf
echo "WAZUH_AGENT_GROUP='default'" | sudo tee -a /var/ossec/etc/preloaded-vars.conf

sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent

sudo systemctl status wazuh-agent

# ------------------------------------------------------------
# Task 5: Install Elasticsearch
# ------------------------------------------------------------

sudo apt install -y openjdk-11-jdk

wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | \
sudo tee /etc/apt/sources.list.d/elastic-7.x.list

sudo apt update
sudo apt install -y elasticsearch=7.17.13

sudo tee /etc/elasticsearch/elasticsearch.yml > /dev/null <<EOF
network.host: 127.0.0.1
http.port: 9200
cluster.initial_master_nodes: ["node-1"]
node.name: node-1
cluster.name: wazuh-cluster
discovery.type: single-node
EOF

sudo systemctl daemon-reload
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch

sudo systemctl status elasticsearch

# ------------------------------------------------------------
# Task 6: Install and Configure Kibana
# ------------------------------------------------------------

sudo apt install -y kibana=7.17.13

sudo tee /etc/kibana/kibana.yml > /dev/null <<EOF
server.host: "127.0.0.1"
server.port: 5601
elasticsearch.hosts: ["http://127.0.0.1:9200"]
EOF

sudo systemctl daemon-reload
sudo systemctl enable kibana
sudo systemctl start kibana

sudo systemctl status kibana

# ------------------------------------------------------------
# Task 7: Install Wazuh Kibana Plugin
# ------------------------------------------------------------

sudo -u kibana /usr/share/kibana/bin/kibana-plugin install \
https://packages.wazuh.com/4.x/ui/kibana/wazuh_kibana-4.5.4_7.17.13-1.zip

sudo systemctl restart kibana

# ------------------------------------------------------------
# Task 8: Configure Log Collection & Integrity Monitoring
# ------------------------------------------------------------

sudo tee -a /var/ossec/etc/ossec.conf > /dev/null <<EOF
<localfile>
 <log_format>syslog</log_format>
 <location>/var/log/auth.log</location>
</localfile>

<localfile>
 <log_format>syslog</log_format>
 <location>/var/log/syslog</location>
</localfile>

<localfile>
 <log_format>apache</log_format>
 <location>/var/log/apache2/access.log</location>
</localfile>

<localfile>
 <log_format>apache</log_format>
 <location>/var/log/apache2/error.log</location>
</localfile>

<syscheck>
 <directories check_all="yes">/etc,/usr/bin,/usr/sbin</directories>
 <directories check_all="yes">/bin,/sbin</directories>
 <directories check_all="yes" realtime="yes">/home</directories>
</syscheck>
EOF

sudo systemctl restart wazuh-manager
sudo systemctl restart wazuh-agent

# ------------------------------------------------------------
# Task 9: Connectivity and Health Checks
# ------------------------------------------------------------

sudo systemctl status wazuh-manager
sudo systemctl status wazuh-agent
sudo systemctl status elasticsearch
sudo systemctl status kibana

curl -X GET "127.0.0.1:9200/_cluster/health?pretty"

sudo /var/ossec/bin/agent_control -l

# ------------------------------------------------------------
# Task 10: Generate Test Security Events
# ------------------------------------------------------------

for i in {1..5}; do
  echo "wrong_password" | su - nonexistent_user 2>/dev/null || true
  sleep 2
done

sudo touch /etc/test_file_$(date +%s)
echo "test content" | sudo tee /etc/test_config_change > /dev/null

curl -s http://httpbin.org/ip > /dev/null
ping -c 3 8.8.8.8 > /dev/null

# ------------------------------------------------------------
# Task 11: Custom Detection Rules
# ------------------------------------------------------------

sudo tee /var/ossec/etc/rules/local_rules.xml > /dev/null <<EOF
<group name="local,">
 <rule id="100001" level="10">
  <if_matched_sid>5503</if_matched_sid>
  <same_source_ip />
  <description>Multiple failed login attempts from same source</description>
  <group>authentication_failures,</group>
 </rule>

 <rule id="100002" level="7">
  <category>ossec</category>
  <decoded_as>syscheck_new_entry</decoded_as>
  <match>/etc</match>
  <description>New file created in /etc directory</description>
  <group>syscheck,</group>
 </rule>
</group>
EOF

sudo systemctl restart wazuh-manager

# ------------------------------------------------------------
# Task 12: Active Response Configuration
# ------------------------------------------------------------

sudo tee -a /var/ossec/etc/ossec.conf > /dev/null <<EOF
<active-response>
 <disabled>no</disabled>
 <command>firewall-drop</command>
 <location>local</location>
 <rules_id>100001</rules_id>
 <timeout>300</timeout>
</active-response>
EOF

sudo systemctl restart wazuh-manager
