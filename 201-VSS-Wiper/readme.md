# 🌑 Project 201: VSS Wiper
**Type:** Destructive / Anti-Recovery
**Tech:** Windows Admin Commands

## Description
Ransomware creates a situation where the victim cannot restore their files from backup. This tool interacts with `vssadmin` to execute the command that wipes **Volume Shadow Copies** (Windows Restore Points).
**Mechanism:** `vssadmin.exe Delete Shadows /All /Quiet`