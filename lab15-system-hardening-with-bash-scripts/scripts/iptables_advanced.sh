#!/bin/bash

# Advanced iptables Configuration
# Ubuntu 24.04 Compatible

LOG_FILE="/var/log/iptables_advanced.log"

log_action() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
    echo "$1"
}

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Run as root."
        exit 1
    fi
}

configure_syn_flood_protection() {

    log_action "Configuring SYN flood protection..."

    iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
    iptables -A INPUT -p tcp --syn -j DROP
}

configure_port_scan_protection() {

    log_action "Configuring port scan protection..."

    iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP
    iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
    iptables -A INPUT -p tcp --tcp-flags ALL FIN,URG,PSH -j DROP
}

block_invalid_packets() {

    log_action "Blocking invalid packets..."

    iptables -A INPUT -m state --state INVALID -j DROP
    iptables -A FORWARD -m state --state INVALID -j DROP
    iptables -A OUTPUT -m state --state INVALID -j DROP
}

save_rules() {

    log_action "Installing iptables-persistent and saving rules..."

    apt install -y iptables-persistent

    netfilter-persistent save
}

main() {

    check_root
    configure_syn_flood_protection
    configure_port_scan_protection
    block_invalid_packets
    save_rules

    log_action "Advanced iptables configuration completed."
}

main "$@"
