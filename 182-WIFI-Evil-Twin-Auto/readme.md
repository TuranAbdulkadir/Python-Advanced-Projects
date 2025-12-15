# 📡 Project 182: WIFI Evil Twin
**Type:** Network Attack / MITM  
**Tech:** Scapy, 802.11 Protocols

## Description
This script broadcasts **fake WiFi Beacon frames** to simulate a legitimate Access Point. 
Victims' devices, seeing a stronger signal with a known SSID (e.g., "Starbucks_Wifi"), will automatically disconnect from the real router and connect to your machine, allowing you to intercept all their traffic.