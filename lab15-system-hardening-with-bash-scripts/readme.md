# 🧪 Lab 15 – System Hardening with Bash Scripts

## 📌 Overview

This lab focuses on automating Linux system hardening procedures using Bash scripting on Ubuntu 24.04 LTS.

The objective was to implement practical security controls across:

- System configuration
- User account management
- Firewall configuration (UFW + iptables)
- SSH hardening
- File system security
- Integrity monitoring (AIDE)
- Verification reporting

All hardening actions were implemented through structured, reusable scripts and executed with sudo privileges.

---

## 🎯 Objectives

- Develop automated Bash scripts for Linux hardening
- Enforce password policies and account security
- Configure UFW firewall and advanced iptables protections
- Harden SSH configurations
- Secure file permissions and temporary directories
- Deploy file integrity monitoring (AIDE)
- Generate automated verification reports

---

## 📌 Prerequisites

-	Basic Linux command line operations
- Familiarity with nano
-	Understanding of file permissions and ownership
-	Basic Bash scripting knowledge
-	Access to sudo privileges

---


## 🖥️ Lab Environment

- OS: Ubuntu 24.04 LTS
- User: toor
- EC2 Host: ip-172-31-10-228
- OpenSSH Server installed
- UFW available
- systemd service management enabled
- Full sudo access

---

## 📁 Project Structure

```
system-hardening/
│
├── system_hardening.sh
├── user_security.sh
├── firewall_config.sh
├── iptables_advanced.sh
├── ssh_hardening.sh
├── validate_ssh.sh
├── filesystem_security.sh
├── verify_hardening.sh
│
├── commands.sh
├── output.txt
├── interview_qna.md
├── troubleshooting.md
```


---

## 🔐 Security Controls Implemented

- Password complexity enforcement
- Password aging policy
- Account lockout configuration
- Disabling unnecessary services
- Kernel parameter hardening
- Secure file permissions
- UFW firewall default deny policy
- SSH brute-force protection
- SYN flood protection via iptables
- File integrity monitoring with AIDE
- Automated system verification reporting

---

## ✅ Expected Outcomes

- Hardened Ubuntu 24.04 system
- Firewall active with secure policies
- SSH restricted and validated
- File system secured
- Integrity monitoring initialized
- Verification report generated

---

## 🏁 Conclusion

This lab demonstrates practical Linux system hardening using automation.  
The scripts developed simulate real-world baseline security controls implemented in production Linux servers and cloud environments.

The automation approach ensures consistency, repeatability, and reduced human error during hardening operations.

---
