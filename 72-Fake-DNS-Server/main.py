from dnslib import DNSRecord, QTYPE, RR, A
import socket

print("--- FAKE DNS SERVER ---")
print("Tüm trafiği bu IP'ye yönlendiriyorum: 127.0.0.1 (Kendin)")

# Yönlendirilecek Hedef IP (Buraya kendi sahte sitenin IP'sini yaz)
REDIRECT_IP = "127.0.0.1" 

udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udps.bind(('0.0.0.0', 53)) # DNS Portu

print("DNS Sunucusu Dinleniyor... (DNS Ayarlarını 127.0.0.1 yapmalısın)")

try:
    while True:
        data, addr = udps.recvfrom(1024)
        request = DNSRecord.parse(data)
        
        reply = DNSRecord(DNSRecord.header(request.id, qr=1, aa=1, ra=1), q=request.q)
        qname = request.q.qname
        qtype = request.q.qtype
        
        # Her şeyi bizim IP'ye yönlendir (A Kaydı)
        if qtype == QTYPE.A:
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(REDIRECT_IP), ttl=60))
            print(f"Yönlendirildi: {qname} -> {REDIRECT_IP}")
            
        udps.sendto(reply.pack(), addr)
except KeyboardInterrupt:
    print("Kapatıldı.")
except Exception as e:
    print(f"Hata (Yönetici İzni Gerekir): {e}")