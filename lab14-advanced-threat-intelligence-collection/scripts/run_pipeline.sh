#!/bin/bash

echo "Starting Threat Intelligence Pipeline"
echo "======================================"

echo "[1/3] Collecting threat intelligence..."
python3 scripts/threat_collector.py

echo "[2/3] Normalizing data..."
python3 scripts/data_normalizer.py

echo "[3/3] Generating reports..."
python3 scripts/report_generator.py

echo "Pipeline completed successfully!"
echo "Check reports/ directory for output"
