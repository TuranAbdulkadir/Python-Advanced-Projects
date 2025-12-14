# 🕷️ ARP Spoofer (Man-in-the-Middle)

## Description
This tool performs an **ARP Poisoning** attack. It tricks the target device into believing your PC is the Router, and tricks the Router into believing your PC is the target device.

## Impact
This places you in the middle of the connection, allowing you to inspect, modify, or drop packets (Wireshark is required to analyze the captured traffic).

## Usage
1. Edit `target_ip` and `gateway_ip` in the script.
2. Run as Administrator.
3. Use `CTRL+C` to stop and restore network tables to avoid crashing the victim's internet.