import socket
import threading
import logging

logging.basicConfig(filename='honeynet.log', level=logging.INFO, format='%(asctime)s - %(message)s')

print("--- HONEYNET MANAGER (Multi-Protocol Trap) ---")

def start_honey(port, service_name):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind(('0.0.0.0', port))
        server.listen(5)
        print(f"🕸️ Tuzak Kuruldu: {service_name} (Port {port})")
        
        while True:
            client, addr = server.accept()
            print(f"🚨 {service_name} SALDIRISI! IP: {addr[0]}")
            logging.info(f"Saldırı: {service_name} - IP: {addr[0]}")
            
            # Servise özel sahte mesaj
            if port == 21: client.send(b"220 ProFTPD 1.3.5 Server\r\n")
            elif port == 80: client.send(b"HTTP/1.1 200 OK\r\nServer: Apache/2.4.49\r\n\r\n")
            
            client.close()
    except:
        print(f"Port {port} hatası (Yönetici izni gerekebilir).")

# Tüm tuzakları aynı anda başlat
services = [(21, "FTP"), (23, "Telnet"), (80, "HTTP"), (2222, "SSH")]

for port, name in services:
    t = threading.Thread(target=start_honey, args=(port, name))
    t.start()