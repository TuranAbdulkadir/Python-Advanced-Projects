import time
from datetime import datetime as dt

# Windows Hosts Dosyası
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

print("--- WEBSITE BLOCKER ACTIVATED ---")
print("Press CTRL+C to stop.")

try:
    while True:
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        time.sleep(5)
except KeyboardInterrupt:
    print("Restoring hosts file...")