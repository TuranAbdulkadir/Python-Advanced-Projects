import os
from cryptography.fernet import Fernet

print("--- KURTARICI (DECRYPTOR) ---")

# 1. Anahtarı Bul
if not os.path.exists("secret.key"):
    print("❌ HATA: 'secret.key' bulunamadı! Şifreyi çözemem.")
    input("Çıkış için Enter...")
    exit()

with open("secret.key", "rb") as key_file:
    key = key_file.read()

crypter = Fernet(key)
target_dir = "test_files" # Hedef klasör

# 2. Şifreleri Çöz
print(f"🔑 Anahtar bulundu. {target_dir} taranıyor...")
count = 0

for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file == "README_RECOVER.txt": 
            continue 
        
        file_path = os.path.join(root, file)
        try:
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            
            decrypted_data = crypter.decrypt(encrypted_data)
            
            with open(file_path, "wb") as f:
                f.write(decrypted_data)
            
            print(f"✅ Açıldı: {file}")
            count += 1
        except:
            pass

print(f"\n🎉 Toplam {count} dosya kurtarıldı!")
input("Kapatmak için Enter'a bas...")