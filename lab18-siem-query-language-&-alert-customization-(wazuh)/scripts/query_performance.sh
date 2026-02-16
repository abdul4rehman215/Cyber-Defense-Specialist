#!/bin/bash

QUERY_FILE=$1
ITERATIONS=${2:-5}

if [ -z "$QUERY_FILE" ]; then
    echo "Usage: $0 <query_file.json> [iterations]"
    exit 1
fi

if [ ! -f "$QUERY_FILE" ]; then
    echo "Query file not found: $QUERY_FILE"
    exit 1
fi

echo "Testing query performance for: $QUERY_FILE"
echo "Iterations: $ITERATIONS"

total_time=0

for i in $(seq 1 $ITERATIONS); do
    start_time=$(date +%s.%N)

    curl -s -X POST "localhost:9200/wazuh-alerts-*/_search" \
      -H "Content-Type: application/json" \
      -u admin:admin \
      -d @"$QUERY_FILE" > /dev/null

    end_time=$(date +%s.%N)

    execution_time=$(echo "$end_time - $start_time" | bc)
    total_time=$(echo "$total_time + $execution_time" | bc)

    echo "Iteration $i: ${execution_time}s"
done

average_time=$(echo "scale=3; $total_time / $ITERATIONS" | bc)

echo "Average execution time: ${average_time}s"
