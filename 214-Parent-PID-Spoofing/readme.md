# 🎭 Project 214: Parent PID Spoofing
**Tech:** Windows API (UpdateProcThreadAttribute)
**Realism:** Technique Demo

Spoofs the **Parent Process ID** of a newly created process. Instead of showing the malware as the parent, the new process appears to be spawned by a trusted system process (like `explorer.exe` or `svchost.exe`), confusing EDR (Endpoint Detection Response) analysis trees.