import os

print("--- FILE CARVING (DOSYA KURTARMA) ---")
# Kurtarılacak sürücü veya dosya imajı (Windows'ta fiziksel disk erişimi zordur, demo olarak bir dosyadan kurtarma yapalım)
# Gerçek senaryoda: drive = "\\\\.\\E:" 
filename = input("Taranacak Dosya/Disk İmajı (örn: disk_image.dd): ")

# JPG Başlangıç ve Bitiş İmzaları (Magic Numbers)
JPG_START = b'\xFF\xD8\xFF'
JPG_END = b'\xFF\xD9'

try:
    with open(filename, "rb") as file:
        data = file.read()
        
    start_offset = 0
    count = 0
    
    while True:
        # Başlangıç imzasını bul
        start = data.find(JPG_START, start_offset)
        if start == -1: break
        
        # Bitiş imzasını bul
        end = data.find(JPG_END, start)
        if end == -1: break
        
        # Dosyayı Çıkar
        recovered_data = data[start:end+2]
        with open(f"recovered_{count}.jpg", "wb") as out:
            out.write(recovered_data)
            
        print(f"♻️ Resim Kurtarıldı: recovered_{count}.jpg")
        count += 1
        start_offset = end + 2
        
except FileNotFoundError:
    print("Dosya bulunamadı. (Test için bir hex editörle içine JPG gömülmüş dosya kullanabilirsin)")