import socket
import time
import random

print("--- ADVANCED PROTOCOL FUZZER ---")
target_ip = input("Hedef IP: ")
target_port = int(input("Hedef Port (örn: 21 FTP): "))

# Fuzzing için Payload Listesi
commands = ["USER", "PASS", "STOR", "RETR", "MKD"]
buffer_chars = ["A", "\x00", "%s", "\xff", "1234"]

def fuzz():
    counter = 0
    while True:
        try:
            # Rastgele payload oluştur
            cmd = random.choice(commands)
            char = random.choice(buffer_chars)
            length = random.randint(10, 5000)
            payload = cmd + " " + (char * length) + "\r\n"
            
            print(f"[{counter}] Fuzzing: {cmd} with {length} bytes...")
            
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)
            s.connect((target_ip, target_port))
            s.recv(1024) # Banner'ı al
            
            s.send(payload.encode())
            s.close()
            
            counter += 1
            time.sleep(0.05) # Hızlı saldırı
            
        except Exception as e:
            print(f"\n🔥 SİSTEM ÇÖKTÜ! (CRASH DETECTED)")
            print(f"Son Gönderilen Paket: {cmd} + {length} bytes ({char})")
            print("Bu bir Buffer Overflow açığı olabilir!")
            break

fuzz()