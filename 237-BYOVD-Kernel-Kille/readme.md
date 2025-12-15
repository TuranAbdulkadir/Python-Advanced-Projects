# 🛡️ Project 237: BYOVD Exploit
**Type:** Kernel Exploitation
**Tech:** DeviceIoControl / Driver Abuse

**Risk Level:** CRITICAL (Total System Compromise)
Demonstrates the **BYOVD** technique used by advanced ransomware groups. Instead of writing a custom driver (which requires a Microsoft certificate), attackers load a legitimate, signed driver with known bugs (like Capcom.sys or Afterburner). They exploit this driver to execute code in the Windows Kernel, allowing them to kill Anti-Virus processes that are normally protected.