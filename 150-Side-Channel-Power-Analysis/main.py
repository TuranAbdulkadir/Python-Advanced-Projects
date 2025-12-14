import time
import random

print("--- SIDE CHANNEL POWER ANALYSIS (Simulation) ---")

secret_key = [1, 0, 1, 1] # Basit RSA Key bitleri

def modular_exponentiation_sim(bit):
    # Eğer bit 1 ise işlemci ÇOK çalışır (Kare + Çarp)
    # Eğer bit 0 ise işlemci AZ çalışır (Sadece Kare)
    if bit == 1:
        time.sleep(0.2) # Güç Tüketimi YÜKSEK (Simüle)
        return "HIGH_POWER"
    else:
        time.sleep(0.1) # Güç Tüketimi DÜŞÜK
        return "LOW_POWER"

print("[*] Cihazın güç tüketimi ölçülüyor...")
measured_trace = []

for bit in secret_key:
    start = time.time()
    power_level = modular_exponentiation_sim(bit)
    end = time.time()
    duration = end - start
    measured_trace.append(duration)
    print(f"İşlem Süresi: {duration:.3f}s -> Profil: {power_level}")

print("\n[ANALİZ] Güç grafiğinden anahtar yeniden oluşturuluyor...")
recovered_key = []
for t in measured_trace:
    if t > 0.15: recovered_key.append(1)
    else: recovered_key.append(0)

print(f"✅ Çalınan Anahtar: {recovered_key}")
print("Şifreleme algoritmasını kırmadan, donanımın fiziğinden şifre çalındı.")