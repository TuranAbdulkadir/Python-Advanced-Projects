import requests
import os

print("--- WEB SITE CLONER (PHISHING PREP) ---")
url = input("Kopyalanacak URL (örn: https://example.com): ")
filename = "index.html"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    print("Site indiriliyor...")
    r = requests.get(url, headers=headers)
    
    if r.status_code == 200:
        # Kaynak kodunu kaydet
        with open(filename, "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"✅ Site kopyalandı! Dosya: {filename}")
        print("Not: Bu dosyayı bir hosting'e atarsan birebir kopya gibi görünür.")
    else:
        print(f"Hata: {r.status_code}")
except Exception as e:
    print(f"Bağlantı Hatası: {e}")