import os
import sys
import psutil # pip install psutil

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod ortam analizi (Evasion) yapar.")

print("--- WEAPONIZED EVASION ---")

def is_virtual_machine():
    checks = []
    
    # 1. DONANIM KONTROLLERİ (Weaponized Part)
    
    # A. Disk Boyutu: VM'ler genelde 60GB civarıdır. Gerçek PC 256GB+ olur.
    hdd_usage = psutil.disk_usage('/')
    total_gb = hdd_usage.total / (1024**3)
    if total_gb < 100: 
        checks.append("Disk Küçük (VM?)")
        
    # B. RAM Miktarı: 4GB altı şüphelidir.
    mem = psutil.virtual_memory()
    if mem.total < 4 * (1024**3):
        checks.append("RAM Düşük (VM?)")
        
    # C. CPU Çekirdeği: 2 çekirdekten azsa kesin VM'dir.
    if os.cpu_count() < 2:
        checks.append("CPU Az (VM?)")
        
    # D. MAC Adresi: VMware/VirtualBox özel MAC adresleri.
    # (Kod detayı...)
    
    if checks:
        print(f"[-] Analiz Ortamı Tespit Edildi: {checks}")
        return True
    return False

def main():
    if is_virtual_machine():
        print("[*] Mod: MASUM")
        print("Sadece not defterini aç ve kapat. (Analisti kandır)")
    else:
        print("💀 Mod: SALDIRI")
        print("Şifreleme modülü başlatılıyor...")

if __name__ == "__main__":
    main()