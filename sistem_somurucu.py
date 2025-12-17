import subprocess
import platform
import os

# --- SYSTEM RECONNAISSANCE ---
def get_system_info():
    # Sonuçları scriptin olduğu yere (USB'ye) kaydet
    output_file = "SISTEM_BILGISI.txt"
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"--- HEDEF SISTEM RAPORU ---\n")
        f.write(f"Bilgisayar Adı: {platform.node()}\n")
        f.write(f"İşletim Sistemi: {platform.system()} {platform.release()}\n")
        f.write(f"İşlemci: {platform.processor()}\n\n")
        
        try:
            # Windows 'systeminfo' komutunu çalıştır
            sys_info = subprocess.check_output("systeminfo", shell=True).decode('utf-8', errors='ignore')
            f.write(sys_info)
        except Exception as e:
            f.write(f"Detaylı bilgi alınamadı: {e}")

if __name__ == "__main__":
    get_system_info()