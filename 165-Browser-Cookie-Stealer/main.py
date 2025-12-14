import os
import shutil
import sqlite3
import win32crypt 

print("--- CHROME COOKIE DUMPER ---")

db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Network", "Cookies")
filename = "Cookies.db"

if not os.path.isfile(db_path):
    print("Chrome veritabanı bulunamadı.")
    exit()

shutil.copyfile(db_path, filename)
db = sqlite3.connect(filename)
cursor = db.cursor()
cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")

print(f"{'DOMAIN':<25} | {'COOKIE NAME':<20} | {'DATA'}")
print("-" * 60)

for host_key, name, encrypted_value in cursor.fetchall():
    print(f"{host_key:<25} | {name:<20} | [ENCRYPTED DATA]")

db.close()
os.remove(filename)
print("\n[!] Chrome çerez veritabanı başarıyla okundu.")