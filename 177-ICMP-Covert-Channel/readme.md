# 👻 Project 177: ICMP Covert Channel
**Type:** Network / Stealth Exfiltration  
**Tech:** Scapy, Raw Sockets

## Description
Establishes a covert communication channel using **ICMP Echo Requests** (Ping). 
Most firewalls allow Ping traffic. This tool hides sensitive data byte-by-byte inside the `Data` payload section of standard ping packets, bypassing DLP (Data Loss Prevention) systems.