#!/bin/bash
# ============================================================
# Script: detect_dns_tunneling.sh
# Purpose: Identify potential DNS tunneling behavior
# ============================================================

DNS_PCAP="/tmp/dns_traffic.pcap"

echo "=== DNS Tunneling Detection ==="

echo ""
echo "Checking for long DNS queries..."
tshark -r "$DNS_PCAP" -T fields -e dns.qry.name -Y "dns.flags.response == 0" | \
while read query; do
  if [ ${#query} -gt 50 ]; then
    echo "Suspicious long DNS query detected: $query"
  fi
done

echo ""
echo "DNS Query Types:"
tshark -r "$DNS_PCAP" -T fields -e dns.qry.type \
-Y "dns.flags.response == 0" | sort | uniq -c | sort -nr

echo ""
echo "Subdomain Depth Estimation:"
tshark -r "$DNS_PCAP" -T fields -e dns.qry.name \
-Y "dns.flags.response == 0" | \
awk -F'.' '{print NF-1}' | awk '{sum+=$1} END {print "Average subdomains per query:", sum/NR}'
