# 👻 Project 172: Process Hollowing
**Type:** Stealth / Evasion  
**Tech:** Ctypes, Windows API, Memory Manipulation

## Description
This tool demonstrates the sophisticated **Process Hollowing** technique used by advanced malware (like Stuxnet). 
1. It launches a legitimate process (e.g., `notepad.exe`) in a **SUSPENDED** state.
2. It carves out (hollows) the legitimate code from RAM.
3. It injects malicious shellcode into the empty memory space.
4. It resumes the process.

**Result:** Task Manager sees "Notepad", but the code running is your malware.

## Usage
Run as **Administrator**.