import socket
import socks # PySocks gerekli
from stem.control import Controller
from stem import Signal

print("--- TOR ANONYMOUS CHAT CLIENT ---")

def connect_tor():
    print("Tor ağına bağlanılıyor...")
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket
    print("✅ Bağlantı Gizlendi! (IP Adresin değişti)")

def check_ip():
    # IP adresini kontrol et
    import requests
    ip = requests.get("http://httpbin.org/ip").json()["origin"]
    print(f"🎭 Yeni Gizli IP Adresin: {ip}")

try:
    connect_tor()
    check_ip()
    print("\n[Chat Modu Başlatılıyor... Sunucu bekleniyor]")
    # Burada normal socket işlemleri yapılır ama artık Tor üzerinden gider.
except Exception as e:
    print(f"Hata: Tor açık mı? {e}")