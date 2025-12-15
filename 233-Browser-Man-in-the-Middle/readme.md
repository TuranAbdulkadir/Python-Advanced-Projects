# 🦎 Project 234: Polyglot Malware
**Type:** Evasion
**Tech:** File Format Abuse

Creates a file that is valid in multiple formats simultaneously (e.g., PDF and JavaScript). Security scanners often identify the file type based on the header (PDF) and skip script analysis. However, if executed in a different context (like a browser), the malicious script portion runs.