# 🦗 Project 190: UEFI/BIOS Persistence
**Type:** Advanced Persistence (APT)  
**Tech:** EFI System Partition Manipulation

## Description
Simulates the most dangerous persistence technique: **UEFI Infection**.
The script targets the EFI System Partition (ESP), which holds the bootloaders. By replacing or modifying `bootx64.efi`, malware can execute **before the Operating System loads**, surviving OS reinstalls and hard drive replacements.