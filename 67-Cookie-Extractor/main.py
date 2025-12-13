import browser_cookie3
import requests

print("--- TARAYICI ÇEREZ (COOKIE) ANALİZİ ---")
print("Chrome çerezleri çekiliyor...")

try:
    # Chrome çerezlerini al
    cookies = browser_cookie3.chrome()
    
    print(f"Toplam {len(cookies)} çerez bulundu.")
    print("İlk 5 Çerez Örneği:")
    
    count = 0
    for cookie in cookies:
        if count < 5:
            print(f"Domain: {cookie.domain} | Name: {cookie.name} | Value: {cookie.value[:20]}...")
            count += 1
        else:
            break
            
    # Bu çerezlerle bir siteye istek atma simülasyonu
    # url = "https://facebook.com"
    # requests.get(url, cookies=cookies)
    
except Exception as e:
    print(f"Hata: {e}")
    print("Not: Tarayıcının kapalı olduğundan emin ol.")