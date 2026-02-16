#!/bin/bash
# ============================================================
# Script: detect_http_anomalies.sh
# Purpose: Detect HTTP-based attack patterns
# ============================================================

HTTP_PCAP="/tmp/http_analysis.pcap"

echo "=== HTTP Anomaly Detection ==="

echo ""
echo "Checking for SQL Injection patterns..."
tshark -r "$HTTP_PCAP" -Y "http.request" -T fields \
-e http.request.uri | grep -iE "(union|select|insert|delete|drop|'|--|;)" \
|| echo "No SQL injection patterns detected"

echo ""
echo "Checking for XSS patterns..."
tshark -r "$HTTP_PCAP" -Y "http.request" -T fields \
-e http.request.uri | grep -iE "(<script|javascript:|onload=|onerror=)" \
|| echo "No XSS patterns detected"

echo ""
echo "Checking for Directory Traversal..."
tshark -r "$HTTP_PCAP" -Y "http.request" -T fields \
-e http.request.uri | grep -E "(\.\./|\.\.\\)" \
|| echo "No directory traversal detected"
