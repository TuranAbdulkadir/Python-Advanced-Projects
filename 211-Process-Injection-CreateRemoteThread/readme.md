# 💉 Project 211: Process Injection (CreateRemoteThread)
**Tech:** Windows API (VirtualAllocEx, CreateRemoteThread)
**Realism:** 100%

Standard malware technique. Instead of running as a separate process, this script allocates memory inside a target process (like `notepad.exe`) and injects raw x64 shellcode. The shellcode is executed by creating a new thread in the remote process.