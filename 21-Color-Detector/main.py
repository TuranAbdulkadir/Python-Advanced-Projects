import cv2
import pandas as pd

# Kamera başlat
cap = cv2.VideoCapture(0)

# Değişkenler
clicked = False
r = g = b = xpos = ypos = 0

def draw_function(event, x, y, flags, param):
    global b, g, r, xpos, ypos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        xpos = x
        ypos = y
        # O anki kareden rengi al (global frame kullanacağız)
        b, g, r = frame[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('Color Detector')
cv2.setMouseCallback('Color Detector', draw_function)

print("Kamera açıldı! Bir yere ÇİFT TIKLA rengini öğren. Çıkış için 'ESC'.")

while True:
    ret, frame = cap.read()
    if not ret: break
    
    # Eğer bir yere tıklandıysa, ekranda bilgi kutusunu sürekli göster
    if clicked:
        # Ekrana renkli bir bar çiz (Dikdörtgen)
        cv2.rectangle(frame, (20, 20), (750, 60), (b, g, r), -1)
        
        # Renk kodlarını metin olarak hazırla
        text = f"RGB: ({r}, {g}, {b})"
        
        # Yazıyı ekle
        cv2.putText(frame, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Eğer renk çok açıksa yazıyı siyah yap ki okunsun
        if r + g + b >= 600:
            cv2.putText(frame, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
            
        # DİKKAT: Burada 'clicked = False' satırını kaldırdık!
        # Böylece sen yeni bir yere tıklayana kadar yazı ekranda kalacak.

    cv2.imshow('Color Detector', frame)
    
    if cv2.waitKey(20) & 0xFF == 27: # ESC tuşu ile çıkış
        break

cap.release()
cv2.destroyAllWindows()