import cv2
import numpy as np
import pyautogui

print("--- SCREEN MELTER EFFECT (Press Q to stop) ---")

# Ekran görüntüsü al
screenshot = pyautogui.screenshot()
frame = np.array(screenshot)
frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
height, width, _ = frame.shape

# Eritme efekti döngüsü
while True:
    # Rastgele sütunları aşağı kaydır
    for i in range(100): # Her karede 100 sütun kaydır
        x = np.random.randint(0, width)
        # Sütunu al ve 10 piksel aşağı it
        col = frame[:, x]
        frame[:, x] = np.roll(col, np.random.randint(1, 5))
        
    cv2.imshow("HACKED - SCREEN MELTER", frame)
    # Tam ekran yap
    cv2.setWindowProperty("HACKED - SCREEN MELTER", cv2.WND_PROP_TOPMOST, 1)
    
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()