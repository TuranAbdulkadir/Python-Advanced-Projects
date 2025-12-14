import zipfile
import itertools

print("--- REAL ZIP CRACKER ---")
zip_name = "sifreli.zip" # Klasöre şifreli bir zip koy
# Demo için oluşturmadıysan hata verir, kendi zipini koy.

# Basit karakter seti (Gerçek hayatta wordlist kullanılır)
chars = "0123456789" 

try:
    zip_file = zipfile.ZipFile(zip_name)
    print(f"{zip_name} analiz ediliyor... (Sadece rakam deneniyor)")
    
    found = False
    for i in range(1, 5): # 1 ile 4 hane arası dene
        if found: break
        for pwd in itertools.product(chars, repeat=i):
            password = "".join(pwd)
            try:
                zip_file.extractall(pwd=password.encode())
                print(f"\n🔥 ŞİFRE KIRILDI: {password}")
                found = True
                break
            except:
                pass # Yanlış şifre
                
    if not found: print("Şifre basit kombinasyonlarda bulunamadı.")
    
except FileNotFoundError:
    print(f"❌ '{zip_name}' bulunamadı! Lütfen klasöre şifreli bir zip dosyası koy.")