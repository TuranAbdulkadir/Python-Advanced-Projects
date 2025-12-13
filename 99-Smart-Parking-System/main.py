import cv2
import pickle
import numpy as np

# Park yeri koordinatları (Daha önce belirlenmiş olmalı, demo için rastgele)
# posList = pickle.load(open("carParkPos", "rb")) 
posList = [(50, 50), (150, 50), (250, 50)] # Örnek koordinatlar
width, height = 80, 40

print("--- AI SMART PARKING SYSTEM ---")

def check_parking_space(img, img_processed):
    space_counter = 0
    
    for pos in posList:
        x, y = pos
        # O park yerindeki pikselleri kes
        img_crop = img_processed[y:y+height, x:x+width]
        # Beyaz piksel sayısına bak (Kenar tespiti sonrası)
        count = cv2.countNonZero(img_crop)
        
        if count < 500: # Eşik değer (Az piksel = Boş)
            color = (0, 255, 0)
            space_counter += 1
            status = "BOS"
        else:
            color = (0, 0, 255)
            status = "DOLU"
            
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), color, 2)
        cv2.putText(img, status, (x, y+height-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    print(f"Boş Yer Sayısı: {space_counter}/{len(posList)}")

# Siyah ekran üzerinde demo
img = np.zeros((300, 400, 3), dtype=np.uint8)
# Dolu olması için biraz beyazlık ekleyelim
cv2.rectangle(img, (150, 50), (230, 90), (255, 255, 255), -1) 

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)

check_parking_space(img, img_thresh)
cv2.imshow("Parking AI", img)
cv2.waitKey(0)
cv2.destroyAllWindows()