from scapy.all import *

print("--- WIFI PROBE REQUEST SNIFFER ---")
print("Çevredeki cihazlar ve aradıkları ağlar listeleniyor...")

seen_devices = []

def packet_handler(pkt):
    if pkt.haslayer(Dot11ProbeReq):
        try:
            mac = pkt.addr2
            ssid = pkt.info.decode()
            
            if ssid: # Boş olmayanları göster
                log = f"📱 Cihaz MAC: {mac} -> Aradığı Ağ: {ssid}"
                if log not in seen_devices:
                    print(log)
                    seen_devices.append(log)
        except:
            pass

# Not: Windows'ta Monitor Mod zordur, Linux/Kali'de tam çalışır.
try:
    sniff(iface="Wi-Fi", prn=packet_handler)
except Exception as e:
    print(f"Hata: {e} (Monitor Mode gerekebilir)")