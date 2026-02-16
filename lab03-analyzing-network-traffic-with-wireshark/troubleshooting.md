# 🛠️ Troubleshooting – Lab 03: Analyzing Network Traffic with Wireshark

This document covers common issues encountered while installing, capturing, and analyzing network traffic using Wireshark and tshark on Linux systems.

---

## Issue 1: Permission Denied When Capturing Packets

### Symptoms
- Wireshark shows no interfaces
- tshark returns permission denied
- Capture fails for non-root user

### Resolution
Ensure the user is part of the `wireshark` group and dumpcap has proper capabilities.

```bash
sudo usermod -a -G wireshark $USER
newgrp wireshark
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
getcap /usr/bin/dumpcap
````

If changes do not apply immediately, log out and log back in.

---

## Issue 2: No Network Interfaces Visible in Wireshark

### Symptoms

* Wireshark GUI shows no capture interfaces
* tshark -D returns empty list

### Resolution

Verify interface status and availability.

```bash
ip link show
sudo ip link set ens5 up
tshark -D
```

Ensure the interface is not disabled or managed by restrictive network policies.

---

## Issue 3: Packet Capture Files Are Empty

### Symptoms

* `.pcap` files exist but contain no packets
* Analysis scripts return no results

### Resolution

Confirm active network traffic and sufficient permissions.

```bash
ping -c 5 google.com
curl http://httpbin.org/get
ls -lh /tmp/*.pcap
```

Run tshark in verbose mode for debugging:

```bash
sudo tshark -i ens5 -v -c 10
```

---

## Issue 4: tshark or Wireshark Not Installed Correctly

### Symptoms

* Command not found errors
* Scripts fail due to missing tshark

### Resolution

Verify installation and reinstall if needed.

```bash
which wireshark
which tshark
sudo apt install --reinstall wireshark tshark
```

---

## Issue 5: DNS Analysis Scripts Return No Results

### Symptoms

* DNS scripts show empty output
* No suspicious domains detected

### Resolution

Confirm DNS capture file exists and contains DNS packets.

```bash
ls -la /tmp/dns_traffic.pcap
tshark -r /tmp/dns_traffic.pcap -Y dns | head
```

Ensure DNS traffic was generated during capture.

This may be normal if no malicious or unusual traffic occurred.

---

## Issue 6: HTTP Analysis Shows Limited Data

### Symptoms

* Few HTTP requests detected
* Missing User-Agent fields

### Resolution

Confirm HTTP traffic was generated during capture.

```bash
curl http://httpbin.org/get
curl -H "User-Agent: TestAgent" http://httpbin.org/user-agent
```

Re-run capture if necessary:

```bash
sudo tshark -i ens5 -f "port 80" -w /tmp/http_analysis.pcap
```

---

## Issue 7: TLS Analysis Does Not Show Certificates or Ciphers

### Symptoms

* TLS scripts show empty certificate or cipher output

### Resolution

Ensure TLS handshake packets are captured.

```bash
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake"
```

TLS payloads are encrypted, but handshake metadata must be present.

---

## Issue 8: Analysis Scripts Fail to Execute

### Symptoms

* Permission denied errors
* Script exits immediately

### Resolution

Ensure scripts are executable and run with correct interpreter.

```bash
chmod +x /tmp/analyze_*.sh
bash -x /tmp/analyze_dns.sh
```

Check for missing files or incorrect paths.

---

## Issue 9: High CPU Usage During Capture

### Symptoms

* System slows down
* tshark consumes high CPU

### Resolution

Limit packet count and scope of capture.

```bash
sudo tshark -i ens5 -c 100
```

Use capture filters to reduce load:

```bash
sudo tshark -i ens5 -f "port 53"
```

---

## Issue 10: Wireshark GUI Fails to Launch

### Symptoms

* Wireshark does not open
* X11 or display errors

### Resolution

Use tshark for CLI-based analysis or verify GUI support.

```bash
wireshark --version
echo $DISPLAY
```

For headless systems, rely on tshark and exported `.pcap` files.

---

## Final Notes

* Not all labs will generate malicious traffic; absence of alerts can still indicate correct configuration
* Packet-level analysis is context-dependent and should be combined with SIEM and endpoint logs
* Automated scripts enhance repeatability but should always be validated manually

---
