# Interview Q&A – Lab 15: System Hardening with Bash Scripts

---

## Q1. What was the primary objective of this lab?

**Answer:**  
The primary objective was to automate Linux system hardening using Bash scripts on Ubuntu 24.04. The lab focused on implementing security best practices such as password policies, firewall configuration, SSH hardening, file system protection, and automated verification.

---

## Q2. Why must hardening scripts be executed with root privileges?

**Answer:**  
Hardening tasks involve modifying critical system files such as:

- `/etc/ssh/sshd_config`
- `/etc/login.defs`
- `/etc/security/pwquality.conf`
- Firewall rules (UFW / iptables)
- System services via `systemctl`

These operations require elevated privileges (sudo/root) to prevent unauthorized modifications and maintain system integrity.

---

## Q3. What password policies were enforced?

**Answer:**

- Minimum password length: **12 characters**
- Minimum character classes: **3**
- Maximum password age: **90 days**
- Minimum password age: **7 days**
- Account lockout after **3 failed attempts**
- Unlock time: **600 seconds**

This enforces strong authentication standards and reduces brute-force risk.

---

## Q4. How were unnecessary services secured?

**Answer:**  
Services such as:

- `avahi-daemon`
- `cups`
- `bluetooth`

were disabled and stopped using:

```bash
systemctl disable service_name
systemctl stop service_name
````

Reducing active services minimizes attack surface.

---

## Q5. What were the default UFW firewall policies configured?

**Answer:**

* Default incoming: **deny**
* Default outgoing: **allow**
* Default forward: **deny**

This follows the **default-deny principle** — only explicitly allowed traffic is permitted.

---

## Q6. How was brute-force protection implemented for SSH?

**Answer:**

* Disabled root login
* Disabled password authentication
* Limited authentication attempts to 3
* Enabled UFW rate limiting (`ufw limit ssh`)
* Enforced Protocol 2
* Set client alive intervals

These controls significantly reduce brute-force and credential-stuffing attacks.

---

## Q7. How was SYN flood protection implemented?

**Answer:**

Using iptables rate limiting:

```bash
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP
```

This limits excessive SYN packets and mitigates TCP-based denial-of-service attacks.

---

## Q8. What is the purpose of AIDE in system hardening?

**Answer:**
AIDE (Advanced Intrusion Detection Environment) provides:

* File integrity monitoring
* Detection of unauthorized file modifications
* Hash-based verification of system files

It helps detect post-compromise changes and insider threats.

---

## Q9. Why is file permission hardening important?

**Answer:**
Incorrect permissions may allow:

* Privilege escalation
* Unauthorized data access
* Malware persistence

The lab secured:

* `/etc/shadow` → 600
* `/root` → 700
* Removed world-writable permissions
* Identified SUID binaries

---

## Q10. How was system hardening verified?

**Answer:**
A dedicated verification script checked:

* Password policy settings
* Firewall status
* SSH configuration values
* Disabled services
* SSH service status

A complete report was generated at:

```
/var/log/hardening_report.txt
```

---

## Q11. What security principles were applied in this lab?

**Answer:**

* Least privilege
* Defense-in-depth
* Secure-by-default configuration
* Automation for consistency
* Attack surface reduction
* Configuration validation

---

## Q12. How can this hardening framework be extended in production?

**Answer:**

* Integrate with Ansible for fleet-wide deployment
* Add auditd rule enforcement
* Enable centralized logging (SIEM integration)
* Implement CIS benchmark validation
* Automate compliance scanning with OpenSCAP
* Add alerting for configuration drift

---

## Q13. What are common risks when hardening SSH?

**Answer:**

* Locking yourself out by disabling password authentication before configuring SSH keys
* Blocking port 22 before confirming firewall rules
* Restarting SSH without testing configuration (`sshd -t`)

Always keep an active SSH session open during changes.

---

## Q14. Why is automation critical in system hardening?

**Answer:**

Manual configuration:

* Is error-prone
* Inconsistent across systems
* Difficult to audit

Automation ensures:

* Repeatability
* Scalability
* Faster deployment
* Compliance enforcement

---

# Key Takeaway

This lab demonstrates practical SOC-level system hardening automation aligned with enterprise security standards. The scripts provide a reusable baseline framework for production Linux security hardening.
