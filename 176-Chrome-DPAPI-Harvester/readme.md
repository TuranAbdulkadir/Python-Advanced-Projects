# 🗝️ Project 176: Chrome DPAPI Harvester
**Type:** Identity Theft / Post-Exploitation  
**Tech:** SQLite, Win32Crypt, AES

## Description
This is an advanced credential dumper.
1. It locates the Chrome `Local State` file to extract the encrypted master key.
2. It uses the Windows **DPAPI (Data Protection API)** via `win32crypt` to decrypt this master key (which only works under the victim's user context).
3. It accesses the `Login Data` SQLite database and decrypts every saved password using AES-GCM.

**Warning:** This reveals actual passwords stored in the browser.