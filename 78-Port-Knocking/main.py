import socket
import time

print("--- PORT KNOCKER CLIENT ---")
target_ip = input("Hedef IP: ")
# Bu sırayı bilen kapıyı açar
knock_sequence = [7000, 8000, 9000]

print("Gizli kapı çalınıyor... 👊")

for port in knock_sequence:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect_ex((target_ip, port))
        s.close()
        print(f"Vuruldu: Port {port}")
        time.sleep(0.5)
    except:
        pass

print("✅ Sekans tamamlandı! Eğer doğruysa gizli port açılmıştır.")
print("(Sunucu tarafında iptables/firewall ayarı gerektirir, bu Client simülasyonudur)")