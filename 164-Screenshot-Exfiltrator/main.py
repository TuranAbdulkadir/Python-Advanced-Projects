import pyautogui
import time
import os

print("--- SCREEN SPY ---")

if not os.path.exists("captured_screens"):
    os.makedirs("captured_screens")

print("Ekran izleme aktif. Her 5 saniyede bir görüntü alınıyor...")

count = 0
try:
    while True:
        # Ekran görüntüsü al
        screenshot = pyautogui.screenshot()
        filename = f"captured_screens/screen_{count}.png"
        screenshot.save(filename)
        
        print(f"[+] Görüntü alındı: {filename}")
        count += 1
        time.sleep(5)
except KeyboardInterrupt:
    print("Durduruldu.")