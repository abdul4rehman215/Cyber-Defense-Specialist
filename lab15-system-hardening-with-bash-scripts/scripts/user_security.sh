#!/bin/bash

# User Account Security Script
# Ubuntu 24.04 Compatible

LOG_FILE="/var/log/user_security.log"

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

check_empty_passwords() {

    log_action "Checking for empty passwords..."

    awk -F: '($2==""){print $1}' /etc/shadow | while read user; do
        if [ "$user" != "root" ]; then
            passwd -l "$user"
            log_action "Locked account with empty password: $user"
        fi
    done
}

check_duplicate_uids() {

    log_action "Checking for duplicate UIDs..."

    cut -d: -f3 /etc/passwd | sort | uniq -d | while read uid; do
        log_action "Duplicate UID found: $uid"
    done
}

configure_account_lockout() {

    log_action "Configuring account lockout policy..."

    apt install -y libpam-modules

    cp /etc/pam.d/common-auth /etc/pam.d/common-auth.bak

    echo "auth required pam_tally2.so deny=3 unlock_time=600 onerr=fail audit even_deny_root" >> /etc/pam.d/common-auth
}

set_password_aging() {

    log_action "Setting password aging..."

    for user in $(awk -F: '$3 >= 1000 && $1 != "nobody" {print $1}' /etc/passwd); do
        chage -M 90 -m 7 -W 14 "$user"
        log_action "Updated password aging for $user"
    done
}

main() {

    check_root
    check_empty_passwords
    check_duplicate_uids
    configure_account_lockout
    set_password_aging

    log_action "User security configuration completed."
}

main "$@"
