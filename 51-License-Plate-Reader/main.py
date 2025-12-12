import cv2
import easyocr
import numpy as np

print("--- POLİS PLAKA TANIMA SİSTEMİ ---")
print("Görüntü işleniyor...")

# EasyOCR okuyucuyu yükle (Türkçe ve İngilizce)
reader = easyocr.Reader(['en', 'tr'], gpu=False)

# Resmi yükle
img = cv2.imread('araba.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Plakayı bul ve oku
result = reader.readtext(gray)

for (bbox, text, prob) in result:
    print(f"🚘 TESPİT EDİLEN PLAKA: {text.upper()} (Güven: %{prob*100:.2f})")
    
    # Plakayı kare içine al
    (tl, tr, br, bl) = bbox
    tl = (int(tl[0]), int(tl[1]))
    br = (int(br[0]), int(br[1]))
    cv2.rectangle(img, tl, br, (0, 255, 0), 5)
    cv2.putText(img, text.upper(), (tl[0], tl[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

cv2.imshow("ANPR System", img)
cv2.waitKey(0)
cv2.destroyAllWindows()