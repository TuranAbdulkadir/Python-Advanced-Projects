# 💀 Reverse TCP Shell

## Description
A classic **Command & Control (C2)** implementation. The victim connects back to the attacker, bypassing inbound firewall rules.

## Usage
1. **Attacker:** Run `attacker.py` first to open the listener port.
2. **Victim:** Edit `SERVER_IP` in `victim.py` and run it on the target machine.
3. **Control:** Once connected, type CMD commands (e.g., `dir`, `whoami`, `ipconfig`) in the attacker terminal to execute them on the victim's PC.