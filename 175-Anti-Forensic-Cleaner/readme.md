# 🧹 Project 175: Anti-Forensic Cleaner
**Type:** Stealth / Counter-Forensics  
**Tech:** OS Low-level File Ops

## Description
A tool designed to defeat digital forensics recovery.
1. **Shredding:** Overwrites the file content with random bytes multiple times (DoD Standard) before deletion to prevent magnetic recovery.
2. **Renaming:** Changes filename to break file table references.
3. **Timestomping:** Manipulates the folder's "Last Modified" timestamp to a past date, confusing forensic timelines.