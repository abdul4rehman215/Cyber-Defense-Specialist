#!/bin/bash

echo "Generating test authentication failure events..."
for i in {1..5}; do
    logger -p auth.info "sshd[1234]: Failed password for user testuser from 192.168.1.100 port 22 ssh2"
    sleep 1
done

echo "Generating test file modification events..."
touch /tmp/test_critical_file
echo "test content" > /tmp/test_critical_file
rm /tmp/test_critical_file

echo "Test events generated successfully"
