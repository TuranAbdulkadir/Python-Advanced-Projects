# 🎭 Project 185: Steganography Polyglot
**Type:** Evasion / Stealth  
**Tech:** Binary Manipulation, File Formats

## Description
Creates a **Polyglot** file that is valid in two different formats simultaneously.
- To a DLP scanner or Antivirus, it looks like a harmless `.jpg` image (valid header).
- To the OS or a script loader, it contains executable code appended at the end.
- This allows malware to bypass "Image Only" upload filters.