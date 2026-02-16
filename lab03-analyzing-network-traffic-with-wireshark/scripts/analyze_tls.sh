#!/bin/bash
# ============================================================
# Script: analyze_tls.sh
# Purpose: Analyze TLS handshakes and encryption
# ============================================================

TLS_PCAP="/tmp/tls_traffic.pcap"

echo "=== TLS Traffic Analysis ==="

echo ""
echo "TLS Versions Used:"
tshark -r "$TLS_PCAP" -Y "tls.handshake.type == 1" -T fields \
-e tls.handshake.version | sort | uniq -c

echo ""
echo "Server Name Indication (SNI):"
tshark -r "$TLS_PCAP" -Y "tls.handshake.extensions_server_name" \
-T fields -e tls.handshake.extensions_server_name | sort | uniq

echo ""
echo "Cipher Suites:"
tshark -r "$TLS_PCAP" -Y "tls.handshake.type == 2" \
-T fields -e tls.handshake.ciphersuite | head -10

echo ""
echo "Certificate Issuers:"
tshark -r "$TLS_PCAP" -Y "tls.handshake.type == 11" \
-T fields -e x509sat.printableString | head -5
