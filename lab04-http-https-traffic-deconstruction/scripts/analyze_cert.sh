#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <hostname>"
    exit 1
fi

HOSTNAME=$1

echo "Analyzing SSL certificate for: $HOSTNAME"
echo "========================================"

echo | openssl s_client -connect ${HOSTNAME}:443 -servername ${HOSTNAME} 2>/dev/null | \
openssl x509 -noout -issuer -subject -dates

echo
echo "TLS Protocol and Cipher:"
echo | openssl s_client -connect ${HOSTNAME}:443 -servername ${HOSTNAME} 2>&1 | \
grep -E "Protocol|Cipher"
