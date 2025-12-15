# ⚙️ Project 204: Windows Service Persistence
**Type:** Advanced Persistence (APT)
**Tech:** Windows Services API (PyWin32)

## Description
Creates a legitimate **Windows Service** that runs malicious Python code.
Services run with `SYSTEM` privileges (higher than Admin) and start automatically before the user logs in. This is the ultimate persistence method used by advanced malware.