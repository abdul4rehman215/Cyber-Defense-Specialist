#!/bin/bash
# ============================================================
# Script: detect_tls_issues.sh
# Purpose: Detect weak TLS versions and certificates
# ============================================================

TLS_PCAP="/tmp/tls_traffic.pcap"

echo "=== TLS Security Issue Detection ==="

tshark -r "$TLS_PCAP" -Y "tls.handshake.type == 1" -T fields \
-e tls.handshake.version | while read version; do
  case $version in
    "0x0300") echo "WARNING: SSL 3.0 detected (insecure)" ;;
    "0x0301") echo "WARNING: TLS 1.0 detected (deprecated)" ;;
    "0x0302") echo "WARNING: TLS 1.1 detected (deprecated)" ;;
    "0x0303") echo "INFO: TLS 1.2 detected" ;;
    "0x0304") echo "GOOD: TLS 1.3 detected" ;;
  esac
done

echo ""
echo "Certificate Validation Alerts:"
tshark -r "$TLS_PCAP" -Y "tls.alert_message.desc == 42" -T fields \
-e frame.time || echo "No certificate validation issues detected"
