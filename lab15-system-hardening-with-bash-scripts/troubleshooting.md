# Troubleshooting Guide – Lab 15: System Hardening with Bash Scripts

---

## Issue 1: Script Fails with “Permission Denied”

### Symptoms
- `Permission denied`
- Script does not execute

### Cause
- Script is not executable
- Script is not run with root privileges

### Solution

```bash
chmod +x script_name.sh
sudo ./script_name.sh
````

Verify current user:

```bash
whoami
```

---

## Issue 2: UFW Blocks SSH Connection

### Symptoms

* SSH session disconnects
* Cannot reconnect to server after enabling firewall

### Cause

* SSH port not allowed before enabling UFW
* Default deny policy applied

### Solution

Always allow SSH before enabling UFW:

```bash
sudo ufw allow 22/tcp
sudo ufw enable
```

Best Practice:

* Keep an active SSH session open while testing firewall changes.
* Confirm UFW status:

```bash
sudo ufw status verbose
```

---

## Issue 3: SSH Service Fails to Restart

### Symptoms

* `systemctl restart ssh` fails
* SSH service inactive

### Cause

* Invalid SSH configuration syntax

### Solution

Test configuration before restarting:

```bash
sudo sshd -t
```

If error appears:

* Restore backup:

```bash
sudo cp /etc/ssh/sshd_config.bak /etc/ssh/sshd_config
sudo systemctl restart ssh
```

Check service logs:

```bash
journalctl -xe | grep ssh
```

---

## Issue 4: Account Lockout Module Not Working

### Symptoms

* Failed login attempts do not trigger lockout

### Cause

* PAM module misconfiguration
* Incorrect entry in `/etc/pam.d/common-auth`

### Solution

Verify PAM entry:

```bash
grep pam_tally2 /etc/pam.d/common-auth
```

Correct format:

```
auth required pam_tally2.so deny=3 unlock_time=600 onerr=fail audit even_deny_root
```

---

## Issue 5: iptables Rules Not Persisting After Reboot

### Symptoms

* Firewall rules disappear after system restart

### Cause

* iptables rules not saved persistently

### Solution

Install persistence module:

```bash
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

Verify:

```bash
sudo iptables -L -n -v
```

---

## Issue 6: AIDE Initialization Takes Too Long

### Symptoms

* `aideinit` runs for extended time (10–30+ minutes)

### Cause

* First-time full filesystem scan

### Solution

* Run during maintenance window
* Exclude large directories in AIDE config
* Run in background:

```bash
sudo aideinit &
```

---

## Issue 7: Systemctl Disable Command Fails

### Symptoms

* Service not found
* Unit file missing

### Cause

* Service not installed
* Service name incorrect

### Solution

Check service availability:

```bash
systemctl list-unit-files | grep service_name
```

Skip if service does not exist.

---

## Issue 8: World-Writable Files Keep Reappearing

### Symptoms

* World-writable permissions return after reboot

### Cause

* Application recreates file
* Incorrect default umask

### Solution

Check umask:

```bash
umask
```

Set secure umask in `/etc/profile`:

```
umask 027
```

---

## Issue 9: Locked Out After Disabling PasswordAuthentication

### Symptoms

* SSH access denied after disabling password authentication

### Cause

* SSH keys not configured before disabling passwords

### Solution

Before disabling password authentication:

1. Ensure SSH key is added:

```bash
ssh-copy-id user@server
```

2. Test login via key.
3. Then disable:

```
PasswordAuthentication no
```

---

## Issue 10: Verification Script Shows Unexpected Values

### Symptoms

* Verification report displays incorrect or missing configuration

### Cause

* Configuration file edited manually afterward
* Grep pattern mismatch

### Solution

Manually verify configuration:

```bash
grep PermitRootLogin /etc/ssh/sshd_config
grep minlen /etc/security/pwquality.conf
```

Ensure settings match enforced values.

---

# Security Validation Checklist

After hardening, confirm:

* [ ] SSH root login disabled
* [ ] Password authentication disabled
* [ ] UFW active
* [ ] Default deny incoming
* [ ] Password aging enforced
* [ ] AIDE initialized
* [ ] No world-writable files
* [ ] Unnecessary services disabled
* [ ] Verification report generated

---

# Best Practice Reminder

System hardening should always be:

* Tested in staging before production
* Backed up before changes
* Logged and documented
* Verified after execution
* Monitored continuously

---

# Final Note

Hardening is not a one-time task.
It is an ongoing process that requires:

* Regular patching
* Configuration auditing
* Log monitoring
* Security reviews

