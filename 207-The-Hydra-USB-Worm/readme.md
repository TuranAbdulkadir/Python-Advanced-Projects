# 🐙 Project 207: Hydra USB Worm
**Type:** Self-Replication / Worm
**Tech:** File System Manipulation

## Description
Demonstrates **Self-Replication**.
The script scans for removable drives (USB sticks). When found, it copies its own executable file onto the drive and creates deceptive "Lure" files to trick the user into running it on the next computer the USB is plugged into.