# 🗝️ Project 215: MiniDump LSASS
**Tech:** DbgHelp API
**Realism:** 100%

Uses the native Windows API `MiniDumpWriteDump` to create a full memory dump of the Local Security Authority Subsystem Service (`lsass.exe`). This dump file contains cleartext passwords and Kerberos tickets, which can be extracted offline using tools like Mimikatz.