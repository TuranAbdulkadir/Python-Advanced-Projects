# 🔒 Project 184: Hybrid Ransomware (RSA+AES)
**Type:** Malware / Cryptography  
**Tech:** RSA-4096, AES-256

## Description
Implements the architecture of modern ransomware.
1. Generates a one-time **AES Session Key** to encrypt files rapidly.
2. Encrypts the AES key itself using an embedded **RSA Public Key**.
3. Destroys the original AES key from memory.

**Result:** The victim is left with encrypted files and an encrypted key. Only the attacker (holding the RSA Private Key) can decrypt the session key to restore the files.