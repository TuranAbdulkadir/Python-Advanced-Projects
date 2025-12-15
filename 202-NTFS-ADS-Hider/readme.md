# 👻 Project 202: NTFS ADS Hider
**Type:** Stealth / Evasion
**Tech:** NTFS File System Features

## Description
Uses **Alternate Data Streams (ADS)** to hide malicious code *inside* a legitimate text file without changing its size or contents visible to the user.
- **Normal user sees:** `masum_notlar.txt` (1 KB)
- **Real content:** `masum_notlar.txt:secret.py` (Hidden Payload)