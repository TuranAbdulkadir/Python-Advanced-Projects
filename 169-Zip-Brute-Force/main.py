import zipfile
import os

print("--- ZIP PASSWORD CRACKER ---")
zip_file = "gizli.zip" 
wordlist = ["123456", "password", "1234", "admin", "secret", "root"]

# Test dosyası yoksa uyarı ver
if not os.path.exists(zip_file):
    print(f"HATA: '{zip_file}' bulunamadı. Lütfen şifreli bir zip dosyası koyun.")
else:
    with zipfile.ZipFile(zip_file) as zf:
        print(f"[*] Saldırı Başlıyor: {zip_file}")
        for password in wordlist:
            try:
                zf.extractall(pwd=password.encode('utf-8'))
                print(f"\n[+] ŞİFRE BULUNDU: {password}")
                print("[+] Dosya başarıyla açıldı.")
                break
            except:
                print(f"[-] Hatalı: {password}")