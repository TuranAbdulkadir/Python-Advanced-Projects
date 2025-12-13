import os
import shutil
import time
import psutil

print("--- USB DATA COPIER (BACKUP BOT) ---")
print("USB bekleniyor...")

def get_usb_drive():
    drives = psutil.disk_partitions()
    for drive in drives:
        if 'removable' in drive.opts:
            return drive.device
    return None

while True:
    usb = get_usb_drive()
    if usb:
        print(f"🔥 USB TESPİT EDİLDİ: {usb}")
        dest_folder = "USB_DUMP"
        if not os.path.exists(dest_folder): os.makedirs(dest_folder)
        
        # USB içindeki dosyaları gez
        for root, dirs, files in os.walk(usb):
            for file in files:
                if file.endswith(('.pdf', '.docx', '.txt')):
                    try:
                        file_path = os.path.join(root, file)
                        shutil.copy(file_path, dest_folder)
                        print(f"Kopyalandı: {file}")
                    except:
                        pass
        print("✅ İşlem Tamam! Çıkarılabilir.")
        break
    time.sleep(2)