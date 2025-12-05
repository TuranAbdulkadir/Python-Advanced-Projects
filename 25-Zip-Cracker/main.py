import zipfile

zip_file = "secret.zip" # Klasörde bu dosya olmalı
password_list = ["1234", "password", "admin", "secret", "123456"] # Denenecek şifreler

print(f"Cracking {zip_file}...")

try:
    with zipfile.ZipFile(zip_file) as zf:
        for password in password_list:
            try:
                zf.extractall(pwd=password.encode())
                print(f"✅ SUCCESS! Password is: {password}")
                break
            except:
                print(f"❌ Failed: {password}")
except FileNotFoundError:
    print("Error: secret.zip not found.")