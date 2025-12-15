# 🦎 Project 173: Polymorphic Engine
**Type:** Evasion / Malware Dev  
**Tech:** File Manipulation, Regex

## Description
A proof-of-concept for **Polymorphic Malware**. Every time this script executes:
1. It reads its own source code.
2. It appends random "junk data" or modifies variable names.
3. It rewrites itself to the disk.

**Impact:** The file's cryptographic hash (MD5/SHA256) changes on every run, bypassing signature-based antivirus detection.