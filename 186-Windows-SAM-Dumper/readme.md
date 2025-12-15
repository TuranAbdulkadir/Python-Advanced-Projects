# 🧠 Project 186: Windows SAM Dumper
**Type:** Post-Exploitation / Credential Theft  
**Tech:** Windows Registry API

## Description
Extracts the **SAM (Security Account Manager)**, **SYSTEM**, and **SECURITY** registry hives from a live Windows system.
- These files contain the NTLM hashes of all user passwords.
- Normally locked by the kernel, this script uses administrative privileges to create a clean backup ("Dump") of the hives for offline cracking.