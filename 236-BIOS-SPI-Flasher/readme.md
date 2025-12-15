# 🧱 Project 236: BIOS SPI Flasher
**Type:** Hardware Destruction / Bricking
**Tech:** SPI Protocol / Low-level I/O

**Risk Level:** IRREVERSIBLE HARDWARE DAMAGE
Simulates the logic of **CIH (Chernobyl)** or **Petya** style attacks that target the motherboard firmware. By communicating with the SPI Flash Controller, it erases or corrupts the BIOS/UEFI code. Once executed, the computer cannot boot, post, or show any logo. The motherboard must be physically replaced or reflashed with hardware tools.