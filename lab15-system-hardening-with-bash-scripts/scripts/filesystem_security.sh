#!/bin/bash

# File System Security Script
# Ubuntu 24.04 LTS Compatible

LOG_DIR="/var/log/security-reports"
LOG_FILE="$LOG_DIR/filesystem_security.log"

log_action() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

check_root() {
    if [ "$EUID" -ne 0 ]; then
        echo "Run as root."
        exit 1
    fi
}

create_log_directory() {
    mkdir -p "$LOG_DIR"
}

find_suid_files() {

    log_action "Searching for SUID files..."

    find / -perm -4000 -type f 2>/dev/null > "$LOG_DIR/suid_files.txt"

    count=$(wc -l < "$LOG_DIR/suid_files.txt")
    log_action "Total SUID files found: $count"
}

find_world_writable() {

    log_action "Searching for world-writable files..."

    find / \
        -path /tmp -prune -o \
        -path /var/tmp -prune -o \
        -path /proc -prune -o \
        -path /sys -prune -o \
        -perm -002 -type f -print 2>/dev/null > "$LOG_DIR/world_writable_files.txt"

    while read file; do
        chmod o-w "$file"
    done < "$LOG_DIR/world_writable_files.txt"

    count=$(wc -l < "$LOG_DIR/world_writable_files.txt")
    log_action "Removed world-write permission from $count files."
}

secure_temp_directories() {

    log_action "Securing temporary directories..."

    chmod 1777 /tmp
    chmod 1777 /var/tmp

    find /tmp -type f -atime +7 -delete
    find /var/tmp -type f -atime +30 -delete

    log_action "Temporary directories secured."
}

setup_aide() {

    log_action "Installing and initializing AIDE..."

    apt update -y
    apt install -y aide

    aideinit

    if [ -f /var/lib/aide/aide.db.new ]; then
        mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db
        log_action "AIDE database initialized successfully."
    else
        log_action "AIDE initialization failed."
    fi
}

main() {

    check_root
    create_log_directory
    find_suid_files
    find_world_writable
    secure_temp_directories
    setup_aide

    log_action "File system hardening completed."
}

main "$@"
