import requests
import time

print("--- REAL TOR NETWORK ACCESS ---")

# Tor Proxy Ayarları (Tor Browser varsayılan portu 9150 veya 9050'dir)
proxies = {
    'http': 'socks5h://127.0.0.1:9150',
    'https': 'socks5h://127.0.0.1:9150'
}

# Gerçek IP adresimizi kontrol edelim (Tor üzerinden mi çıkıyoruz?)
try:
    print("Normal IP adresin gizleniyor...")
    ip_url = "http://httpbin.org/ip"
    
    # Proxy ile istek at
    r = requests.get(ip_url, proxies=proxies, timeout=10)
    print(f"✅ TOR BAĞLANTISI BAŞARILI!")
    print(f"🌍 Görünen Sahte IP (Tor Exit Node): {r.json()['origin']}")
    
    # .onion sitesine erişim (Örn: Facebook Onion)
    onion_url = "https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion/"
    print(f"\nBağlanılıyor: {onion_url} ...")
    r_onion = requests.get(onion_url, proxies=proxies)
    print(f"Statü Kodu: {r_onion.status_code} (Erişim Açık)")
    
except Exception as e:
    print(f"❌ Hata: Tor Browser açık mı? Port 9150 mi 9050 mi kontrol et. Hata: {e}")