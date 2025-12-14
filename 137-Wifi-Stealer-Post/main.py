import subprocess
import re

print("--- WIFI PASSWORD DUMP ---")

# Wifi Profillerini al
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode(errors='ignore')
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        # Her profilin şifresini al
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode(errors='ignore')
        
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            # Şifreyi temiz metin (cleartext) olarak çek
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode(errors='ignore')
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            
            if password == None:
                wifi_list.append(f"{name} : [Şifre Bulunamadı]")
            else:
                wifi_list.append(f"{name} : {password[1]}")

print("\n🔑 BULUNAN WİFİ ŞİFRELERİ:")
with open("wifi_passwords.txt", "w") as f:
    for item in wifi_list:
        print(item)
        f.write(item + "\n")

print("\n✅ 'wifi_passwords.txt' dosyasına kaydedildi.")