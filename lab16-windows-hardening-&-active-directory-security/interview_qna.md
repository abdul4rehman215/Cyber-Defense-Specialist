# 📘 Interview Q&A – Lab 16  
Windows Hardening & Active Directory Security (PowerShell)

---

## Q1. What was the primary objective of this lab?

**Answer:**  
To automate Windows security hardening and Active Directory security validation using PowerShell Core on Ubuntu 24.04.

---

## Q2. Why was PowerShell Core used on Ubuntu?

**Answer:**  
PowerShell Core (pwsh 7.4.1) allows cross-platform scripting and enables simulation of Windows security automation from a Linux environment.

---

## Q3. What Active Directory policies were validated?

**Answer:**
- Password Policy (minimum length, complexity, max age)
- Account Lockout Policy (threshold, duration, reset counter)

---

## Q4. How were user accounts audited?

**Answer:**  
The script analyzed the JSON configuration and calculated:
- Number of disabled accounts
- Number of admin accounts
- Number of service accounts

---

## Q5. What registry settings were validated?

**Answer:**
- LimitBlankPasswordUse
- NoLMHash
- EnableLUA (User Account Control)
- ConsentPromptBehaviorAdmin

These simulate critical Windows security registry controls.

---

## Q6. How was registry compliance calculated?

**Answer:**  
The script compared expected registry values with simulated current values and calculated a compliance percentage based on total checks.

---

## Q7. What does the security-monitor.ps1 script do?

**Answer:**  
It combines:
- AD security score
- Registry compliance score  
And calculates an overall security posture score.

---

## Q8. How is the overall security score determined?

**Answer:**  
It averages:
- Active Directory security score
- Registry compliance percentage

---

## Q9. What types of reports were generated?

**Answer:**
- JSON security summary
- Registry compliance report
- Security monitoring summary
- Enterprise-level HTML security report

---

## Q10. Why is automation important in enterprise security?

**Answer:**  
Automation:
- Reduces human error
- Ensures consistent policy validation
- Enables continuous compliance monitoring
- Supports audit documentation
- Improves enterprise security posture management
