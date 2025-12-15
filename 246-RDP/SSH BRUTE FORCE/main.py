import socket
import time

print("--- RDP/SSH BRUTE FORCE ---")
# Kurbanın haberi bile yok, biz kapıyı zorluyoruz.

target_ip = "192.168.1.20"
users = ["admin", "user", "root"]
passwords = ["123456", "password", "admin123", "toor"]

def kapiyi_zorla():
    for user in users:
        for pwd in passwords:
            # Simülasyon: Bağlanıp şifreyi deniyoruz
            print(f"[*] Deneniyor: {user} / {pwd} -> {target_ip}")
            time.sleep(0.1) # Çok hızlı denersek banlanırız
            
            # Eğer şifre tutarsa:
            if pwd == "123456": # Örnek doğru şifre
                print(f"\n[!!!] GİRİŞ BAŞARILI! Şifre bulundu: {pwd}")
                print("Artık kurbanın masaüstü benim ekranımda.")
                return

if __name__ == "__main__":
    kapiyi_zorla()