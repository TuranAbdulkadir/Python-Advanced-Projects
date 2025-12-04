import socket, threading
name = input("Nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True: print(client.recv(1024).decode('ascii'))

def write():
    while True: client.send(f'{name}: {input("")}'.encode('ascii'))

threading.Thread(target=receive).start()
threading.Thread(target=write).start()