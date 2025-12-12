import requests

target = input("Analiz edilecek site (https://google.com): ")

print("\n--- SUNUCU İSTİHBARATI ---")
try:
    response = requests.get(target)
    headers = response.headers
    
    print(f"Sunucu: {headers.get('Server', 'Gizli')}")
    print(f"Teknoloji: {headers.get('X-Powered-By', 'Bilinmiyor')}")
    print(f"Çerezler: {len(response.cookies)} adet")
    print(f"Güvenlik Politikası: {headers.get('Strict-Transport-Security', 'Yok')}")
    print("-" * 30)
    
    for key, value in headers.items():
        print(f"{key}: {value}")
        
except Exception as e:
    print("Bağlantı Hatası:", e)