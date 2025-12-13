import time
import random
import matplotlib.pyplot as plt

print("--- WIFI SIGNAL HEATMAP ---")
print("Lütfen odada yürüyün (Veri toplanıyor)...")

locations = [] # (x, y)
signals = []   # dBm (Sinyal gücü)

# Simülasyon: Odayı geziyormuşsun gibi
for x in range(10):
    for y in range(10):
        # Gerçekte 'netsh' veya 'iwconfig' ile sinyal alınır
        signal_strength = -random.randint(30, 90) # -30 mükemmel, -90 kötü
        locations.append((x, y))
        signals.append(signal_strength)
        print(f"Konum ({x},{y}) -> Sinyal: {signal_strength} dBm")
        time.sleep(0.05)

print("Harita oluşturuluyor...")
x_val = [i[0] for i in locations]
y_val = [i[1] for i in locations]

plt.figure(figsize=(8, 6))
plt.scatter(x_val, y_val, c=signals, cmap='RdYlGn', s=500, marker='s')
plt.colorbar(label='Sinyal Gücü (dBm)')
plt.title("Wifi Kapsama Haritası")
plt.show()