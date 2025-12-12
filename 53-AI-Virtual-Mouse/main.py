import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

print("🔵 MAVİ NESNE İLE MOUSE KONTROLÜ AKTİF!")
print("Mavi bir cismi kameraya göster...")

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    
    # Rengi algıla (HSV Formatında Mavi)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000: # Gürültüyü engelle
            x, y, w_box, h_box = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w_box, y+h_box), (0, 255, 0), 2)
            
            # Mouse Hareket Ettir
            target_x = np.interp(x, [0, w], [0, screen_width])
            target_y = np.interp(y, [0, h], [0, screen_height])
            pyautogui.moveTo(target_x, target_y)

    cv2.imshow("Color Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()