import requests

print("--- SUBDOMAIN TAKEOVER SCANNER ---")

target_domain = input("Hedef Domain (örn: criyus.com): ")
# Yaygın alt alan adları
subs = ["dev", "test", "staging", "blog", "shop", "app", "admin"]

signatures = {
    "GitHub": "There isn't a GitHub Pages site here",
    "Heroku": "No such app",
    "AWS": "The specified bucket does not exist"
}

print("[*] Tarama Başlıyor...")

for sub in subs:
    url = f"http://{sub}.{target_domain}"
    try:
        r = requests.get(url, timeout=3)
        print(f"[+] {url} - Aktif (Kod: {r.status_code})")
        
        # Takeover Kontrolü
        for service, error in signatures.items():
            if error in r.text:
                print(f"🔥🔥 POTANSİYEL TAKEOVER BULUNDU! ({service})")
                print(f"   Bu adresi hemen gidip {service} üzerinde kendi adına kaydet!")
    except:
        pass