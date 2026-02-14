# 🛠 Troubleshooting - Lab 7: MITRE ATT&CK Mapping for Incident Detection

<br>

### Issue 1: MITRE ATT&CK JSON File Not Downloading

#### Symptoms

* `wget` fails
* File size is 0 KB
* JSON parsing errors occur later

#### Solution

```
wget https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json -O data/enterprise-attack.json
```

Verify file integrity:

```
ls -lh data/enterprise-attack.json
```

Validate JSON structure:

```
python3 -m json.tool data/enterprise-attack.json > /dev/null
```

If errors occur:

* Check internet connectivity
* Re-download file
* Ensure file encoding is UTF-8

---

### Issue 2: Python Module Import Error (mitre_parser not found)

#### Symptoms

`
ModuleNotFoundError: No module named 'mitre_parser'
`

#### Solution

Ensure you are running scripts from the correct directory:

```
cd ~/mitre-lab/scripts
python3 log_analyzer.py
```

Or adjust Python path:

```
export PYTHONPATH=$PYTHONPATH:$(pwd)
```

---

### Issue 3: Required Python Libraries Missing

#### Symptoms

`
ModuleNotFoundError: No module named 'stix2'
`

#### Solution

Install required packages:

```
pip3 install requests pandas stix2 pyyaml
```

If permission errors occur:

```
pip3 install --user requests pandas stix2 pyyaml
```

---

### Issue 4: No Techniques Loaded

#### Symptoms

`
Loaded 0 techniques
`

#### Possible Causes

* Incorrect JSON file path
* Corrupted JSON file
* Missing "mitre-attack" external references

#### Solution

Check JSON file path inside `mitre_parser.py`:

```python
json_file_path="../data/enterprise-attack.json"
```

Confirm file exists:

```
ls ../data/
```

Re-download file if needed.

---

### Issue 5: No Findings in analysis_report.json

#### Symptoms

`
Total Findings: 0
`

#### Causes

* Regex patterns not matching
* Log file path incorrect
* Case sensitivity issues

#### Solutions

Verify log file paths:

```
ls ../logs/
```

Test regex patterns manually:

```
grep -i powershell ../logs/windows_security.log
grep -i mimikatz ../logs/windows_security.log
```

Adjust regex if necessary.

---

### Issue 6: Missing Technique Name in Findings

#### Symptoms

`
NoneType error when accessing technique name
`

#### Cause

Technique ID not found in parsed MITRE dataset.

#### Solution

Verify technique exists:

```
parser.get_technique_by_id("T1059.001")
```

Confirm correct technique ID format:
```
T#### or T####.###
```
---

### Issue 7: JSON Report Not Generated

#### Symptoms

* `analysis_report.json` not found
* `incident_report.json` missing

#### Solution

Ensure script executed successfully:

```
python3 log_analyzer.py
python3 auto_mapper.py
```

Check reports directory:

```
ls -lh ../reports/
```

Confirm write permissions:

```
chmod -R 755 ../reports
```

---

### Issue 8: Tree Command Not Found

#### Symptoms

`
tree: command not found
`

#### Solution

Install tree utility:

```
sudo apt update
sudo apt install tree
```

---

### Issue 9: Encoding or JSON Decode Errors

#### Symptoms

`
UnicodeDecodeError
JSONDecodeError
`

#### Solution

Open file with explicit encoding:

```
with open(self.json_file_path, "r", encoding="utf-8") as f:
```

Validate JSON again:

```
python3 -m json.tool data/enterprise-attack.json
```

---

### Issue 10: Regex Not Detecting Multi-Word Patterns

#### Symptoms

Expected matches not appearing.

#### Solution

Test regex in Python interactive mode:

```
python3
>>> import re
>>> re.search(r"powershell.*-enc", "powershell.exe -enc SQBuAHYAbwBrAGUA")
```

Refine regex if necessary.

---

# ✅ Validation Checklist

Before completing the lab, verify:

* MITRE ATT&CK JSON file downloaded correctly
* Techniques and tactics loaded successfully
* Log analyzer produces findings
* Incident report generated
* JSON reports properly structured
* Regex detection rules functioning
* No Python runtime errors

---

# 🔐 Best Practice Notes

* Always validate external data sources.
* Keep detection rules updated with evolving MITRE techniques.
* Test regex patterns before deployment.
* Maintain proper directory structure.
* Use structured JSON reports for integration with SIEM systems.
