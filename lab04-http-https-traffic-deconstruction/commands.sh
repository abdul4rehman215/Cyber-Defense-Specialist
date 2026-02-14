#!/bin/bash

# ==========================================================
# Lab 04: HTTP/HTTPS Traffic Deconstruction
# Host: ip-172-31-10-224
# User: toor
# ==========================================================

echo "Starting Lab 04 - HTTP/HTTPS Traffic Deconstruction"

# ----------------------------------------------------------
# Task 1: HTTP Server Setup
# ----------------------------------------------------------

mkdir -p ~/http_analysis_lab
cd ~/http_analysis_lab

pwd

# Create test HTML file
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>HTTP Analysis Lab</title>
</head>
<body>
    <h1>Test Server</h1>
</body>
</html>
EOF

# Start Python HTTP server
python3 -m http.server 8080 &
echo $! > server.pid

sleep 2

# ----------------------------------------------------------
# Task 2: Capture HTTP Traffic
# ----------------------------------------------------------

sudo tcpdump -i lo -w http_traffic.pcap port 8080 &
echo $! > tcpdump.pid

sleep 2

# Generate normal HTTP request
curl -v http://localhost:8080/

# Generate custom User-Agent
curl -v -H "User-Agent: TestBot/1.0" http://localhost:8080/

# Generate POST request
curl -v -X POST -d "username=admin&password=test" http://localhost:8080/login

# Simulate Path Traversal
curl -v http://localhost:8080/../../etc/passwd

# Simulate XSS
curl -v "http://localhost:8080/search?q=<script>alert('xss')</script>"

sleep 3

# Stop tcpdump capture
sudo kill "$(cat tcpdump.pid)"

ls -lh http_traffic.pcap

# ----------------------------------------------------------
# Task 3: Extract HTTP Payloads
# ----------------------------------------------------------

tcpdump -r http_traffic.pcap -A -s 0 > http_requests.txt

ls -lh http_requests.txt

# Analyze HTTP methods
grep -E "^(GET|POST|PUT|DELETE)" http_requests.txt

# Analyze User-Agents
grep -i "user-agent:" http_requests.txt

# Count HTTP methods
grep -E "^(GET|POST)" http_requests.txt | awk '{print $1}' | sort | uniq -c

# ----------------------------------------------------------
# Task 4: Create and Test HTTP Parser
# ----------------------------------------------------------

cat > test_requests.txt << 'EOF'
GET / HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0

POST /login HTTP/1.1
Host: localhost:8080
User-Agent: AttackBot/1.0
Content-Length: 50

GET /admin' OR '1'='1 HTTP/1.1
Host: localhost:8080

GET /../../../etc/passwd HTTP/1.1
Host: localhost:8080
X-Forwarded-For: 10.0.0.1
EOF

python3 http_parser.py test_requests.txt

# ----------------------------------------------------------
# Task 5: HTTPS Certificate Analysis
# ----------------------------------------------------------

chmod +x analyze_cert.sh
./analyze_cert.sh www.google.com

# ----------------------------------------------------------
# Task 6: HTTPS Timing Analysis
# ----------------------------------------------------------

chmod +x timing_analysis.sh
./timing_analysis.sh https://www.google.com

# ----------------------------------------------------------
# Task 7: Real-Time Monitoring
# ----------------------------------------------------------

chmod +x traffic_monitor.sh
./traffic_monitor.sh

ls -l traffic_logs/

cat traffic_logs/http_alerts.log

# ----------------------------------------------------------
# Task 8: Alert System Execution
# ----------------------------------------------------------

chmod +x alert_system.py
python3 alert_system.py

cat alerts.log

echo "Lab 04 Commands Execution Completed"
