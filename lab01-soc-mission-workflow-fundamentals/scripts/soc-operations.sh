#!/bin/bash
# ============================================================
# Script: soc-operations.sh
# Purpose: SOC Operations Menu for analysts
# ============================================================

while true; do
  clear
  echo "=================================="
  echo "        SOC OPERATIONS MENU        "
  echo "=================================="
  echo "1. View SOC Dashboard"
  echo "2. Generate Test Security Events"
  echo "3. Check SIEM System Status"
  echo "4. View Recent Alerts"
  echo "5. Search Logs"
  echo "6. View SOC Documentation"
  echo "7. Exit"
  echo "=================================="
  read -p "Select an option (1-7): " choice

  case $choice in
    1)
      ~/soc-lab/scripts/soc-dashboard.sh
      read -p "Press Enter to continue..."
      ;;
    2)
      echo "Generating test security events..."
      ~/soc-lab/scripts/generate-events.sh
      read -p "Press Enter to continue..."
      ;;
    3)
      echo "SYSTEM STATUS CHECK"
      echo "==================="
      systemctl status elasticsearch --no-pager -l
      systemctl status kibana --no-pager -l
      systemctl status logstash --no-pager -l
      read -p "Press Enter to continue..."
      ;;
    4)
      echo "RECENT ALERTS"
      echo "============="
      tail -20 /var/log/elastalert/elastalert.log 2>/dev/null | \
      grep -E "(Alert|Match found)" || echo "No recent alerts found"
      read -p "Press Enter to continue..."
      ;;
    5)
      read -p "Enter search keyword: " keyword
      echo "Searching logs for: $keyword"
      grep -i "$keyword" /var/log/syslog /var/log/auth.log | tail -10
      read -p "Press Enter to continue..."
      ;;
    6)
      echo "AVAILABLE DOCUMENTATION"
      echo "======================="
      echo "1. SOC Mission Statement"
      echo "2. Incident Response Procedures"
      read -p "Select document (1-2): " doc

      case $doc in
        1) cat ~/soc-lab/documentation/soc-mission.txt ;;
        2) cat ~/soc-lab/documentation/incident-response.txt ;;
        *) echo "Invalid selection" ;;
      esac
      read -p "Press Enter to continue..."
      ;;
    7)
      echo "Exiting SOC Operations..."
      exit 0
      ;;
    *)
      echo "Invalid option. Please try again."
      sleep 2
      ;;
  esac
done
