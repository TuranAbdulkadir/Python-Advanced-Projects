import sys
import os

print("--- ANTI-VM / SANDBOX DETECTOR ---")

def check_vm():
    score = 0
    
    # 1. MAC Adresi Kontrolü (VMware/VirtualBox MAC'leri bellidir)
    # Basitleştirilmiş: Komut çıktısına bak
    mac_output = os.popen('getmac').read()
    if "00-05-69" in mac_output or "08-00-27" in mac_output:
        print("⚠️ VM Tespiti: MAC Adresi şüpheli.")
        score += 1
        
    # 2. Dosya Kontrolü (Guest Additions sürücüleri)
    if os.path.exists("C:\\Windows\\System32\\drivers\\VBoxMouse.sys") or \
       os.path.exists("C:\\Windows\\System32\\drivers\\vm3dmp.sys"):
        print("⚠️ VM Tespiti: Sürücü dosyaları bulundu.")
        score += 2
        
    # 3. Çekirdek Sayısı (Analiz makineleri genelde 1-2 çekirdektir)
    if os.cpu_count() < 2:
        print("⚠️ VM Tespiti: CPU çekirdek sayısı çok düşük.")
        score += 1

    return score

print("Ortam taranıyor...")
risk_level = check_vm()

if risk_level >= 2:
    print("\n🛑 SANAL MAKİNE TESPİT EDİLDİ! KENDİMİ KAPATIYORUM.")
    print("Analizden kaçmak için zararlı kod çalıştırılmadı.")
    sys.exit()
else:
    print("\n✅ ORTAM GÜVENLİ (Gerçek Bilgisayar).")
    print("😈 Zararlı kod çalıştırılıyor...")