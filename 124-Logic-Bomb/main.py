import datetime
import time
import os

print("--- LOGIC BOMB PLANTED ---")
# Tetiklenme Tarihi (Yıl, Ay, Gün)
TRIGGER_DATE = datetime.date(2025, 12, 15) 

def explode():
    print("\n💣 BOOM! MANTIK BOMBASI PATLADI!")
    print("Sistem dosyaları etkileniyor... (Simülasyon)")
    # Gerçek zararlı kod buraya yazılır (örn: os.remove("önemli.txt"))
    with open("HACKED.txt", "w") as f:
        f.write("Zaman doldu. Sisteminiz ele geçirildi.")

while True:
    today = datetime.date.today()
    
    if today >= TRIGGER_DATE:
        explode()
        break
    else:
        print(f"Henüz zamanı gelmedi... ({today})")
        time.sleep(10) # 10 saniyede bir kontrol (Gerçekte günde 1 olur)