import cv2

cap = cv2.VideoCapture(0)

print("--- WEBCAM FILTERS ---")
print("Press '1': Original")
print("Press '2': Grayscale (Siyah-Beyaz)")
print("Press '3': Edge Detection (Çizim Modu)")
print("Press 'q': QUIT")

mode = 1

while True:
    ret, frame = cap.read()
    if not ret: break
    
    if mode == 2:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    elif mode == 3:
        # Canny algoritması ile kenarları bulur
        frame = cv2.Canny(frame, 100, 200)
    
    cv2.imshow('Advanced Camera', frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'): break
    elif key == ord('1'): mode = 1
    elif key == ord('2'): mode = 2
    elif key == ord('3'): mode = 3

cap.release()
cv2.destroyAllWindows()