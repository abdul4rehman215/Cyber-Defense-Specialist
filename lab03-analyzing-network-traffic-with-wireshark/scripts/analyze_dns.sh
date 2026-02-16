#!/bin/bash
# ============================================================
# Script: analyze_dns.sh
# Lab: Analyzing Network Traffic with Wireshark
# Purpose: Analyze DNS traffic for patterns and anomalies
# ============================================================

echo "=== DNS Traffic Analysis ==="
echo "Analyzing DNS queries from capture file..."

DNS_PCAP="/tmp/dns_traffic.pcap"

# Extract DNS queries
tshark -r "$DNS_PCAP" -T fields -e dns.qry.name -Y "dns.flags.response == 0" > /tmp/dns_queries.txt

echo ""
echo "Top DNS Queries:"
sort /tmp/dns_queries.txt | uniq -c | sort -nr | head -10

echo ""
echo "Potential Suspicious Domains:"
grep -E "(malware|suspicious|phishing|botnet|trojan)" /tmp/dns_queries.txt || echo "No obvious malicious domains detected"

echo ""
echo "Top-Level Domain (TLD) Analysis:"
grep -o '\.[a-z]*$' /tmp/dns_queries.txt | sort | uniq -c | sort -nr

echo ""
echo "DNS Responses (Sample):"
tshark -r "$DNS_PCAP" -T fields -e dns.resp.name -e dns.a \
-Y "dns.flags.response == 1 and dns.a" | head -10
