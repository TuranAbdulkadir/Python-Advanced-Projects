from cryptography.fernet import Fernet

print("--- REAL AES FILE ENCRYPTION ---")
filename = input("Şifrelenecek dosya adı: ")

# Anahtar Üret
key = Fernet.generate_key()
with open("my_secret.key", "wb") as key_file:
    key_file.write(key)

try:
    # Dosyayı Oku
    with open(filename, "rb") as f:
        data = f.read()
    
    # Şifrele
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    
    # Şifreli veriyi kaydet (Orijinalin üzerine yazar!)
    with open(filename, "wb") as f:
        f.write(encrypted)
        
    print(f"✅ DOSYA KİLİTLENDİ: {filename}")
    print("🔑 Anahtar 'my_secret.key' dosyasına kaydedildi. KAYBETME YOKSA AÇILMAZ!")

except FileNotFoundError:
    print("Dosya yok.")