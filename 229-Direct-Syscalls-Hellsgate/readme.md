# 🛡️ Project 229: Direct Syscalls (Hell's Gate)
**Type:** Evasion / Red Team Tradecraft
**Tech:** Assembly / Kernel Interaction

Bypasses user-mode API hooks placed by EDRs (Endpoint Detection and Response). Instead of calling monitored APIs like `CreateThread`, this tool executes raw **Syscall** instructions in Assembly, talking directly to the Windows Kernel without going through `ntdll.dll`.