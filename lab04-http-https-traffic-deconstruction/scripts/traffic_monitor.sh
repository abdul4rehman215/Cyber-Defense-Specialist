#!/bin/bash

INTERFACE="any"
DURATION=60
OUTPUT_DIR="./traffic_logs"

mkdir -p "$OUTPUT_DIR"

monitor_http_traffic() {
    timeout $DURATION sudo tcpdump -i $INTERFACE port 80 -A 2>/dev/null | \
    grep -Ei "union|select|script|../" >> "$OUTPUT_DIR/http_alerts.log"
}

monitor_https_traffic() {
    timeout $DURATION sudo tcpdump -i $INTERFACE port 443 -n 2>/dev/null >> "$OUTPUT_DIR/https_connections.log"
}

echo "Starting traffic monitoring..."
monitor_http_traffic &
monitor_https_traffic &
wait
echo "Monitoring completed."
