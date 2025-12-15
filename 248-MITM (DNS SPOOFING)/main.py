print("--- DNS SPOOFING (YÖNLENDİRME) ---")
# Kurban 'google.com' yazıyor sanıyor, ama bize geliyor.

def dns_cevapla(paket):
    # Kurbanın DNS isteği: "google.com nerede?"
    istenen_site = "google.com"
    
    # Bizim yalan cevabımız:
    sahte_ip = "192.168.1.100" # Hacker'ın IP'si
    
    print(f"[*] İstek Yakalandı: {istenen_site}")
    print(f"[!] Yalan Cevap Gönderiliyor: {istenen_site} -> {sahte_ip}")
    print("[+] Kurban şu an bizim hazırladığımız siteye bağlanıyor...")

if __name__ == "__main__":
    while True:
        # Scapy ile ağ dinlenir ve cevap verilir
        dns_cevapla("paket_simulasyonu")
        break