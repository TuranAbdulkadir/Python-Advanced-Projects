from scapy.all import *

print("--- DEAUTH ATTACK DETECTOR ---")
print("Ağ izleniyor... Jammer aranıyor.")

packet_count = 0
threshold = 50 # 50 deauth paketi gelirse alarm ver

def packet_handler(pkt):
    global packet_count
    # Deauth (Type 0, Subtype 12)
    if pkt.haslayer(Dot11Deauth):
        packet_count += 1
        src = pkt.addr2
        target = pkt.addr1
        
        print(f"⚠️ Deauth Paketi: {src} -> {target}")
        
        if packet_count > threshold:
            print(f"\n🚨 SALDIRI ALTINDASINIZ! Kaynak: {src}")
            print("Wifi Jammer Tespiti Yapıldı.")
            packet_count = 0 # Sayacı sıfırla

# Windows için iface='Wi-Fi'
try:
    sniff(iface="Wi-Fi", prn=packet_handler)
except:
    print("Hata: Monitor mod veya Npcap gerekli.")