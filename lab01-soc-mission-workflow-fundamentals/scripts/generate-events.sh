#!/bin/bash
# ============================================================
# Script: generate-events.sh
# Purpose: Generate simulated security events for SOC testing
# ============================================================

# Generate failed SSH login attempts
logger -p auth.warning "sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2"
logger -p auth.warning "sshd[1235]: Failed password for invalid user root from 10.0.0.50 port 22 ssh2"

# Generate successful SSH login
logger -p auth.info "sshd[1236]: Accepted password for user from 192.168.1.10 port 22 ssh2"

# Generate suspicious firewall activity
logger -p daemon.warning "kernel: [UFW BLOCK] IN=ens5 OUT= MAC= SRC=192.168.1.200 DST=192.168.1.1 PROTO=TCP SPT=12345 DPT=22"

# Generate system service events
logger -p daemon.info "systemd[1]: Started Security monitoring service"
logger -p daemon.warning "systemd[1]: Failed to start suspicious-service.service"

echo "Sample security events generated and logged"
