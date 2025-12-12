import cv2
from datetime import datetime

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

def mark_attendance(name):
    with open('Yoklama.csv', 'a+') as f:
        now = datetime.now()
        dtString = now.strftime('%H:%M:%S')
        f.write(f'\n{name},{dtString}')
        print(f"✅ {name} kaydedildi.")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, "Ogrenci", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        mark_attendance("Ogrenci_1") # Demo isim
        
    cv2.imshow('Smart Attendance', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()