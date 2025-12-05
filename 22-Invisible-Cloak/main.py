import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# KULLANIM TALİMATI
print("--- GÖRÜNMEZLİK PELERİNİ (MAVİ) ---")
print("1. Kameranın karşısından ÇEKİL.")
print("2. Arka planı kaydetmem için 3 saniye bekle...")
time.sleep(3) 

background = 0

# Arka planı hafızaya alıyoruz (Sen yokken)
for i in range(60):
    ret, background = cap.read()

background = np.flip(background, axis=1)
print("✅ Arka plan kaydedildi! Şimdi MAVİ bezini alıp gelebilirsin.")

while (cap.isOpened()):
    ret, img = cap.read()
    if not ret: break
    img = np.flip(img, axis=1)
    
    # Görüntüyü HSV formatına çevir (Renk tespiti için en iyisi)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # --- MAVİ RENK AYARLARI ---
    # Mavi rengin ton aralığı (Hue: 90-130 arası genelde mavidir)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Mavi olan yerleri maskele (seç)
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Görüntüdeki pürüzleri temizle (Daha pürüzsüz görünmezlik için)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    
    # Maskenin tersini al (Mavi olmayan yerler)
    mask2 = cv2.bitwise_not(mask1)
    
    # 1. Adım: Mavi olan yerlere "Kaydettiğimiz Arka Planı" yapıştır
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    
    # 2. Adım: Mavi olmayan yerlere "Şu anki Görüntüyü" yapıştır
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    
    # İkisini birleştir = SİHİR!
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    cv2.imshow("Invisible Cloak (Blue)", final_output)
    
    if cv2.waitKey(10) == ord('q'): break

cap.release()
cv2.destroyAllWindows()