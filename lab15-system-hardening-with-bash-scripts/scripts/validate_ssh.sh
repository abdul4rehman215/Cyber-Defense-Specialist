#!/bin/bash

# SSH Configuration Validator

check_ssh_setting() {
    local setting=$1
    local expected=$2

    actual=$(grep -i "^$setting" /etc/ssh/sshd_config | awk '{print $2}')

    if [ "$actual" == "$expected" ]; then
        echo "[PASS] $setting is set to $expected"
    else
        echo "[FAIL] $setting is $actual (Expected: $expected)"
    fi
}

main() {

    echo "Validating SSH Configuration..."

    check_ssh_setting "PermitRootLogin" "no"
    check_ssh_setting "PasswordAuthentication" "no"
    check_ssh_setting "MaxAuthTries" "3"
    check_ssh_setting "PermitEmptyPasswords" "no"
    check_ssh_setting "ClientAliveInterval" "300"
    check_ssh_setting "ClientAliveCountMax" "2"
    check_ssh_setting "Protocol" "2"
}

main "$@"
