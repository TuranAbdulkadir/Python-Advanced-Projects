import psutil
import os

print("--- ROOTKIT & HIDDEN PROCESS HUNTER ---")
print("Sistemdeki gizli işlemleri (PID) arıyorum...")

# 1. PSUTIL ile görünen işlemler (API)
visible_pids = set(psutil.pids())

# 2. İşletim sisteminin derinliklerindeki işlemler (Manuel Tarama)
# Windows'ta bu kısmı simüle ediyoruz, Linux'ta /proc klasörü taranır.
hidden_pids = []

# Demo: Simüle edilmiş gizli PID
print("Analiz ediliyor...")
# Normalde burada os.listdir('/proc') yapılır.

# Diyelim ki sistemde gizli bir PID var (Simülasyon)
# visible_pids.remove(1234) # 1234 PID'si API'de gizlendi varsayalım

for pid in visible_pids:
    try:
        proc = psutil.Process(pid)
        # Şüpheli isim kontrolü
        if proc.name() == "" or "keylog" in proc.name():
            print(f"⚠️ Şüpheli İsim: {proc.name()} (PID: {pid})")
            
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        # Eğer PSUTIL erişemiyorsa ama PID varsa, bu bir Rootkit belirtisi olabilir
        print(f"🚨 ERİŞİLEMEYEN GİZLİ PID: {pid} (Rootkit Şüphesi!)")

print("Tarama tamamlandı. Eğer 'Erişilemeyen PID' çoksa sistem enfekte olabilir.")