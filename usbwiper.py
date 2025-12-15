import os
import time
import sys

# --- USB WIPER: D SÜRÜCÜSÜ YOK EDİCİ ---
# DİKKAT: D: Sürücüsündeki HER ŞEYİ siler.

def secure_delete(file_path):
    try:
        # 1. Dosyanın boyutunu al
        length = os.path.getsize(file_path)
        # 2. Üzerine rastgele veri yaz (Recover edilemesin diye)
        with open(file_path, "wb") as f:
            f.write(os.urandom(length))
        # 3. Dosyayı sil
        os.remove(file_path)
        print(f"[YOK EDİLDİ] {file_path}")
    except Exception as e:
        print(f"[HATA] {file_path} silinemedi: {e}")

def nuke_drive():
    target_drive = "D:\\"  # <--- İŞTE DEĞİŞTİRDİĞİMİZ YER
    
    print(f"[!] HEDEF SÜRÜCÜ: {target_drive}")
    print("[!] DİKKAT: USB içindeki veriler silinecek!")
    
    if not os.path.exists(target_drive):
        print("[!] Hata: D: Sürücüsü (USB) bulunamadı!")
        return

    input("[?] Emin misin? Silmek için ENTER'a bas...")

    # D Sürücüsündeki tüm klasörleri gez
    for root, dirs, files in os.walk(target_drive):
        for file in files:
            file_path = os.path.join(root, file)
            secure_delete(file_path)

    print("\n[INFO] D: Sürücüsü temizlendi.")

if __name__ == "__main__":
    nuke_drive()