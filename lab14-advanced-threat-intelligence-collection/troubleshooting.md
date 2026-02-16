# 🛠 Troubleshooting Guide - Lab 14 – Advanced Threat Intelligence Collection

---

## 1️⃣ Script Fails with "Configuration file not found"

### Error
```

FileNotFoundError: Configuration file not found: config/sources.json

````

### Cause
The configuration file is either:
- Missing
- Misnamed
- Placed in the wrong directory

### Resolution

Verify file exists:

```bash
ls config/
````

If missing, recreate:

```bash
nano config/sources.json
```

Ensure correct JSON formatting and directory structure.

---

## 2️⃣ JSON Decode Error

### Error

```
json.decoder.JSONDecodeError
```

### Cause

Malformed JSON structure in:

* config/sources.json
* collected_*.json
* normalized_*.json

Common issues:

* Missing comma
* Extra trailing comma
* Incorrect brackets

### Resolution

Validate JSON:

```bash
python3 -m json.tool config/sources.json
```

If no output → JSON valid
If error appears → fix syntax accordingly.

---

## 3️⃣ Permission Denied When Running Script

### Error

```
Permission denied
```

### Cause

Script not executable.

### Resolution

```bash
chmod +x scripts/threat_collector.py
chmod +x scripts/data_normalizer.py
chmod +x scripts/report_generator.py
chmod +x scripts/run_pipeline.sh
```

Alternatively run directly with:

```bash
python3 scripts/threat_collector.py
```

---

## 4️⃣ No Indicators Collected

### Symptom

```
Total Indicators: 0
```

### Possible Causes

* Empty data files
* Invalid IP/domain format
* Incorrect file path in config

### Resolution

Check feed files:

```bash
cat data/malware_domains.txt
cat data/suspicious_ips.txt
```

Verify config paths:

```bash
cat config/sources.json
```

Ensure:

* Correct relative paths
* Proper domain/IP formatting

---

## 5️⃣ Normalizer Fails: "No collected data files found"

### Error

```
FileNotFoundError: No collected data files found in data/
```

### Cause

Collector not executed before normalizer.

### Resolution

Run collection first:

```bash
python3 scripts/threat_collector.py
```

Then run:

```bash
python3 scripts/data_normalizer.py
```

Or use pipeline:

```bash
./scripts/run_pipeline.sh
```

---

## 6️⃣ Duplicate Indicators Not Merging

### Symptom

Unexpected duplicate entries remain.

### Cause

Deduplication key depends on:

```
value + type
```

If:

* Case differences exist
* Whitespace present

Duplicates may not merge.

### Resolution

Ensure inputs are normalized:

* Domains lowercase
* No trailing spaces
* Consistent formatting

---

## 7️⃣ Logging File Not Created

### Symptom

`logs/collection.log` missing.

### Cause

`logs/` directory not present.

### Resolution

Create manually:

```bash
mkdir logs
```

Then rerun collector.

---

## 8️⃣ HTML Report Not Rendering Properly

### Symptom

Browser shows raw text.

### Cause

File opened as text instead of HTML.

### Resolution

Open via browser:

```bash
xdg-open reports/threat_report_*.html
```

Or download and open locally.

---

## 9️⃣ Risk Scores Appear Incorrect

### Observation

All domains show same risk.

### Explanation

Base confidence is fixed at 50 in this lab.
Risk score formula:

```
confidence + type_adjustment
```

So:

* Domain = 50 + 20 = 70
* IP = 50 + 10 = 60

This is expected behavior.

---

## 🔟 Pipeline Stops Mid-Execution

### Cause

One script failed earlier.

### Resolution

Run each stage manually to isolate issue:

```bash
python3 scripts/threat_collector.py
python3 scripts/data_normalizer.py
python3 scripts/report_generator.py
```

Check logs:

```bash
tail -n 20 logs/collection.log
```

---

# 🔎 Validation Checklist

Before concluding lab, verify:

✔ config/sources.json exists
✔ data feed files exist
✔ scripts are executable
✔ collected_*.json created
✔ normalized_*.json created
✔ reports generated in all formats
✔ logs file updated
✔ JSON validates successfully

---

# ⚠ Common Operational Risks

* Unvalidated feeds polluting dataset
* Duplicate entries increasing false positives
* Poor scoring logic leading to alert fatigue
* Lack of automation delaying intelligence cycle

---

# 🏁 Final Operational Status

After validation:

✔ Threat collection functioning
✔ Data normalization verified
✔ Deduplication operational
✔ Severity classification accurate
✔ Multi-format reporting functional
✔ Automated pipeline working end-to-end

System ready for extension into production-grade threat intelligence environment.

precision.
```
