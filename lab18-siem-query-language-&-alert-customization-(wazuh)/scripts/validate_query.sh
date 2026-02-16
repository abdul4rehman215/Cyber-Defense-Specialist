#!/bin/bash

QUERY_FILE=$1

if [ ! -f "$QUERY_FILE" ]; then
    echo "Query file not found: $QUERY_FILE"
    exit 1
fi

# Validate JSON syntax
if ! jq empty "$QUERY_FILE" 2>/dev/null; then
    echo "Invalid JSON syntax in $QUERY_FILE"
    exit 1
fi

# Test query execution
RESULT=$(curl -s -X POST "localhost:9200/wazuh-alerts-*/_search" \
  -H "Content-Type: application/json" \
  -u admin:admin \
  -d @"$QUERY_FILE")

if echo "$RESULT" | jq -e '.error' > /dev/null; then
    echo "Query execution failed:"
    echo "$RESULT" | jq '.error'
    exit 1
else
    echo "Query validation successful for $QUERY_FILE"
    echo "Total hits: $(echo "$RESULT" | jq '.hits.total.value')"
fi
