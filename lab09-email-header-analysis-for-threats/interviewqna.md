# 📘 Interview Q&A – Lab 09  
## Email Header Analysis for Threats

---

### Q1. What was the primary objective of this lab?

**Answer:**  
The primary objective of this lab was to analyze email headers and detect phishing, spoofing, and authentication failures using SPF, DKIM, and DMARC validation mechanisms. The lab also focused on building an automated threat scoring and reporting system.

---

### Q2. Why are email headers important in digital forensics?

**Answer:**  
Email headers contain metadata about message routing, authentication, sender identity, and originating systems. They allow analysts to:
- Trace message origin
- Identify spoofed domains
- Detect suspicious relay servers
- Investigate phishing campaigns
- Validate authentication mechanisms

Headers are often the first artifact analyzed in email-based incident response.

---

### Q3. How does header_analyzer.py detect spoofing?

**Answer:**  
The script compares:

- **From vs Reply-To**
- **From vs Return-Path**

If the domains differ, it flags possible spoofing. Attackers commonly manipulate Reply-To or Return-Path to redirect responses to malicious domains.

---

### Q4. Why are "Received" headers critical for analysis?

**Answer:**  
Received headers show the email's routing path between mail servers. Analysts can:
- Count hops
- Identify suspicious sending servers
- Detect known malicious IP ranges
- Identify compromised infrastructure

In this lab, IP ranges starting with `203.` and `198.` were flagged as suspicious indicators.

---

### Q5. How does SPF validation work in this lab?

**Answer:**  
SPF validation:
1. Queries DNS TXT records for the sender domain.
2. Extracts the `v=spf1` record.
3. Parses IP mechanisms (`ip4:` entries).
4. Checks if the sender IP is authorized.

If no valid record is found, the result returns "None".

---

### Q6. What is the purpose of DKIM in email security?

**Answer:**  
DKIM ensures message integrity by:
- Signing email content with a private key
- Publishing a public key in DNS
- Allowing receivers to verify that content was not modified

In this lab, DKIM validation checked for:
- Presence of DKIM-Signature header
- Valid selector and domain
- Public key availability in DNS

---

### Q7. What does DMARC enforce?

**Answer:**  
DMARC enforces policy alignment between SPF and DKIM. It defines actions:

- `none` → Monitor only
- `quarantine` → Mark as suspicious
- `reject` → Block email

DMARC ensures domain alignment and protects against spoofing attacks.

---

### Q8. Why did the legitimate email still show LOW risk?

**Answer:**  
Although header indicators were clean, the absence of verified SPF/DKIM records increased the overall risk score slightly. The scoring engine adds small penalty points for missing authentication validation.

---

### Q9. How was the final threat score calculated?

**Answer:**  
Threat score combined:

- Spoofing indicators (×3 weight)
- Suspicious subject keywords (×2 weight)
- Suspicious IPs (×4 weight)
- SPF failure penalty
- DKIM failure penalty
- DMARC enforcement penalty

Final risk levels:
- 0 → MINIMAL
- 1–7 → LOW
- 8–14 → MEDIUM
- 15+ → HIGH

---

### Q10. Why is automated threat scoring useful in a SOC?

**Answer:**  
Automated scoring:

- Speeds up email triage
- Prioritizes high-risk threats
- Reduces analyst fatigue
- Standardizes decision-making
- Integrates easily into SIEM pipelines
- Improves incident response time

---

### Q11. What are common phishing indicators visible in headers?

**Answer:**
- From/Reply-To mismatch
- Suspicious originating IP
- Bulk mailer indicators (X-Mailer headers)
- Urgent or coercive subject lines
- Executable attachments
- Return-Path mismatch

---

### Q12. Why is SPF alone insufficient for security?

**Answer:**  
SPF only validates sending IP authorization. It does not:
- Protect against message tampering
- Ensure domain alignment
- Prevent display-name spoofing

That is why SPF must be combined with DKIM and DMARC.

---

### Q13. How can this system be improved for enterprise use?

**Answer:**
- Integrate with real-time DNS validation
- Add reputation scoring (IP/domain intelligence)
- Integrate VirusTotal API
- Add attachment sandboxing
- Implement full DKIM cryptographic verification
- Connect to SIEM for automated alerts

---

### Q14. What is the key security lesson from this lab?

**Answer:**  
Email security must be layered:

- Header analysis
- Authentication validation
- Threat scoring
- Policy enforcement
- Automated reporting

No single mechanism is sufficient alone.

---

