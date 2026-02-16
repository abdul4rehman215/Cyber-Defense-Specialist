#!/bin/bash

# Firewall Configuration Script
# Ubuntu 24.04 LTS Compatible

LOG_FILE="/var/log/firewall_config.log"

log_action() {
    echo -e "\033[0;32m[$(date '+%Y-%m-%d %H:%M:%S')] $1\033[0m"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Run as root."
        exit 1
    fi
}

configure_ufw() {

    log_action "Installing and configuring UFW..."

    apt update -y
    apt install -y ufw

    ufw --force reset

    ufw default deny incoming
    ufw default allow outgoing
    ufw default deny forward

    log_action "Default firewall policies configured."
}

configure_basic_rules() {

    log_action "Adding basic firewall rules..."

    ufw allow 22/tcp comment 'Allow SSH'
    ufw allow 80/tcp comment 'Allow HTTP'
    ufw allow 443/tcp comment 'Allow HTTPS'
    ufw allow 53/udp comment 'Allow DNS'

    log_action "Basic rules added."
}

configure_rate_limiting() {

    log_action "Configuring rate limiting and blocking common attack ports..."

    ufw limit ssh

    ufw deny 135/tcp
    ufw deny 139/tcp
    ufw deny 445/tcp
    ufw deny 3389/tcp

    log_action "Rate limiting and blocking rules configured."
}

enable_firewall() {

    log_action "Enabling firewall..."

    ufw --force enable
    ufw logging on

    ufw status verbose

    log_action "Firewall enabled successfully."
}

main() {

    check_root
    configure_ufw
    configure_basic_rules
    configure_rate_limiting
    enable_firewall

    log_action "Firewall configuration completed."
}

main "$@"
