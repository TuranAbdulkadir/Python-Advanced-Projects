import socket
import threading
from queue import Queue
from datetime import datetime

target = input("Target IP (e.g., google.com): ")
target_ip = socket.gethostbyname(target)
print_lock = threading.Lock()

print(f"Scanning: {target_ip}")
print("-" * 50)

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        con = s.connect((target_ip, port))
        with print_lock:
            print(f"✅ Port {port} is OPEN")
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()
for x in range(50): # 50 Thread (Hız)
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 1001): # 1-1000 arası portları tara
    q.put(worker)

q.join()
print("Scanning Completed.")