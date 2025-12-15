# 👻 Project 226: ETW Blinder
**Type:** Evasion / Stealth
**Tech:** Memory Patching

Patches the `EtwEventWrite` function in `ntdll.dll` inside the current process. This effectively blinds **Event Tracing for Windows (ETW)**. Modern EDRs and Blue Teams rely on ETW to see what a process is doing (network connections, .NET calls). This tool cuts that feed.