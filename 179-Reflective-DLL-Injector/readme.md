# 💉 Project 179: Reflective Code Injector
**Type:** Stealth / Malware Tech  
**Tech:** Ctypes, Windows API (CreateRemoteThread)

## Description
Demonstrates **Memory Injection**. Instead of running a malicious `.exe`, this script forces a legitimate running program (like Chrome or Explorer) to execute our malicious code (Shellcode) from its own memory space. This is a common technique to hide from antivirus software.