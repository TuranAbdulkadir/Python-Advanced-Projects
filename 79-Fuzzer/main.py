import socket
import time

print("--- SIMPLE FUZZER ---")
target_ip = input("Hedef IP: ")
port = int(input("Hedef Port (örn 21 FTP): "))

buffer = ["A"]
counter = 100

while len(buffer) <= 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        print(f"Fuzzing ile {len(string)} byte gönderiliyor...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.recv(1024)
        s.send(string.encode() + b'\r\n')
        s.close()
    except:
        print(f"⚠️ HEDEF ÇÖKTÜ! Tahmini Buffer Boyutu: {len(string)} byte")
        print("Bu noktada bir Buffer Overflow açığı olabilir.")
        break
    time.sleep(1)