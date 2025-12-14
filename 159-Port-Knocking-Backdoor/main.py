import socket
import time

print("--- PORT KNOCKING DOOR ---")
print("Sıra: 7000, 8000, 9000. Doğru vurursan 9999 açılır.")

knock_sequence = [7000, 8000, 9000]
client_progress = {} # {ip: [state]}

# Basit sniff mantığı (Gerçekte raw socket gerekir)
# Burada simülasyon olarak her porta bind edip bekliyoruz
def start_backdoor():
    s = socket.socket()
    s.bind(('0.0.0.0', 9999))
    s.listen(1)
    print("✅ GİZLİ KAPI AÇILDI! Giriş yapabilirsiniz.")
    conn, addr = s.accept()
    conn.send(b"HACKER SHELL ACCESS GRANTED\n")

# Bu örnekte mantığı gösteriyoruz, gerçek port knocking firewall (iptables) ile yapılır.
# Python ile bunu yapmak için raw socket ile SYN paketlerini saymak gerekir.
print("Bu kod firewall seviyesinde çalışmalıdır. Simülasyon modunda bekliyor.")
start_backdoor()