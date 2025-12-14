from scapy.all import *
import sys

print("--- STEALTH SYN SCANNER (ROOT GEREKİR) ---")
target = input("Hedef IP: ")
ports = [21, 22, 80, 443, 3306, 8080]

def syn_scan(target, port):
    # El sıkışmayı tamamlamadan (SYN) portu yokla
    pkt = IP(dst=target)/TCP(dport=port, flags="S")
    resp = sr1(pkt, timeout=1, verbose=0)
    
    if resp:
        if resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12: # SYN-ACK (Açık)
                # Bağlantıyı hemen kopar (RST) - Log tutulmasın diye
                send_rst = IP(dst=target)/TCP(dport=port, flags="R")
                send(send_rst, verbose=0)
                return True
    return False

print("Tarama başladı (Bu gerçek bir ağ taramasıdır)...")
try:
    for port in ports:
        if syn_scan(target, port):
            print(f"✅ Port {port} AÇIK (SYN-ACK alındı)")
        else:
            print(f"❌ Port {port} KAPALI")
except Exception as e:
    print(f"Hata: {e} (Scapy için Yönetici/Root izni gerekir)")