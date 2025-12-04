import socket, threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()
clients = []

def broadcast(msg):
    for c in clients: c.send(msg)

def handle(client):
    while True:
        try: broadcast(client.recv(1024))
        except: clients.remove(client); client.close(); break

print("Server Running...")
while True:
    client, addr = server.accept()
    clients.append(client)
    threading.Thread(target=handle, args=(client,)).start()