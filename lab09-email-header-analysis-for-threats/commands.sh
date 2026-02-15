#!/bin/bash

# Create lab directory structure
mkdir -p ~/email_lab/{samples,scripts,output}
cd ~/email_lab

# Verify Python version
python3 --version

# Upgrade pip
pip3 install --upgrade pip

# Install required libraries
pip3 install dnspython email-validator

# Create sample email headers
nano samples/legitimate.eml
nano samples/phishing.eml
nano samples/malware.eml

# Verify sample files
ls -lh samples/

# Create header analyzer script
nano scripts/header_analyzer.py
chmod +x scripts/header_analyzer.py

# Run header analyzer
python3 scripts/header_analyzer.py

# Create SPF validator
nano scripts/spf_validator.py
chmod +x scripts/spf_validator.py

# Run SPF validator
python3 scripts/spf_validator.py

# Create DKIM validator
nano scripts/dkim_validator.py
chmod +x scripts/dkim_validator.py

# Run DKIM validator
python3 scripts/dkim_validator.py

# Create DMARC validator
nano scripts/dmarc_validator.py
chmod +x scripts/dmarc_validator.py

# Run DMARC validator
python3 scripts/dmarc_validator.py

# Create integrated threat reporter
nano scripts/threat_reporter.py
chmod +x scripts/threat_reporter.py

# Run final integrated test
python3 scripts/threat_reporter.py

# Verify generated reports
ls -lh output/

# View example JSON report
cat output/legitimate.eml.json

# Troubleshooting DNS resolution
ping 8.8.8.8
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf

# Fix permission issues
chmod +x scripts/*.py
chmod 644 samples/*.eml
