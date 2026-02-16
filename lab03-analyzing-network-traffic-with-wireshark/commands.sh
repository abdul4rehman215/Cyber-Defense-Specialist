#!/bin/bash
# ============================================================
# Lab 03: Analyzing Network Traffic with Wireshark
# File: commands.sh
# Environment: Ubuntu Linux
# User: toor
# Host: ip-172-31-10-212
# ============================================================

# ------------------------------------------------------------
# Task 1: System Update and Wireshark Installation
# ------------------------------------------------------------

sudo apt update

sudo apt install -y \
  wireshark \
  tshark \
  curl \
  wget \
  dnsutils

# ------------------------------------------------------------
# Task 2: Configure Non-Root Packet Capture
# ------------------------------------------------------------

sudo usermod -a -G wireshark $USER
newgrp wireshark

sudo dpkg-reconfigure wireshark-common

sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
getcap /usr/bin/dumpcap

# ------------------------------------------------------------
# Task 3: Verify Network Interfaces
# ------------------------------------------------------------

ip link show
tshark -D

# ------------------------------------------------------------
# Task 4: Start Packet Capture
# ------------------------------------------------------------

wireshark &

sudo tshark -i ens5 -w /tmp/network_capture.pcap &

# ------------------------------------------------------------
# Task 5: Generate DNS Traffic
# ------------------------------------------------------------

nslookup google.com
nslookup facebook.com
nslookup malicious-domain-example.com
nslookup suspicious.example.com
nslookup malware.test.com

# ------------------------------------------------------------
# Task 6: Generate HTTP Traffic
# ------------------------------------------------------------

curl -v http://httpbin.org/get
curl -v http://httpbin.org/user-agent

curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
http://httpbin.org/user-agent

curl -H "User-Agent: SuspiciousBot/1.0" \
http://httpbin.org/user-agent

# ------------------------------------------------------------
# Task 7: Generate HTTPS / TLS Traffic
# ------------------------------------------------------------

curl -v https://httpbin.org/get
curl -v https://www.google.com
curl -v https://badssl.com/
curl -k -v https://self-signed.badssl.com/

# ------------------------------------------------------------
# Task 8: Capture Filtered Traffic
# ------------------------------------------------------------

sudo tshark -i ens5 -f "port 53" -w /tmp/dns_traffic.pcap -c 50
sudo tshark -i ens5 -f "port 80" -w /tmp/http_traffic.pcap -c 50
sudo tshark -i ens5 -f "port 443" -w /tmp/https_traffic.pcap -c 50

# ------------------------------------------------------------
# Task 9: Open Captures in Wireshark
# ------------------------------------------------------------

wireshark /tmp/dns_traffic.pcap &
wireshark /tmp/http_traffic.pcap &
wireshark /tmp/https_traffic.pcap &

# ------------------------------------------------------------
# Task 10: HTTP Analysis Capture
# ------------------------------------------------------------

sudo tshark -i ens5 -f "port 80" -w /tmp/http_analysis.pcap -c 30 &

sleep 2
curl -v http://httpbin.org/get
curl -v http://httpbin.org/post -d "data=test"
curl -v http://httpbin.org/cookies/set/session/abc123

# ------------------------------------------------------------
# Task 11: TLS Traffic Capture
# ------------------------------------------------------------

sudo tshark -i ens5 -f "port 443" -w /tmp/tls_traffic.pcap -c 50 &

sleep 2
curl -v https://www.google.com
curl -v https://httpbin.org/get
curl -v https://badssl.com/

# ------------------------------------------------------------
# Task 12: Validate Capture Files
# ------------------------------------------------------------

ls -lh /tmp/*.pcap

# ------------------------------------------------------------
# End of commands.sh
# ------------------------------------------------------------
