# 🧪 Lab 16 – Windows Hardening & Active Directory Security

---

## 📌 Lab Summary

This lab implements automated Windows security hardening using PowerShell Core (pwsh 7.4.1) on Ubuntu 24.04.

The lab simulates:
- Active Directory security validation
- Registry hardening checks
- Compliance scoring
- Continuous monitoring
- Enterprise security reporting

All validation logic is configuration-driven using JSON files.

---

## 🎯 Objectives

- Validate AD password and lockout policies
- Audit privileged and disabled accounts
- Perform registry security compliance checks
- Calculate overall security posture score
- Generate JSON and HTML compliance reports

---

## 📌 Prerequisites

- Basic understanding of Windows operating systems and Active Directory concepts
- Familiarity with PowerShell scripting and command-line interfaces
- Knowledge of security principles and Windows registry structure
- Understanding of JSON configuration files

---

## 🖥 Environment

- Ubuntu 24.04 LTS
- PowerShell Core 7.4.1
- Simulated Active Directory
- Simulated Windows Registry
- User: toor
- Host: ip-172-31-10-241

---

## 📁 Project Structure

```

ad-security-lab/
│
├── configs/
│   ├── ad-config.json
│   └── registry/security-registry.json
│
├── scripts/
│   ├── ad-security-automation.ps1
│   ├── registry-hardening.ps1
│   ├── security-monitor.ps1
│   └── generate-report.ps1
│
└── logs/

````

---

## ▶ Execution Order

```bash
pwsh scripts/ad-security-automation.ps1
pwsh scripts/registry-hardening.ps1
pwsh scripts/security-monitor.ps1
pwsh scripts/generate-report.ps1
````

---

## ✅ Expected Output

* AD security log
* Registry compliance report
* Security monitor summary
* Enterprise HTML security report
* Overall compliance score

---

## 🏁 Result

Windows security validation and compliance monitoring successfully automated using PowerShell Core with structured JSON configuration and reporting.


Say **next**.
```
