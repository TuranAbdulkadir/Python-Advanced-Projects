# 🍪 Project 210: Browser Token Injector
**Type:** Account Takeover / Web
**Tech:** LevelDB Parsing, Regex

## Description
Targets **Session Tokens** stored in the browser's Local Storage (LevelDB).
Instead of stealing passwords, this attacks the session itself. If an attacker injects this stolen token into their own browser console, they instantly log into the victim's account (e.g., Discord, Instagram) bypassing 2FA.