# 🕵️‍♂️ Project 189: Sandbox Detector
**Type:** Evasion / Anti-Analysis  
**Tech:** System Resource Profiling

## Description
Malware uses this technique to avoid detection.
Before executing the payload, it checks:
- **RAM/Disk Size:** Sandboxes usually have low resources (e.g., 2GB RAM).
- **CPU Cores:** Single-core systems are suspicious.
- **User Interaction:** If the mouse cursor doesn't move over time, it's likely an automated analysis bot.
If a sandbox is detected, the script terminates immediately to hide its true intent.