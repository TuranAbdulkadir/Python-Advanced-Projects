from PIL import Image
from PIL.ExifTags import TAGS

print("--- REAL EXIF DATA EXTRACTOR ---")
img_path = input("Resim dosyası adı (örn: foto.jpg): ")

try:
    image = Image.open(img_path)
    exif_data = image._getexif()
    
    if exif_data:
        print("\n🔍 Gizli Veriler Bulundu:")
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name in ['Make', 'Model', 'DateTime', 'GPSInfo']:
                print(f"📌 {tag_name}: {value}")
    else:
        print("Bu resimde EXIF verisi yok (Temizlenmiş).")
        
except FileNotFoundError:
    print("Resim bulunamadı.")