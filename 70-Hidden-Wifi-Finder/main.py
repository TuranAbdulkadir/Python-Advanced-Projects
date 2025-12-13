from scapy.all import *

print("--- HIDDEN WIFI FINDER ---")
print("Gizli ağlar aranıyor... (Kapatmak için CTRL+C)")

hidden_nets = []

def packet_handler(pkt):
    if pkt.haslayer(Dot11Beacon):
        # SSID boşsa veya gizliyse
        if not pkt.info:
            addr = pkt.addr3
            if addr not in hidden_nets:
                print(f"👻 GİZLİ AĞ BULUNDU! MAC: {addr}")
                hidden_nets.append(addr)
    
    # Probe Response paketleri bazen gizli adı ifşa eder
    elif pkt.haslayer(Dot11ProbeResp):
        addr = pkt.addr3
        if addr in hidden_nets:
            print(f"🔓 GİZLİ AĞIN ADI ÇÖZÜLDÜ: {pkt.info.decode()} ({addr})")

# Wifi arayüzünü dinle (Monitör mod gerekli)
# Windows'ta kısıtlı çalışır, Linux'ta tam güç çalışır.
try:
    sniff(iface="Wi-Fi", prn=packet_handler, count=1000)
except:
    print("Hata: Scapy/Npcap sorunu veya Wifi kartı desteklemiyor.")