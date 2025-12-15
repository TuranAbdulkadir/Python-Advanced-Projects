# 🛡️ Project 212: AMSI Memory Patcher
**Tech:** Memory Patching
**Realism:** 100%

Disables **Windows Defender's** ability to scan scripts in the current process memory. It locates the `AmsiScanBuffer` function in `amsi.dll` and overwrites its first instructions with a "return" opcode, effectively blinding the antivirus.