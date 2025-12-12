import requests
from bs4 import BeautifulSoup
import os

url = input("Resimlerin çalınacağı site (örn: https://xkcd.com): ")
os.makedirs('downloaded_images', exist_ok=True)

print("Site taranıyor...")
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
images = soup.find_all('img')

print(f"Toplam {len(images)} resim bulundu. İndiriliyor...")

for i, img in enumerate(images):
    try:
        img_url = img['src']
        if not img_url.startswith('http'): 
            img_url = url + img_url # Relative link düzeltmesi
            
        img_data = requests.get(img_url).content
        
        with open(f"downloaded_images/img_{i}.jpg", 'wb') as handler:
            handler.write(img_data)
        print(f"✅ İndirildi: img_{i}.jpg")
    except:
        print(f"❌ Hata: Resim {i} indirilemedi")

print("Tüm işlemler tamamlandı!")