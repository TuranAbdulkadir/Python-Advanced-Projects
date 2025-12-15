# ⚙️ Project 232: COM Hijacking
**Type:** Persistence
**Tech:** Windows Registry / COM

Abuses the **Component Object Model (COM)** logic. By creating a user-mode registry key for a specific CLSID, we trick Windows into loading our malicious DLL instead of the system DLL whenever that object is requested (e.g., when opening a folder or the start menu).