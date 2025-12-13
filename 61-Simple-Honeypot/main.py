import socket
import logging
from datetime import datetime

# Log dosyasını ayarla
logging.basicConfig(filename='honeypot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def start_honeypot(port=2222):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    
    print(f"🍯 HONEYPOT AKTİF! Port: {port} (Saldırılar bekleniyor...)")
    
    while True:
        client, addr = server.accept()
        print(f"🚨 SALDIRI ALGILANDI! IP: {addr[0]}")
        
        # Sahte karşılama mesajı
        client.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\r\n")
        
        try:
            data = client.recv(1024).decode('utf-8', errors='ignore')
            print(f"📝 Girilen Veri: {data.strip()}")
            logging.info(f"IP: {addr[0]} - Data: {data.strip()}")
        except:
            pass
        
        client.close()

if __name__ == "__main__":
    # Gerçek 22 portu için yönetici izni gerekir, 2222 test içindir.
    start_honeypot(2222)