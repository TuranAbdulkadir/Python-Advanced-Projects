import requests

domain = input("Hedef Domain (google.com): ")
print("--- SUBDOMAIN TARAMASI BAŞLIYOR ---")

# Basit bir wordlist oluşturuyoruz (Normalde binlerce olur)
sub_list = ["admin", "mail", "blog", "dev", "shop", "test", "portal", "secure", "vpn"]

for sub in sub_list:
    url = f"https://{sub}.{domain}"
    try:
        requests.get(url, timeout=2)
        print(f"✅ BULUNDU: {url}")
    except requests.ConnectionError:
        pass # Bulunamadıysa sessiz kal

print("--- Tarama Bitti ---")