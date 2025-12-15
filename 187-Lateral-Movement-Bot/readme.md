# 🐛 Project 187: Lateral Movement Bot
**Type:** Network / Worm  
**Tech:** WMI (Windows Management Instrumentation)

## Description
Simulates the behavior of a **Network Worm**.
1. Scans the local subnet for live hosts with open management ports (RPC/135).
2. Attempts to authenticate using a list of stolen credentials (Credential Stuffing).
3. If successful, executes a malicious payload remotely via WMI `Win32_Process.Create`.
**Impact:** Allows the attacker to pivot from one compromised machine to the entire network.