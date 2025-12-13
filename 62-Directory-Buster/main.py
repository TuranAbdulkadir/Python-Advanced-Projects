import requests
import sys

print("--- DIRECTORY BUSTER ---")
target_url = input("Hedef URL (örn: http://testphp.vulnweb.com): ")
wordlist_file = "wordlist.txt"

try:
    with open(wordlist_file, "r") as file:
        words = file.readlines()
        
    print(f"Toplam {len(words)} kelime denenecek...")
    
    for word in words:
        word = word.strip()
        url = f"{target_url}/{word}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"✅ BULUNDU (200): {url}")
            elif response.status_code == 403:
                print(f"🔒 YASAKLI (403): {url}")
        except KeyboardInterrupt:
            sys.exit()
        except:
            pass
            
except FileNotFoundError:
    print("❌ wordlist.txt bulunamadı!")