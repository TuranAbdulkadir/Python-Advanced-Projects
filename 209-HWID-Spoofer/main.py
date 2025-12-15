import winreg
import uuid
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod sistem kimliklerini kalıcı olarak değiştirir.")

print("--- WEAPONIZED HWID SPOOFER ---")

def spoof_ids():
    new_guid = str(uuid.uuid4())
    print(f"[*] Yeni HWID Üretildi: {new_guid}")
    
    # 1. HEDEF: REGISTRY (Weaponized Part)
    # Simülasyon: print(guid)
    # Gerçek: HKLM (Local Machine) anahtarlarını değiştir.
    
    paths = [
        r"SYSTEM\CurrentControlSet\Control\IDConfigDB\Hardware Profiles\0001",
        r"SOFTWARE\Microsoft\Cryptography",
        r"SYSTEM\CurrentControlSet\Control\SystemInformation"
    ]
    
    try:
        # HwProfileGuid, MachineGuid, ComputerHardwareId değerlerini değiştir
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, paths[0], 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "HwProfileGuid", 0, winreg.REG_SZ, f"{{{new_guid}}}")
        winreg.CloseKey(key)
        
        print("💀 REGISTRY GÜNCELLENDİ.")
        print("Yeniden başlatınca sistem kendini farklı bir PC sanacak.")
        
    except PermissionError:
        print("[-] Yönetici yetkisi gerekli.")

if __name__ == "__main__":
    spoof_ids()