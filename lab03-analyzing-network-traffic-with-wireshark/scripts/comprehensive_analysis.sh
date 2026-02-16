#!/bin/bash
# ============================================================
# Script: comprehensive_analysis.sh
# Purpose: Generate a full network traffic analysis report
# ============================================================

REPORT="/tmp/network_analysis_report.txt"

echo "COMPREHENSIVE NETWORK TRAFFIC ANALYSIS REPORT" > $REPORT
echo "Generated on: $(date)" >> $REPORT
echo "Analyst: $(whoami)" >> $REPORT
echo "---------------------------------------------" >> $REPORT

echo "" >> $REPORT
echo "DNS Analysis:" >> $REPORT
/tmp/analyze_dns.sh >> $REPORT

echo "" >> $REPORT
echo "HTTP Analysis:" >> $REPORT
/tmp/analyze_http.sh >> $REPORT

echo "" >> $REPORT
echo "TLS Analysis:" >> $REPORT
/tmp/analyze_tls.sh >> $REPORT

cat $REPORT
