import os
from cryptography.fernet import Fernet
from colorama import Fore, init

init(autoreset=True)
print("--- RANSOMWARE DECRYPTOR (KURTARICI) ---")

folder = "test_dosyalari" # Şifreli klasör
key_file = "thekey.key" # Hacker'ın bıraktığı anahtar dosyası (varsa)

def load_key():
    return open(key_file, "rb").read()

def decrypt_files():
    try:
        key = load_key()
        fernet = Fernet(key)
        
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            
            # Sadece dosyaları işlemden geçir
            if os.path.isfile(file_path) and filename != "gizli.txt": # Örnek
                with open(file_path, "rb") as file:
                    encrypted_data = file.read()
                
                try:
                    decrypted_data = fernet.decrypt(encrypted_data)
                    
                    with open(file_path, "wb") as file:
                        file.write(decrypted_data)
                    print(f"{Fore.GREEN}✅ Kurtarıldı: {filename}")
                except:
                    print(f"{Fore.RED}❌ Başarısız: {filename} (Anahtar yanlış olabilir)")
                    
        print("\n🎉 Operasyon Tamamlandı! Dosyalarını kontrol et.")

    except FileNotFoundError:
        print("❌ Anahtar dosyası (thekey.key) bulunamadı! Fidye ödenmemiş olabilir...")

decrypt_files()