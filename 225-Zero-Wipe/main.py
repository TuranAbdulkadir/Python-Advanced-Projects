import os
import sys
import random

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod veriyi fiziksel olarak yok eder.")

print("--- WEAPONIZED DISK WIPER ---")

def secure_delete(filepath):
    # 1. ÜZERİNE YAZMA (Weaponized Part)
    # Simülasyon: os.remove(filepath)
    # Gerçek: Dosyanın bulunduğu sektörlere 0 ve 1 yaz.
    
    file_size = os.path.getsize(filepath)
    
    with open(filepath, "wb") as f:
        # Tur 1: Sıfırlar
        print("[*] Pass 1: Sıfırlanıyor...")
        f.write(b'\x00' * file_size)
        f.flush()
        os.fsync(f.fileno()) # Diske zorla yaz
        
        # Tur 2: Rastgele Veri
        print("[*] Pass 2: Karıştırılıyor...")
        f.seek(0)
        f.write(os.urandom(file_size))
        f.flush()
        os.fsync(f.fileno())
        
    # 2. İSİM DEĞİŞTİRME VE SİLME
    # Metadata'yı bozmak için ismini değiştirip siliyoruz.
    new_name = filepath + ".tmp"
    os.rename(filepath, new_name)
    os.remove(new_name)
    
    print("💀 DOSYA YOK EDİLDİ. FBI gelse kurtaramaz.")

if __name__ == "__main__":
    secure_delete("gizli_belge.docx")