import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

print("🤟 İŞARET DİLİ AI AKTİF")

while True:
    ret, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_lms, mp_hands.HAND_CONNECTIONS)
            
            thumb = hand_lms.landmark[4].y
            index = hand_lms.landmark[8].y
            
            if index < hand_lms.landmark[5].y and thumb < hand_lms.landmark[2].y:
                cv2.putText(img, "SELAM / OK", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Sign Language", img)
    if cv2.waitKey(1) == ord('q'): break

cap.release()
cv2.destroyAllWindows()