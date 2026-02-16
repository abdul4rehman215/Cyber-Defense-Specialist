#!/bin/bash

TARGET="localhost"
ATTEMPTS=10

echo "======================================"
echo " Simulating SSH Brute Force Attack"
echo " Target: $TARGET"
echo " Attempts: $ATTEMPTS"
echo "======================================"

for i in $(seq 1 $ATTEMPTS); do
    echo "[Attempt $i] Trying invalid credentials..."
    sshpass -p "wrongpassword" ssh \
        -o StrictHostKeyChecking=no \
        -o ConnectTimeout=3 \
        testuser@$TARGET 2>/dev/null

    sleep 1
done

echo "======================================"
echo " SSH Brute Force Simulation Complete"
echo "======================================"
