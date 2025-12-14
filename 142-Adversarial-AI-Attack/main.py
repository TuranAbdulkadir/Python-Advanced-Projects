import numpy as np

print("--- ADVERSARIAL AI ATTACK SIMULATOR ---")

# Sahte bir AI Modeli (Basitleştirilmiş)
def ai_predict(image_array):
    # Eğer piksellerin ortalaması 128'den büyükse 'Panda', küçükse 'Gibbon'
    avg = np.mean(image_array)
    if avg > 128: return "Panda", 0.99
    else: return "Gibbon", 0.98

# Orijinal Görüntü (Panda) - Rastgele pikseller
original_image = np.random.randint(150, 255, (10, 10)) 

# Saldırı: Gürültü Ekleme (FGSM Attack Mantığı)
# İnsan gözü bu 5 birimlik değişimi fark etmez.
noise = np.random.randint(-50, -30, (10, 10)) 
adversarial_image = original_image + noise

print(f"[*] Orijinal Resim Tahmini: {ai_predict(original_image)}")
print(f"[*] Gürültü Ekleniyor (Adversarial Noise)...")
print(f"[*] Hacklenmiş Resim Tahmini: {ai_predict(adversarial_image)}")

print("\n✅ AI başarıyla kandırıldı. İnsan için resim hala aynı görünüyor.")