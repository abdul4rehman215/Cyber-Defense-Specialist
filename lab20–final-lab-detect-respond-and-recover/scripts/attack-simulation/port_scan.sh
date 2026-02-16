#!/bin/bash

TARGET="127.0.0.1"

echo "======================================"
echo " Simulating Port Scan"
echo " Target: $TARGET"
echo "======================================"

for port in {20..100}; do
    echo "Scanning port $port"
    timeout 1 bash -c "echo >/dev/tcp/$TARGET/$port" 2>/dev/null
done

echo "======================================"
echo " Port Scan Simulation Complete"
echo "======================================"
