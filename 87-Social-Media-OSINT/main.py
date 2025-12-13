import requests

print("--- SOCIAL MEDIA OSINT ---")
username = input("Aranacak Kullanıcı Adı: ")

sites = {
    "Instagram": f"https://www.instagram.com/{username}",
    "Twitter": f"https://twitter.com/{username}",
    "GitHub": f"https://github.com/{username}",
    "Facebook": f"https://www.facebook.com/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Medium": f"https://medium.com/@{username}"
}

print(f"\n'{username}' taranıyor...\n")

for site, url in sites.items():
    try:
        r = requests.get(url)
        if r.status_code == 200:
            print(f"✅ BULUNDU: {site} -> {url}")
        else:
            print(f"❌ Yok: {site}")
    except:
        print(f"❓ Hata: {site}")

print("\nTarama Bitti.")