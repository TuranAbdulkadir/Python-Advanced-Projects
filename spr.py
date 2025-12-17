from scapy.all import ARP, Ether, srp
import sys

# --- STAGE 1: NETWORK SCANNER ---
# AMAÇ: Ağdaki cihazların IP ve MAC adreslerini bulmak.

def scan_network(ip_range):
    print(f"[*] Ağ Taranıyor: {ip_range} ...")
    
    # 1. ARP İsteği (Kim orada?)
    arp = ARP(pdst=ip_range)
    # 2. Ethernet Çerçevesi (Broadcast)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # 3. Gönder ve Cevapları Al (srp fonksiyonu burada)
    # timeout=2: 2 saniye bekle, cevap gelmezse geç.
    result = srp(packet, timeout=2, verbose=0)[0]

    # 4. Sonuçları Listele
    print("-" * 40)
    print("IP ADRESİ\t\tMAC ADRESİ")
    print("-" * 40)
    
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
        print(f"{received.psrc}\t\t{received.hwsrc}")
    
    return clients

if __name__ == "__main__":
    # Kendi ağ aralığını yaz (Genelde 192.168.1.1/24)
    target_ip = "192.168.1.1/24" 
    scan_network(target_ip)