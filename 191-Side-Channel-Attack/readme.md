# ⏱️ Project 191: Timing Side-Channel Attack
**Type:** Cryptanalysis / Exploitation  
**Tech:** Timing Analysis

## Description
Demonstrates how to crack passwords without brute-forcing all combinations, using a **Timing Attack**.
- Vulnerable systems often verify passwords character-by-character and return `False` immediately upon a mismatch.
- This creates a tiny time difference: processing "Wrong" takes less time than processing "Correct" -> "Wrong".
- By measuring these micro-delays, the attacker can guess the password one character at a time.