import cv2
import numpy as np

# Siyah ekran oluştur
canvas = np.zeros((500, 500, 3), dtype="uint8")

# Normalde görünmeyen ama mavi filtrede parlayan yazı
# Renk kodu (B, G, R) -> (255, 5, 5) insan gözüne siyah gibi görünür ama mavidir
cv2.putText(canvas, "GIZLI MESAJ", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 2, 2), 5)

# Gürültü ekleyerek gizle
noise = np.random.randint(0, 50, (500, 500, 3), dtype='uint8')
hidden_img = cv2.add(canvas, noise)

print("Gizli mesaj oluşturuldu. Sadece Mavi kanalı ayrıştırınca okunabilir.")
cv2.imshow("Gorunmez Murekkep", hidden_img)

# Mavi kanalı göster (Mesaj ortaya çıkar)
blue_channel = hidden_img[:,:,0]
cv2.imshow("Filtre Uygulandi (Desifre)", blue_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()