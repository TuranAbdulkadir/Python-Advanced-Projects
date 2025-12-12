import cv2
import numpy as np

# Klasöre 'belge.jpg' adında yamuk bir kağıt fotosu koy
img = cv2.imread('belge.jpg')

if img is None:
    print("❌ 'belge.jpg' bulunamadı!")
else:
    # Resmi gri yap ve kenarları bul
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    
    # Perspektif düzeltme (Basitleştirilmiş koordinatlar - dinamik yapılabilir)
    # Köşe noktaları (Sol-Üst, Sağ-Üst, Sol-Alt, Sağ-Alt)
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 400], [300, 400]])
    
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (300, 400))
    
    cv2.imshow("Orjinal", img)
    cv2.imshow("Taranmis Belge", result)
    print("✅ Belge tarandı ve düzeltildi!")
    cv2.waitKey(0)
    cv2.destroyAllWindows()