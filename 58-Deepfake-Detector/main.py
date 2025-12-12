import cv2

print("--- DEEPFAKE ANALYZER ---")
video_path = input("Video dosyasını sürükle: ")
cap = cv2.VideoCapture(video_path)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: break
    frame_count += 1
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Bulanıklık/Yapaylık testi
    score = cv2.Laplacian(gray, cv2.CV_64F).var()
    
    if frame_count % 30 == 0:
        print(f"Kare {frame_count}: Keskinlik Skoru {int(score)}")

print("Analiz Bitti. Düşük skorlar yapaylık belirtisi olabilir.")