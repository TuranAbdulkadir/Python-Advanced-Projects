from scapy.all import *
import sys

print("--- ARP SPOOF DETECTOR (SAVUNMA) ---")
print("Ağ dinleniyor... Saldırı olursa uyaracağım!")

def get_mac(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    answered = srp(broadcast/arp_request, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc

def sniff_arp(interface):
    try:
        sniff(iface=interface, store=False, prn=process_packet)
    except Exception as e:
        print(f"Hata: {e}")

def process_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2: # ARP Response
        try:
            real_mac = get_mac(packet[ARP].psrc)
            response_mac = packet[ARP].hwsrc

            if real_mac != response_mac:
                print(f"🚨 DİKKAT! ARP SPOOFING SALDIRISI ALGILANDI!")
                print(f"Saldırgan MAC: {response_mac} | Taklit Edilen IP: {packet[ARP].psrc}")
        except IndexError:
            pass

# Windows'ta arayüz adı genelde 'Wi-Fi' veya 'Ethernet' olur
sniff_arp("Wi-Fi")