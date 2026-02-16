#!/bin/bash

# System Hardening Verification Script
# Ubuntu 24.04 Compatible

REPORT_FILE="/var/log/hardening_report.txt"

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Run as root."
        exit 1
    fi
}

verify_password_policy() {

    echo "Verifying Password Policy..." >> "$REPORT_FILE"

    grep "^minlen" /etc/security/pwquality.conf >> "$REPORT_FILE"
    grep "^minclass" /etc/security/pwquality.conf >> "$REPORT_FILE"
    grep "^PASS_MAX_DAYS" /etc/login.defs >> "$REPORT_FILE"
    grep "^PASS_MIN_DAYS" /etc/login.defs >> "$REPORT_FILE"

    echo "" >> "$REPORT_FILE"
}

verify_firewall() {

    echo "Verifying Firewall..." >> "$REPORT_FILE"

    ufw status verbose >> "$REPORT_FILE"

    echo "" >> "$REPORT_FILE"
}

verify_ssh_config() {

    echo "Verifying SSH Configuration..." >> "$REPORT_FILE"

    grep -E "PermitRootLogin|PasswordAuthentication|MaxAuthTries|PermitEmptyPasswords|ClientAliveInterval|ClientAliveCountMax|Protocol" /etc/ssh/sshd_config >> "$REPORT_FILE"

    systemctl is-active ssh >> "$REPORT_FILE"

    echo "" >> "$REPORT_FILE"
}

verify_services() {

    echo "Verifying Disabled Services..." >> "$REPORT_FILE"

    systemctl list-unit-files --type=service --state=disabled >> "$REPORT_FILE"

    echo "" >> "$REPORT_FILE"
}

generate_report() {

    echo "System Hardening Verification Report" > "$REPORT_FILE"
    echo "Generated on: $(date)" >> "$REPORT_FILE"
    echo "=====================================" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"

    verify_password_policy
    verify_firewall
    verify_ssh_config
    verify_services

    echo "Verification Completed." >> "$REPORT_FILE"

    cat "$REPORT_FILE"
}

main() {

    check_root
    generate_report
}

main "$@"
