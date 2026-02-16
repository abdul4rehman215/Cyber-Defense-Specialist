# INCIDENT RESPONSE REPORT

## Executive Summary
A simulated SSH brute force attack and port scan were detected and analyzed using Wazuh and Zeek. Automated detection scripts identified suspicious activity and response actions were executed.

## Incident Details
- **Date/Time**: [Insert current timestamp]
- **Incident Type**: SSH Brute Force & Port Scan
- **Severity**: High
- **Affected Systems**: Localhost (Lab Environment)

## Detection
- **Detection Method**: Wazuh log monitoring, Zeek traffic analysis
- **Tools Used**: Wazuh, Zeek, Custom Python Scripts
- **Key Indicators**:
  - Multiple failed SSH login attempts
  - High number of port connections from single IP
  - Elevated alert severity levels

## Analysis
Attack simulations generated repeated failed login attempts and connections to multiple ports. Wazuh detected authentication failures. Zeek detected port scanning behavior (connections to >20 unique ports).

## Response Actions
1. Identified suspicious IP address
2. Blocked IP using iptables
3. Collected forensic evidence (logs, netstat, process list)
4. Generated incident report

## Evidence Collected
- Wazuh alerts.json
- Zeek conn.log
- Netstat output
- Process list
- Firewall rule backup

## Recovery Steps
1. Verified system integrity with rootcheck
2. Confirmed no unauthorized file modifications
3. Reviewed active connections

## Lessons Learned
- Automated detection significantly reduces response time
- Combining host and network monitoring improves visibility
- Documentation is critical for post-incident review

## Recommendations
- Enable persistent firewall rules
- Implement centralized SIEM
- Deploy real-time alert notifications
- Conduct periodic incident response drills

---
Report prepared by: SOC Analyst  
Date: 16-02-2026
