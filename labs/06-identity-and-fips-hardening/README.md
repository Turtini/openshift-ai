# Lab 06: Identity Integration and FIPS Hardening (Optional)

## Objective

In this lab, you will explore **enterprise identity integration** and **FIPS enablement**
patterns commonly required in U.S. federal environments.

By the end of this lab, you will understand how to:

- Enable FIPS mode on RHEL systems
- Integrate RHEL hosts with Active Directory using SSSD
- Migrate from Centrify-based identity integration to SSSD
- Validate cryptographic and identity behavior under FIPS constraints

This lab is **optional** and intended for regulated environments where compliance,
security, and identity controls are mandatory.

---

## Important scope clarification

This lab applies to:

- **RHEL bastion hosts**
- **Utility or jump hosts**
- **Build systems**
- **Supporting infrastructure around OpenShift AI**

This lab **does NOT** apply to:

- Red Hat CoreOS (RHCOS)
- OpenShift cluster nodes
- Managed OpenShift services

OpenShift nodes manage FIPS and identity independently and should not be modified
manually.

---

## Environment assumptions

This lab has been validated conceptually against:

- Red Hat Enterprise Linux 9.x
- Active Directory–backed identity environments
- OpenShift Container Platform 4.20 (adjacent systems)
- OpenShift AI 3.x (adjacent systems)

Notes:
- Root or sudo access is required
- A system reboot is required for FIPS enablement
- This lab should be performed on a **non-production system first**

---

## Why this lab matters for federal environments

Federal systems often require:

- FIPS 140-2 / 140-3–validated cryptography
- Centralized identity (Active Directory)
- Auditable authentication and authorization
- Removal of third-party identity agents

SSSD is the **Red Hat–supported** approach for direct AD integration and aligns with
long-term platform support and compliance requirements.

---

## Step 1: Validate system readiness

Confirm the system is running RHEL:

```bash
cat /etc/redhat-release
```

Confirm FIPS is not already enabled:

```bash
cat /proc/sys/crypto/fips_enabled
```

A value of 0 indicates FIPS is not enabled.

---

## Step 2: Enable FIPS mode

Enable FIPS mode using supported tooling:

```bash
sudo fips-mode-setup --enable
```

Reboot the system:

```bash
sudo reboot
```

After reboot, confirm FIPS mode:

```bash
cat /proc/sys/crypto/fips_enabled
```

Expected output:

```
1
```

---

## Step 3: Validate system-wide crypto policies

Check the active crypto policy:

```bash
update-crypto-policies --show
```

Expected output:

```
FIPS
```

In environments using Active Directory, additional crypto subpolicies may be required
to maintain Kerberos compatibility. These should be evaluated in coordination with
security and directory teams.

---

## Step 4: Assess existing Centrify configuration

If Centrify is installed, identify components:

```bash
rpm -qa | grep -i centrify
```

Document:

- UID/GID mappings

- File ownership expectations

- sudo rules

- SSH access behavior

This step is critical to avoid ownership or access issues during migration.

---

## Step 5: Install required identity packages

```bash
Install supported packages for SSSD-based AD integration:

sudo dnf install -y \
  realmd \
  sssd \
  sssd-tools \
  oddjob \
  oddjob-mkhomedir \
  adcli \
  samba-common-tools
```

---

## Step 6: Join the system to Active Directory

Discover the domain:

```bash
realm discover example.com
```

Join the domain:

```bash
sudo realm join example.com
```

Provide AD credentials when prompted.

Verify the join:

```bash
realm list
```

---

## Step 7: Validate SSSD identity resolution

Test identity lookup:

```bash
id someuser@example.com
getent passwd someuser@example.com
```

Test group resolution:

```bash
getent group "Domain Users"
```

Confirm home directory creation on login.

---

## Step 8: Remove or disable Centrify (post-validation)

Only after validating SSSD functionality:

```bash
sudo systemctl stop centrifydc
sudo systemctl disable centrifydc
```

Optionally remove packages:

```bash
sudo dnf remove centrifydc
```

Removal should be coordinated with security and identity teams.

---

## Step 9: Validate behavior under FIPS

Confirm:

- Authentication succeeds

- Kerberos tickets are issued

- SSH access functions normally

- No cryptographic errors appear in logs

Inspect logs if issues arise:

```bash
journalctl -u sssd
journalctl -u sshd
```

---

## Completion criteria

You have successfully completed this lab when:

- FIPS mode is enabled and validated

- System crypto policy is FIPS-compliant

- AD authentication works via SSSD

- Centrify is no longer required

- Identity behavior is stable under FIPS constraints

---

## Why this lab is optional but important

Not every environment requires FIPS or centralized identity.

However, for federal workloads, this lab demonstrates:

- Compliance awareness

- Platform maturity

- Alignment with Red Hat–supported approaches

- Real-world operational considerations

This lab intentionally prioritizes correctness and safety over speed.

---

## Repository conclusion

This lab concludes the OpenShift AI lab series:

1. Data preparation

2. Model training

3. Model serving

4. Automation

5. Identity and compliance hardening

Together, these labs demonstrate a complete, enterprise-ready OpenShift AI workflow.

---

## Final note

Always validate identity and cryptographic changes in a controlled environment before
applying them to production systems.

When in doubt, involve platform security and directory services teams early.
