# 🪝 Project 188: Rootkit Userland Hook
**Type:** Stealth / Evasion  
**Tech:** API Hooking, Memory Patching, Assembly

## Description
Demonstrates **Inline API Hooking**, a core technique used by Rootkits and Antiviruses.
1. It locates a system function (`MessageBoxW` in `user32.dll`) in memory.
2. It overwrites the first 5 bytes of the function with a **JMP** (Jump) instruction redirecting to our malicious Python function.
3. When any program tries to call `MessageBoxW`, our code runs first, allowing us to modify arguments or block execution.