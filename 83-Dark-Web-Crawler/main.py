import requests

print("--- DARK WEB SCRAPER ---")
print("Tor servisi kontrol ediliyor (127.0.0.1:9050)...")

# Tor Proxy Ayarları
session = requests.session()
session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                   'https': 'socks5h://127.0.0.1:9050'}

# Test edilecek Onion Linki (DuckDuckGo Onion)
url = "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/"

try:
    print(f"Bağlanılıyor: {url}")
    r = session.get(url, timeout=20)
    
    if r.status_code == 200:
        print("✅ BAĞLANTI BAŞARILI!")
        print(f"Başlık: {r.text.split('<title>')[1].split('</title>')[0]}")
        print("Gizli ağa erişim sağlandı.")
    else:
        print(f"Durum Kodu: {r.status_code}")
except Exception as e:
    print("❌ Hata: Tor Proxy açık mı? (Tor Browser'ı açıp dene)")
    print(f"Detay: {e}")