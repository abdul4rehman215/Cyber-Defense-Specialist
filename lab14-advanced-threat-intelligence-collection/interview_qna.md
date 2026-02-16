# 📘 Interview Q&A - Lab 14 – Advanced Threat Intelligence Collection

---

### Q1. What was the primary objective of this lab?

**Answer:**  
The primary objective was to design and implement a complete automated Threat Intelligence pipeline.  
This included:

- Collecting threat indicators from multiple sources
- Validating indicators (IP addresses, domains, hashes)
- Enriching and assigning risk scores
- Normalizing data into a standardized structure
- Deduplicating indicators
- Generating multi-format intelligence reports
- Automating the workflow using a pipeline script

The lab simulates a foundational SOC-level Threat Intelligence processing system.

---

### Q2. Why is indicator validation critical in threat intelligence systems?

**Answer:**  
Indicator validation ensures:

- Data integrity
- Removal of malformed entries
- Reduction of false positives
- Improved reliability of downstream analysis

For example:
- Invalid IP formats must not enter correlation engines.
- Incorrect domains may break enrichment logic.
- Invalid hashes reduce trust in malware intelligence feeds.

Proper validation prevents polluted intelligence datasets.

---

### Q3. How were IP addresses validated in this implementation?

**Answer:**  
IP validation was performed using Python’s built-in `ipaddress` module:

```python
ipaddress.ip_address(ip_string.strip())
````

This method:

* Validates IPv4 and IPv6
* Raises a `ValueError` if invalid
* Ensures only properly formatted addresses are processed

Using a standard library avoids writing unreliable regex-based validation.

---

### Q4. How does the domain validation logic work?

**Answer:**
Domain validation uses a structured regular expression:

```python
pattern = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$"
```

This ensures:

* No leading/trailing hyphens
* Valid character sets
* Proper TLD format
* Minimum structure requirements

It prevents malformed or incomplete domain indicators from entering the system.

---

### Q5. How does the system determine hash type?

**Answer:**
Hash type is determined based on length and hexadecimal validation:

| Length | Hash Type |
| ------ | --------- |
| 32     | MD5       |
| 40     | SHA1      |
| 64     | SHA256    |

The script first validates hexadecimal format using regex, then determines the type by checking the string length.

---

### Q6. How is risk scoring calculated?

**Answer:**
Risk scoring starts with a base confidence value (default: 50).
The score is adjusted based on indicator type:

* IP → +10
* Domain → +20
* Hash → +30

Example:

* Domain: 50 + 20 = 70
* IP: 50 + 10 = 60

Scores are bounded between 0 and 100.

This provides a simple but scalable scoring model.

---

### Q7. What is the purpose of data normalization?

**Answer:**
Normalization ensures:

* Consistent field structure
* Standardized confidence values (0–100 scale)
* Standard severity classification
* Unified tagging format
* Removal of duplicates

It transforms raw intelligence into SOC-ready structured data.

---

### Q8. How are duplicates handled?

**Answer:**
Deduplication is performed using a composite key:

```
value + type
```

If duplicates are found:

* The indicator with higher confidence is kept.
* Tags are merged.
* Duplicate counter increases.

This ensures clean intelligence datasets.

---

### Q9. How is severity determined from risk score?

**Answer:**

| Risk Score | Severity |
| ---------- | -------- |
| ≥ 80       | HIGH     |
| ≥ 60       | MEDIUM   |
| ≥ 40       | LOW      |
| < 40       | INFO     |

This classification allows SOC teams to prioritize investigation efforts.

---

### Q10. What reporting formats were generated?

**Answer:**

The system generates:

* `.txt` – Human-readable executive summary
* `.html` – Web-viewable formatted report
* `.json` – Structured machine-readable intelligence

This supports:

* Analysts
* Managers
* Automated systems

---

### Q11. What is the purpose of the automated pipeline script?

**Answer:**
The `run_pipeline.sh` script orchestrates:

1. Collection
2. Normalization
3. Report generation

This simulates real-world SOC automation where intelligence ingestion runs on scheduled jobs or cron tasks.

It reduces manual intervention and improves operational efficiency.

---

### Q12. How could this system be extended for production use?

**Answer:**
Possible production enhancements:

* Integration with VirusTotal and AbuseIPDB APIs
* Database storage (PostgreSQL / Elasticsearch)
* Real-time alerting for HIGH severity indicators
* Dashboard visualization (Kibana / Grafana)
* Indicator correlation engine
* STIX/TAXII integration
* Threat feed ingestion automation

This lab provides the architectural foundation for a scalable Threat Intelligence platform.

---

### Q13. What cybersecurity skills were developed in this lab?

**Answer:**

* Threat indicator validation
* Risk scoring methodology
* Data normalization techniques
* Deduplication strategies
* SOC workflow automation
* Multi-format reporting
* Secure scripting practices
* Structured logging
* JSON data processing

These skills are directly applicable in SOC, Blue Team, and Threat Intelligence Analyst roles.

---

### Q14. What real-world role does this lab simulate?

**Answer:**
This lab simulates responsibilities of:

* Threat Intelligence Analyst
* SOC Automation Engineer
* Blue Team Security Engineer
* Cybersecurity Data Engineer

It demonstrates the ability to build automated security pipelines from scratch.
