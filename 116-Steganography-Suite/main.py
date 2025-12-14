from PIL import Image
from cryptography.fernet import Fernet

print("--- ADVANCED STEGANOGRAPHY SUITE ---")

# 1. Metni Şifrele
key = Fernet.generate_key()
cipher = Fernet(key)
msg = "BU COK GIZLI BIR DEVLET SIRRIDIR"
encrypted_msg = cipher.encrypt(msg.encode()).decode()

print(f"Mesaj: {msg}")
print(f"Şifreli: {encrypted_msg[:15]}...")
print(f"Anahtar: {key.decode()}")

# 2. Resme Gizle (Basitleştirilmiş Mantık)
def encode_image(img_path, data):
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    
    # Veriyi binary yap
    binary_data = ''.join(format(ord(i), '08b') for i in data)
    data_len = len(binary_data)
    idx = 0
    
    for y in range(height):
        for x in range(width):
            if idx < data_len:
                pixel = list(img.getpixel((x, y)))
                # Rengini 1 birim değiştir (Gözle görülmez)
                pixel[0] = pixel[0] & ~1 | int(binary_data[idx])
                encoded.putpixel((x, y), tuple(pixel))
                idx += 1
            else:
                break
    
    encoded.save("secret_image.png")
    print("✅ Resim oluşturuldu: secret_image.png")

# Test için 'input.png' gerekiyor
try:
    # Boş resim oluştur (Test için)
    img = Image.new('RGB', (100, 100), color = 'red')
    img.save('input.png')
    
    encode_image("input.png", encrypted_msg)
except Exception as e:
    print(f"Hata: {e}")