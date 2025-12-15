# 🚇 Project 174: DNS Tunneling C2
**Type:** Network / Exfiltration  
**Tech:** Scapy, UDP, DNS Protocol

## Description
Demonstrates how to bypass strict Firewalls. Since DNS traffic (Port 53) is rarely blocked, this tool hides sensitive data inside **DNS Queries**.
- **Technique:** It encodes data into Base64 and attaches it as a subdomain (e.g., `SECRET_DATA.google.com`).
- **Result:** The firewall sees a standard DNS lookup, but the attacker receives the data.