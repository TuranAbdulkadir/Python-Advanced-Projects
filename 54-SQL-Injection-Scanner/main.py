import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0"

errors = {"you have an error in your sql syntax;", "warning: mysql", "quoted string not properly terminated"}

def is_vulnerable(response):
    for error in errors:
        if error in response.content.decode().lower():
            return True
    return False

def scan_sql_injection(url):
    print(f"Taranıyor: {url}")
    new_url = f"{url}'" # Payload
    print(f"Test ediliyor: {new_url}")
    
    res = s.get(new_url)
    if is_vulnerable(res):
        print(f"🔥 KRİTİK AÇIK BULUNDU (SQLi): {url}")
    else:
        print("✅ Güvenli.")

target = input("Hedef URL (örn: http://testphp.vulnweb.com/listproducts.php?cat=1): ")
scan_sql_injection(target)