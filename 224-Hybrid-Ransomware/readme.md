# 🔒 Project 184: Hybrid Ransomware (RSA + AES)
**Type:** Advanced Malware / Cryptography  
**Tech Stack:** Python, Cryptography Library (Fernet/AES, RSA-OAEP)  
**Difficulty:** God Mode (Critical)

## ⚠️ WARNING
**THIS PROJECT IS DANGEROUS.** It uses military-grade encryption. If you lose the `private_key.pem` file after encryption, the data is **mathematically impossible** to recover. Run this **ONLY** in the designated `TEST_ORTAMI` folder.

## 📖 Description
This project demonstrates the architecture of modern "Double Encryption" ransomware (like REvil, WannaCry, Conti). Pure RSA is too slow for large files, and pure AES is fast but key management is hard. This tool combines both:



1.  **Symmetric Phase (Speed):** Generates a random **AES-256** key in memory and encrypts the victim's files instantly.
2.  **Asymmetric Phase (Security):** Encrypts the random AES key using a hardcoded **RSA-4096 Public Key**.
3.  **Destruction:** Deletes the original AES key from memory.
4.  **Result:** The victim has the encrypted files and the encrypted key. They cannot unlock the key because they don't have the RSA Private Key (which is on the attacker's server).

## 🚀 How to Run
1.  Install requirements: `pip install cryptography`
2.  Run `main.py`.
3.  Select **Option 1** to Encrypt. It will create a dummy file in `TEST_ORTAMI` and lock it.
4.  Select **Option 2** to Decrypt. It will use the generated `private_key.pem` to restore the file.

## 🛡️ Defense Mechanism (Blue Team)
To stop this attack, engineers use **Entropy Analysis**. Encrypted files have high randomness (entropy). EDR systems monitor file write operations; if a process starts writing high-entropy data rapidly, it is flagged as ransomware and killed.