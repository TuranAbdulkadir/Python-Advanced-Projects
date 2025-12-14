import os
import sys
import time

print("--- SELF DESTRUCTING SCRIPT ---")
print("Bu kod çalışacak, görevini yapacak ve sonra kendini silecek.")

# Görev (Payload)
with open("calinti_veri.txt", "w") as f:
    f.write("Gizli veriler buraya...")
print("✅ Görev tamamlandı.")

# Kendini İmha Etme
print("💥 Kendini imha başlatılıyor...")
time.sleep(2)

script_path = os.path.abspath(sys.argv[0])
os.remove(script_path)

# Script silindiği için bu satır sonrası hata verebilir veya kapanır