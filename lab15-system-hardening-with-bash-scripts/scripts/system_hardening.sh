#!/bin/bash

# System Hardening Script
# Ubuntu 24.04 LTS Compatible

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

LOG_FILE="/var/log/system_hardening.log"

log_action() {
    local message="$1"
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')] $message${NC}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $message" >> "$LOG_FILE"
}

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo -e "${RED}Please run as root or with sudo.${NC}"
        exit 1
    fi
}

update_system() {
    log_action "Updating system packages..."
    apt update -y && apt upgrade -y
    if [ $? -eq 0 ]; then
        log_action "System updated successfully."
    else
        log_action "System update failed."
    fi
}

configure_password_policy() {
    log_action "Configuring password policies..."

    apt install -y libpam-pwquality

    cp /etc/pam.d/common-password /etc/pam.d/common-password.bak

    sed -i 's/^# minlen =.*/minlen = 12/' /etc/security/pwquality.conf
    sed -i 's/^# minclass =.*/minclass = 3/' /etc/security/pwquality.conf

    sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS   90/' /etc/login.defs
    sed -i 's/^PASS_MIN_DAYS.*/PASS_MIN_DAYS   7/' /etc/login.defs

    log_action "Password policy configured."
}

disable_unnecessary_services() {

    log_action "Disabling unnecessary services..."

    services=("avahi-daemon" "cups" "bluetooth")

    for service in "${services[@]}"; do
        if systemctl is-enabled "$service" &>/dev/null; then
            systemctl disable "$service"
            systemctl stop "$service"
            log_action "Disabled $service"
        fi
    done
}

configure_kernel_parameters() {

    log_action "Configuring kernel security parameters..."

    cp /etc/sysctl.conf /etc/sysctl.conf.bak

    cat <<EOF >> /etc/sysctl.conf

# Security Hardening
net.ipv4.ip_forward = 0
net.ipv4.conf.all.accept_source_route = 0
net.ipv4.tcp_syncookies = 1
net.ipv4.conf.all.log_martians = 1
EOF

    sysctl -p
    log_action "Kernel parameters configured."
}

secure_file_permissions() {

    log_action "Securing critical file permissions..."

    chmod 600 /etc/shadow
    chmod 600 /etc/gshadow
    chmod 644 /etc/passwd
    chmod 644 /etc/group

    chmod 700 /root
    chmod 700 /home/*

    log_action "File permissions secured."
}

main() {

    echo "========================================"
    echo " Linux System Hardening Script "
    echo "========================================"

    check_root
    update_system
    configure_password_policy
    disable_unnecessary_services
    configure_kernel_parameters
    secure_file_permissions

    log_action "System hardening completed successfully."
}

main "$@"
