import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from colorama import Fore, init

init(autoreset=True)
print(f"{Fore.CYAN}--- AI NETWORK INTRUSION DETECTION SYSTEM (NIDS) ---")

# 1. Yapay Zeka Modelini Eğit (Demo Verisi)
# Özellikler: [Paket Boyutu, Kaynak Port, Hedef Port, Protokol (0:TCP, 1:UDP)]
# Etiketler: 0: Temiz, 1: Saldırı (DDoS/Scan)
print("Yapay Zeka eğitiliyor...")
X_train = np.array([
    [50, 80, 443, 0], [60, 443, 80, 0], [1500, 22, 5555, 1], # Normal
    [10, 0, 80, 0], [20, 0, 443, 0], [9999, 4444, 80, 1]     # Saldırı
])
y_train = np.array([0, 0, 0, 1, 1, 1])

model = RandomForestClassifier()
model.fit(X_train, y_train)
print("✅ Model Hazır!\n")

# 2. Canlı Trafik Simülasyonu
def analyze_packet(size, src_port, dst_port, proto):
    prediction = model.predict([[size, src_port, dst_port, proto]])
    prob = model.predict_proba([[size, src_port, dst_port, proto]])[0][1]
    
    if prediction[0] == 1:
        print(f"{Fore.RED}🚨 SALDIRI TESPİT EDİLDİ! (Güven: %{prob*100:.2f})")
        print(f"   Detay: Size={size}, Ports={src_port}->{dst_port}")
    else:
        print(f"{Fore.GREEN}✅ Normal Trafik. (Güven: %{(1-prob)*100:.2f})")

# Test Verileri
analyze_packet(55, 1234, 80, 0)   # Normal gibi
analyze_packet(12000, 666, 80, 1) # Anormal (DDoS)
analyze_packet(15, 0, 22, 0)      # Anormal (Port Scan)