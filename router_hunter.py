from scapy.all import conf, srp, Ether, ARP
import socket
import sys

# --- THE ROUTER HUNTER: STAGE 1 (DISCOVERY) ---
# AMAÇ: Ağın varsayılan ağ geçidini (Gateway) tespit etmek.

def get_gateway_ip():
    print("-" * 50)
    print("[*] AĞIN PATRONU (GATEWAY) ARANIYOR...")
    
    # Scapy'nin kendi ayarlarından Gateway IP'sini çek
    # conf.route.route("0.0.0.0")[2] komutu, internete çıkan yolu verir.
    gateway_ip = conf.route.route("0.0.0.0")[2]
    
    print(f"[+] BULUNDU: Gateway IP Adresi -> {gateway_ip}")
    return gateway_ip

def get_mac(ip):
    # IP adresinin fiziksel (MAC) adresini bul
    ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=0)
    if ans:
        return ans[0][1].hwsrc
    return None

if __name__ == "__main__":
    # 1. Gateway IP'sini bul
    target_router = get_gateway_ip()
    
    # 2. Gateway MAC adresini bul
    router_mac = get_mac(target_router)
    print(f"[+] MAC Adresi: {router_mac}")
    print("-" * 50)
    # ... (Yukarıdaki kodun devamı)

def scan_router_ports(router_ip):
    print(f"\n[*] {router_ip} ÜZERİNDEKİ YÖNETİM KAPILARI TARANIYOR...")
    
    # En kritik yönetim portları
    critical_ports = [21, 22, 23, 80, 443, 8080, 8443]
    
    open_ports = []
    
    for port in critical_ports:
        # Gerçek bir soket bağlantısı dene
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # 1 saniye bekle
        
        result = sock.connect_ex((router_ip, port))
        
        if result == 0:
            print(f"[!!!] AÇIK PORT BULUNDU: {port} (Riskli!)")
            open_ports.append(port)
        else:
            # Kapalıysa ekrana basma, kalabalık etmesin
            pass
            
        sock.close()
    
    return open_ports

if __name__ == "__main__":
    # ... (Önceki main kodları) ...
    
    # 3. Portları Tara
    open_doors = scan_router_ports(target_router)
    # ... (Yukarıdaki kodun devamı)

import requests

def identify_router(router_ip, ports):
    print(f"\n[*] CİHAZ KİMLİĞİ TESPİT EDİLİYOR...")
    
    # Eğer 80 veya 8080 açıks web arayüzüne istek at
    if 80 in ports or 8080 in ports:
        target_url = f"http://{router_ip}"
        try:
            # Gerçek bir HTTP isteği gönder
            response = requests.get(target_url, timeout=3)
            
            # Sunucu bilgisini (Server Header) çek
            server_header = response.headers.get('Server')
            auth_header = response.headers.get('WWW-Authenticate')
            
            print(f"[+] Web Sunucusu Başlığı: {server_header}")
            
            if auth_header:
                print(f"[+] Giriş Tipi: {auth_header}")
                # Genelde burada "Realm=TP-LINK" gibi marka yazar
                
            print(f"[+] Sayfa Başlığı: {response.text.split('<title>')[1].split('</title>')[0]}")
            
        except Exception as e:
            print(f"[-] Kimlik alınamadı: {e}")
            
    else:
        print("[-] Web portları kapalı, kimlik tespiti zor.")

if __name__ == "__main__":
    # ... (Önceki main kodları) ...
    
    # 4. Kimliği Belirle
    identify_router(target_router, open_doors)