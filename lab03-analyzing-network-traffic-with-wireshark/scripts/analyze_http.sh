#!/bin/bash
# ============================================================
# Script: analyze_http.sh
# Purpose: Analyze HTTP traffic for anomalies
# ============================================================

HTTP_PCAP="/tmp/http_analysis.pcap"

echo "=== HTTP Traffic Analysis ==="

echo ""
echo "HTTP Methods Used:"
tshark -r "$HTTP_PCAP" -Y "http.request" -T fields \
-e http.request.method | sort | uniq -c

echo ""
echo "User-Agent Analysis:"
tshark -r "$HTTP_PCAP" -Y "http.request" -T fields \
-e http.user_agent | sort | uniq -c

echo ""
echo "Requested URLs:"
tshark -r "$HTTP_PCAP" -Y "http.request" -T fields \
-e http.host -e http.request.uri | head -10

echo ""
echo "HTTP Response Codes:"
tshark -r "$HTTP_PCAP" -Y "http.response" -T fields \
-e http.response.code | sort | uniq -c

echo ""
echo "Suspicious User-Agents:"
tshark -r "$HTTP_PCAP" -Y "http.request" -T fields \
-e http.user_agent | grep -iE "(bot|scanner|crawler|exploit)" || echo "No suspicious User-Agents found"
