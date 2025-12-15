# 🦈 Project 221: Raw Socket Sniffer
**Tech:** Raw Sockets, IOCTL
**Realism:** 100%

Interacts directly with the Network Interface Card (NIC) using **Raw Sockets**. By sending an IOCTL code to enable Promiscuous Mode, it captures all traffic passing through the interface, similar to how Wireshark works at a low level.