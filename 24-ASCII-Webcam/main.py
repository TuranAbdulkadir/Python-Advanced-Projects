import cv2
import os

# ASCII Karakter seti
CHARS = ' .:-=+*#%@'

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Görüntüyü küçült ve gri yap
    small_frame = cv2.resize(frame, (100, 40))
    gray_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2GRAY)
    
    # Her pikseli karaktere çevir
    ascii_art = ""
    for row in gray_frame:
        for pixel in row:
            index = int(pixel / 255 * (len(CHARS) - 1))
            ascii_art += CHARS[index]
        ascii_art += "\n"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ascii_art)

cap.release()