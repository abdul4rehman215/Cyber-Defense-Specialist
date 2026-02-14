#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

curl -w "\nDNS Lookup: %{time_namelookup}s
TCP Connect: %{time_connect}s
TLS Handshake: %{time_appconnect}s
Server Processing: %{time_starttransfer}s
Total Time: %{time_total}s
Download Size: %{size_download} bytes
HTTP Code: %{http_code}\n" \
-o /dev/null -s "$URL"
