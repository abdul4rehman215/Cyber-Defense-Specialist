#!/bin/bash

# SSH Hardening Script
# Ubuntu 24.04 Compatible

LOG_FILE="/var/log/ssh_hardening.log"

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

backup_ssh_config() {
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
    log_action "SSH configuration backed up."
}

configure_ssh_security() {

    log_action "Applying SSH security settings..."

    sed -i 's/^#\?PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
    sed -i 's/^#\?PasswordAuthentication.*/PasswordAuthentication no/' /etc/ssh/sshd_config
    sed -i 's/^#\?MaxAuthTries.*/MaxAuthTries 3/' /etc/ssh/sshd_config
    sed -i 's/^#\?PermitEmptyPasswords.*/PermitEmptyPasswords no/' /etc/ssh/sshd_config
    sed -i 's/^#\?ClientAliveInterval.*/ClientAliveInterval 300/' /etc/ssh/sshd_config
    sed -i 's/^#\?ClientAliveCountMax.*/ClientAliveCountMax 2/' /etc/ssh/sshd_config
    sed -i 's/^#\?Protocol.*/Protocol 2/' /etc/ssh/sshd_config

    log_action "SSH security parameters configured."
}

configure_ssh_banner() {

    log_action "Configuring SSH login banner..."

    echo "Unauthorized access is prohibited. All activities are monitored." > /etc/ssh/banner
    echo "Banner /etc/ssh/banner" >> /etc/ssh/sshd_config
}

restart_ssh_service() {

    log_action "Testing SSH configuration..."

    sshd -t
    if [ $? -ne 0 ]; then
        log_action "SSH configuration test failed."
        exit 1
    fi

    systemctl restart ssh
    systemctl status ssh --no-pager
}

main() {

    check_root
    backup_ssh_config
    configure_ssh_security
    configure_ssh_banner
    restart_ssh_service

    log_action "SSH hardening completed."
}

main "$@"
