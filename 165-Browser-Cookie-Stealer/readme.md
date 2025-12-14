# 🍪 Browser Cookie Stealer

## Description
Accesses the Google Chrome internal SQLite database to dump stored session cookies. 

## Technical Note
Chrome encrypts cookie values using Windows DPAPI. This script extracts the encrypted database. In a real scenario, hackers decrypt these values to perform **Session Hijacking** (logging into accounts without passwords).