# 📘 Interview Q&A – Lab 18: SIEM Query Language & Alert Customization

---

## Q1. What is the purpose of Wazuh Query Language?

Wazuh Query Language (Elasticsearch DSL based) is used to search, filter, and analyze security events stored in Wazuh indices. It enables detection of authentication attacks, file integrity violations, and network anomalies.

---

## Q2. What does the bool + must clause do?

The `bool` query combines multiple conditions.

The `must` clause ensures all specified conditions must match for results to be returned.

---

## Q3. How can brute force attacks be detected using queries?

By filtering authentication_failed events within a short time window and aggregating by source IP to identify repeated attempts.

---

## Q4. Why use .keyword fields?

`.keyword` fields allow exact matching and aggregation.  
They improve performance and accuracy when grouping IP addresses or usernames.

---

## Q5. How do you validate a Wazuh query?

1. Validate JSON syntax:
   jq empty query.json

2. Execute using curl

3. Check for `.error` in response

---

## Q6. Why use custom rule IDs like 100001?

Custom rule IDs:
- Separate organization rules from default ones
- Enable custom severity assignment
- Allow automation triggers
- Improve maintainability

---

## Q7. How are custom rules loaded?

1. Place XML in:
   /var/ossec/etc/rules/custom/

2. Include in ossec.conf

3. Validate with:
   sudo /var/ossec/bin/wazuh-logtest -t

4. Restart wazuh-manager

---

## Q8. How was alert automation implemented?

Using:
- monitor_alerts.sh
- process_alerts.sh
- alert_response.sh

Alerts trigger simulated IP blocking and logging.

---

## Q9. How was query performance optimized?

- Used filter instead of must
- Used size: 0 for aggregation-only queries
- Used .keyword fields
- Limited time range

Result: ~43% performance improvement.

---

## Q10. Why is SIEM customization important?

Because default rules:
- May miss organization-specific threats
- Generate false positives
- Cannot automate responses

Customization enables:
- Faster detection
- Reduced alert fatigue
- Automated SOC workflows
- Better performance
