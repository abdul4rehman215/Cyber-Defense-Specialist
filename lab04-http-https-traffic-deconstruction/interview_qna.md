# 📘 Interview Q&A – Lab 4: HTTP/HTTPS Traffic Deconstruction

---

## Q1. Why was a Python HTTP server started on port 8080 in this lab?
**Answer:**  
A local Python HTTP server was started to generate controlled HTTP traffic. This allowed safe capture and analysis of requests without relying on external systems.

---

## Q2. Why was tcpdump used on the loopback interface (lo)?
**Answer:**  
Because both the HTTP client and server were running on the same system, traffic flowed through the loopback interface. Capturing on `lo` ensured all local web traffic was recorded.

---

## Q3. What types of HTTP attacks were intentionally simulated?
**Answer:**  
The lab simulated:
- SQL Injection
- Cross-Site Scripting (XSS)
- Path Traversal
- Suspicious / automated User-Agent behavior

These were generated using crafted curl requests.

---

## Q4. How was captured HTTP traffic converted into a readable format?
**Answer:**  
Using:
- tcpdump -r http_traffic.pcap -A -s 0
This extracted the ASCII payload from packets, making HTTP headers and requests readable.

---

## Q5. What was the purpose of the `http_parser.py` script?
**Answer:**  
The script parsed HTTP requests and automatically detected suspicious patterns such as:
- SQL injection indicators
- XSS payloads
- Path traversal attempts
- Missing or unusual User-Agent headers
- Proxy-related headers

---

## Q6. Which anomalies were successfully detected?
**Answer:**  
The parser identified:
- SQL injection attempts
- Path traversal attempts
- Proxy header usage (X-Forwarded-For)
- Unusual or missing User-Agent strings

---

## Q7. Why was OpenSSL used in HTTPS analysis?
**Answer:**  
OpenSSL was used to:
- Inspect SSL/TLS certificates
- Identify certificate issuer and validity dates
- Determine TLS protocol version
- Identify negotiated cipher suite

This helps evaluate encryption strength and certificate trust.

---

## Q8. What information did the HTTPS timing analysis script provide?
**Answer:**  
The timing script measured:
- DNS lookup time
- TCP connection time
- TLS handshake duration
- Server processing time
- Total request time
- HTTP status code
- Download size

This is useful for performance and anomaly detection.

---

## Q9. What was the goal of the real-time traffic monitoring script?
**Answer:**  
The monitoring script continuously captured live HTTP/HTTPS traffic and scanned for:
- SQL keywords
- Script injection patterns
- Directory traversal attempts

It logged suspicious activity for further review.

---

## Q10. Why is automated alerting important in web traffic monitoring?
**Answer:**  
Automated alerting:
- Reduces manual log review effort
- Speeds up detection time
- Enables faster incident response
- Supports SOC automation workflows

Without alerting, critical web attacks may go unnoticed.

---

## Q11. What is the difference between HTTP and HTTPS from a monitoring perspective?
**Answer:**  
HTTP traffic can be inspected fully (headers + body).  
HTTPS traffic encrypts payload data, so analysis focuses on:
- TLS metadata
- Certificates
- Cipher suites
- Connection behavior
- Timing patterns

---

## Q12. Why is detecting unusual User-Agent strings important?
**Answer:**  
Unusual or automated User-Agent values may indicate:
- Bots
- Vulnerability scanners
- Exploitation tools
- Malware communication

User-Agent inspection is a common SOC detection technique.

---

## Q13. How does path traversal detection improve security monitoring?
**Answer:**  
Path traversal attempts (`../`) indicate attempts to access restricted files such as:
- `/etc/passwd`
- Configuration files
- Application secrets

Detecting them early prevents data exposure.

---

## Q14. How does this lab relate to SOC operations?
**Answer:**  
This lab replicates real SOC activities including:
- Packet capture
- Traffic inspection
- Threat detection
- TLS validation
- Automated monitoring
- Alert generation

These are foundational blue-team skills.

---

# ✅ Key Technical Skills Demonstrated

- Packet-level traffic capture
- HTTP request parsing
- Web attack pattern recognition
- TLS certificate inspection
- Performance timing analysis
- Real-time monitoring automation
- Alert threshold implementation
