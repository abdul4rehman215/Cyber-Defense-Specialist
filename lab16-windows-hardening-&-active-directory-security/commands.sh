#!/bin/bash
# Lab 16 – Commands Executed
# Windows Hardening & Active Directory Security (PowerShell on Ubuntu 24.04)

# Verify PowerShell installation
pwsh --version

# Create project structure
mkdir -p ~/ad-security-lab/{scripts,configs,logs}
cd ~/ad-security-lab
ls

# Create AD configuration file
nano configs/ad-config.json

# Create AD security automation script
nano scripts/ad-security-automation.ps1

# Make script executable
chmod +x scripts/ad-security-automation.ps1

# Execute AD security automation
pwsh scripts/ad-security-automation.ps1

# Check AD security log
cat logs/ad-security.log

# Check AD security summary
cat logs/security-summary.json

# Create registry configuration directory
mkdir -p configs/registry

# Create registry configuration file
nano configs/registry/security-registry.json

# Create registry hardening script
nano scripts/registry-hardening.ps1

# Make registry script executable
chmod +x scripts/registry-hardening.ps1

# Execute registry hardening
pwsh scripts/registry-hardening.ps1

# Review registry hardening log
cat logs/registry-hardening.log

# Review registry compliance report
cat logs/registry-hardening-report.json

# Create security monitoring script
nano scripts/security-monitor.ps1

# Make monitoring script executable
chmod +x scripts/security-monitor.ps1

# Execute monitoring
pwsh scripts/security-monitor.ps1

# Create HTML report generator
nano scripts/generate-report.ps1

# Make report generator executable
chmod +x scripts/generate-report.ps1

# Generate HTML report
pwsh scripts/generate-report.ps1

# Execute full validation cycle again
pwsh scripts/ad-security-automation.ps1
pwsh scripts/registry-hardening.ps1
pwsh scripts/security-monitor.ps1
pwsh scripts/generate-report.ps1

# View final HTML report
cat logs/security-report.html
