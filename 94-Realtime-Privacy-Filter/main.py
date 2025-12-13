import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

print("--- GİZLİLİK FİLTRESİ (Yüzler Sansürleniyor) ---")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        # Yüz bölgesini al
        roi = frame[y:y+h, x:x+w]
        # Bulanıklaştır (Blur)
        roi = cv2.GaussianBlur(roi, (99, 99), 30)
        # Orijinal kareye geri koy
        frame[y:y+h, x:x+w] = roi
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, "GIZLI", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow('Privacy Filter', frame)
    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()