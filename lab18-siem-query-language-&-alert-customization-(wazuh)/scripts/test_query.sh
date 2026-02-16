#!/bin/bash

QUERY_FILE=$1

if [ -z "$QUERY_FILE" ]; then
    echo "Usage: $0 <query_file.json>"
    exit 1
fi

if [ ! -f "$QUERY_FILE" ]; then
    echo "Query file not found: $QUERY_FILE"
    exit 1
fi

curl -X POST "localhost:9200/wazuh-alerts-*/_search" \
  -H "Content-Type: application/json" \
  -u admin:admin \
  -d @"$QUERY_FILE" | jq '.'
