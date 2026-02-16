# 🧪 Lab 16 – Windows Hardening & Active Directory Security  
(PowerShell Automation on Ubuntu 24.04)

---

## 📌 Overview

This lab demonstrates automated Windows security hardening and Active Directory validation using PowerShell Core (pwsh 7.4.1) on Ubuntu 24.04.

A simulated Active Directory and Windows Registry environment was used to implement enterprise-style security validation, compliance scoring, and reporting automation.

The lab focuses on structured security validation driven by JSON configuration files.

---

## 🎯 Objectives

- Validate Active Directory password and lockout policies
- Audit privileged, disabled, and service accounts
- Perform registry security compliance checks
- Calculate overall enterprise security score
- Generate JSON and HTML compliance reports
- Create remediation templates for security findings

---

## 📌 Prerequisites

- Basic understanding of Windows OS and Active Directory
- Familiarity with PowerShell scripting
- Knowledge of Windows registry structure
- Understanding of JSON configuration files

---

## 🖥 Lab Environment

- Ubuntu 24.04 LTS
- PowerShell Core 7.4.1
- Simulated Active Directory environment
- Simulated Windows Registry
- User: `toor`
- Host: `ip-172-31-10-241`

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

## ▶ Execution Workflow

```bash
pwsh scripts/ad-security-automation.ps1
pwsh scripts/registry-hardening.ps1
pwsh scripts/security-monitor.ps1
pwsh scripts/generate-report.ps1
````

---

## ✅ Expected Outcomes

After successful execution, the lab produces:

* Active Directory security validation
* Registry compliance assessment
* Automated compliance scoring
* Continuous monitoring summary
* Enterprise-style HTML security report
* Remediation recommendations

The `logs/` directory contains:

* `ad-security.log`
* `security-summary.json`
* `registry-hardening.log`
* `registry-hardening-report.json`
* `security-monitor-summary.json`
* `security-report.html`

---

## 🧠 Skills Developed

* PowerShell security automation
* Active Directory policy validation
* Registry hardening simulation
* Compliance percentage calculation
* Enterprise security monitoring logic
* Structured security reporting

---

## 🏁 Conclusion

This lab successfully implemented Windows security hardening automation using PowerShell Core on Ubuntu 24.04.

Security controls validated include:

* Active Directory password and lockout policies
* Privileged account auditing
* Critical registry security settings
* Compliance scoring and monitoring
* Automated enterprise reporting

The automation framework built in this lab demonstrates scalable and structured security validation techniques that can be adapted to real-world Active Directory and Windows enterprise environments.
