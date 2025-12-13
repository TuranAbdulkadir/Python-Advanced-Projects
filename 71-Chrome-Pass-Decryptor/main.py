import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime

print("--- CHROME PASSWORD FORENSICS ---")

def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # Base64 şifreyi çöz ve DPAPI ile ham anahtarı al
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        return "(Şifre çözülemedi)"

def main():
    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                            "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename) # Veritabanını kopyala (Kilit hatası olmasın diye)

    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute("select origin_url, username_value, password_value, date_created from logins order by date_created")

    print(f"{'URL':<50} | {'KULLANICI':<30} | {'ŞİFRE'}")
    print("-" * 100)

    for row in cursor.fetchall():
        url = row[0]
        username = row[1]
        password = decrypt_password(row[2], key)
        
        if username or password:
            if len(url) > 50: url = url[:47] + "..."
            print(f"{url:<50} | {username:<30} | {password}")

    cursor.close()
    db.close()
    os.remove(filename)

if __name__ == "__main__":
    main()