# 📘 Interview Q&A – Lab 03: Analyzing Network Traffic with Wireshark

---

### Q1. What is the primary purpose of Wireshark in a SOC environment?
**A:** Wireshark is used to capture and analyze network traffic at the packet level, enabling SOC analysts to detect anomalies, investigate incidents, and understand how attacks communicate over the network.

---

### Q2. Why was the user added to the `wireshark` group in this lab?
**A:** Adding the user to the `wireshark` group allows packet capture without running Wireshark as root, improving security while maintaining capture capabilities.

---

### Q3. What role does `dumpcap` play in Wireshark packet capture?
**A:** `dumpcap` is the backend packet capture engine used by Wireshark. Capabilities were set on it to allow packet capture with limited privileges instead of full root access.

---

### Q4. Which network interface was used for traffic capture and why?
**A:** The `ens5` interface was used because it was the active network interface handling live inbound and outbound traffic on the system.

---

### Q5. What is the difference between capture filters and display filters?
**A:** Capture filters limit traffic during packet capture, reducing file size and overhead. Display filters are applied after capture to analyze specific traffic types without discarding packets.

---

### Q6. How was DNS traffic analyzed for suspicious activity?
**A:** DNS traffic was filtered and analyzed for NXDOMAIN responses, suspicious domain names, unusual query patterns, and keyword-based indicators such as malware or phishing terms.

---

### Q7. What indicators were checked to identify potential DNS tunneling?
**A:** Indicators included unusually long domain names, excessive subdomains, abnormal query frequency, and uncommon query types.

---

### Q8. What suspicious behavior was identified in HTTP traffic?
**A:** An unusual User-Agent string (`SuspiciousBot/1.0`) was detected, which could indicate automated scanning or malicious activity.

---

### Q9. Why is TLS traffic analysis important even though payloads are encrypted?
**A:** TLS analysis reveals metadata such as protocol versions, cipher suites, certificate validity, and handshake failures, which helps identify weak encryption or misconfigured services.

---

### Q10. What security issue was observed during TLS analysis?
**A:** A self-signed certificate was detected, which can indicate insecure configurations or potential man-in-the-middle risks if used improperly.

---

### Q11. What is Perfect Forward Secrecy (PFS) and why is it important?
**A:** PFS ensures that session keys are not compromised even if the server’s private key is exposed, enhancing long-term confidentiality of encrypted traffic.

---

### Q12. Why were automation scripts used in this lab?
**A:** Automation scripts improve efficiency, ensure repeatable analysis, reduce human error, and enable faster investigation during real SOC operations.

---

### Q13. How does network traffic analysis support incident response?
**A:** It helps identify attack vectors, understand attacker behavior, trace data exfiltration, and validate containment and remediation actions.

---

### Q14. What SOC-relevant skills were developed in this lab?
**A:** Packet analysis, anomaly detection, protocol inspection, scripting for automation, and security-focused traffic interpretation.

---

### Q15. How does this lab align with real-world SOC workflows?
**A:** The lab mirrors real SOC tasks such as packet capture, traffic filtering, anomaly detection, encrypted traffic inspection, and reporting findings for incident handling.

---
