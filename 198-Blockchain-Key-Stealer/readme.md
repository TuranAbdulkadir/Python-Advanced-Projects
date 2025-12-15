# ₿ Project 198: Blockchain Key Stealer
**Type:** Crypto Forensics / Theft  
**Tech:** Regex, Memory Analysis

## Description
Scans files (like Memory Dumps, Swap files, or Disk Images) for **Unencrypted Private Keys**.
It uses specific Regular Expressions to identify:
- Bitcoin WIF Keys (starts with '5', Base58)
- Ethereum Private Keys (64 hex characters)