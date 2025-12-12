import cv2
import winsound # Sadece Windows için alarm sesi

cap = cv2.VideoCapture(0)
print("🔴 GÜVENLİK KAMERASI AKTİF (Çıkış: q)")

while cap.isOpened():
    # İki kare arasındaki farkı al
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 900: # Küçük hareketleri yoksay
            continue
        
        # Hareket algılandı!
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame1, "HAREKET ALGILANDI!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        
        # Alarm çal (Sistem bip sesi)
        # winsound.Beep(1000, 200) 

    cv2.imshow("Security Feed", frame1)
    if cv2.waitKey(10) == ord('q'): break

cap.release()
cv2.destroyAllWindows()