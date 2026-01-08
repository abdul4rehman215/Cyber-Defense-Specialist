#!/bin/bash
# ============================================================
# Script: generate_auth_events.sh
# Purpose: Generate authentication-related security events
# ============================================================

echo "[+] Generating authentication failures..."

for i in {1..5}; do
  echo "invalid_password" | su - nonexistent_user 2>/dev/null || true
  sleep 2
done

echo "[+] Authentication failure events generated"
