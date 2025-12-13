import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("--- PHISHING CAMPAIGN SIMULATOR ---")
print("Bu araç sadece yetkili olduğunuz sistemlerde test içindir!")

smtp_server = "smtp.gmail.com" # Örnek
port = 587
sender_email = input("Gönderici Email: ")
password = input("Uygulama Şifresi: ")

targets = ["kurban1@sirket.com", "kurban2@sirket.com"] # Hedef Listesi

subject = "ACİL: Hesabınız Kapatılacak!"
body = """
Sayın Kullanıcı,
Hesabınızda şüpheli işlem tespit edildi.
Lütfen hemen aşağıdaki linke tıklayıp şifrenizi yenileyin:
http://fake-site.com/login

Saygılar,
Güvenlik Ekibi
"""

def send_phish(target):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = target
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Gerçek gönderim için SMTP sunucusu gerekir
        # server = smtplib.SMTP(smtp_server, port)
        # server.starttls()
        # server.login(sender_email, password)
        # server.sendmail(sender_email, target, msg.as_string())
        # server.quit()
        print(f"📧 [SİMÜLASYON] Mail gönderildi -> {target}")
    except Exception as e:
        print(f"Hata: {e}")

for t in targets:
    send_phish(t)
print("Kampanya Tamamlandı.")