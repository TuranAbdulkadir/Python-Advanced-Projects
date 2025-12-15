# ☠️ Project 180: MBR Wiper (Bootkit)
**Type:** Destructive Malware  
**Tech:** Raw Disk Access, MBR Structure

## Description
Simulates a destructive attack on the **Master Boot Record (MBR)** of a hard drive.
The MBR is the first 512 bytes of the disk that tells the BIOS how to boot Windows. Overwriting this section renders the computer unbootable ("Bricked").
**WARNING:** The code is configured to write to a dummy file for safety.