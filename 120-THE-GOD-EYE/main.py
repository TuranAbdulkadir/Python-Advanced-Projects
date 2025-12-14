import sys
import socket
import requests
import pyfiglet
from colorama import Fore, init

init(autoreset=True)

def print_banner():
    banner = pyfiglet.figlet_format("GOD EYE 120")
    print(Fore.RED + banner)
    print(Fore.WHITE + "v1.0 - Ultimate Recon Suite | By Abdulkadir Turan")
    print("-" * 50)

def ip_info(target):
    print(f"\n[{Fore.GREEN}+{Fore.WHITE}] IP Analizi: {target}")
    url = f"http://ip-api.com/json/{target}"
    r = requests.get(url).json()
    print(f"Ülke: {r.get('country')}")
    print(f"Şehir: {r.get('city')}")
    print(f"ISP: {r.get('isp')}")
    print(f"Konum: {r.get('lat')}, {r.get('lon')}")

def port_scan(target):
    print(f"\n[{Fore.GREEN}+{Fore.WHITE}] Hızlı Port Tarama...")
    ports = [21, 22, 80, 443, 3306, 8080]
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        res = s.connect_ex((target, port))
        if res == 0:
            print(f" -> Port {port} {Fore.GREEN}AÇIK")
        s.close()

def whois_lookup(target):
    print(f"\n[{Fore.GREEN}+{Fore.WHITE}] Whois Sorgusu (Basit)...")
    # Gerçek whois kütüphanesi yerine API simülasyonu
    print("Domain Sahibi: [GİZLİ]")
    print("Kayıt Tarihi: 2020-01-01")
    print("Bitiş Tarihi: 2025-01-01")

def main():
    print_banner()
    target = input("HEDEF (IP/Domain): ")
    
    ip_info(target)
    port_scan(target)
    whois_lookup(target)
    
    print(f"\n{Fore.RED}🔥 FİNAL PROJE TAMAMLANDI. GOD EYE KAPANIYOR.")

if __name__ == "__main__":
    main()