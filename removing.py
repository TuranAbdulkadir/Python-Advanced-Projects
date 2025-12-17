import os
import random
import string
import sys

# --- THE DIGITAL NUKE: SECURE DISK WIPER ---
# AMAÇ: Hedef sürücüdeki verileri geri getirilemez şekilde yok etmek.

def wipe_file(file_path):
    try:
        # 1. Dosya boyutunu öğren
        file_size = os.path.getsize(file_path)
        
        # 2. Dosyanın içini rastgele verilerle doldur (Shredding)
        with open(file_path, "wb") as f:
            f.write(os.urandom(file_size))
            
        # 3. Dosya ismini değiştir (İzleri karıştır)
        new_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        dir_name = os.path.dirname(file_path)
        new_path = os.path.join(dir_name, new_name)
        os.rename(file_path, new_path)
        
        # 4. Dosyayı tamamen sil
        os.remove(new_path)
        print(f"[YOK EDİLDİ] {file_path}")
        
    except Exception as e:
        print(f"[HATA] {file_path} silinemedi: {e}")

def nuke_drive(target_drive):
    print("!" * 50)
    print(f"DİKKAT: {target_drive} SÜRÜCÜSÜNDEKİ HER ŞEY SİLİNECEK!")
    
    confirm = input(f"Devam etmek için 'YOKET' yazıp Enter'a bas: ")
    if confirm != "YOKET":
        sys.exit()

    for root, dirs, files in os.walk(target_drive, topdown=False):
        for name in files:
            wipe_file(os.path.join(root, name))
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except: pass

    print("\n[SUCCESS] Sürücü temizlendi.")

if __name__ == "__main__":
    # USB Sürücü Harfini Buraya Yaz (DİKKATLİ OL!)
    TARGET_USB = "D:\\" 
    
    if os.path.exists(TARGET_USB):
        nuke_drive(TARGET_USB)
    else:
        print("Sürücü bulunamadı.")
        