import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

print("--- SESLİ GÜVENLİK SİSTEMİ ---")
fs = 44100
seconds = 3

def record_voice(filename):
    print("🎙️ Konuşun...")
    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("Kaydedildi.")
    return recording

print("1. Sesini Kaydet (Referans)")
print("2. Giriş Yap (Test)")
choice = input("Seçim: ")

if choice == '1':
    record_voice("my_voice.wav")
    print("✅ Ses imzanız oluşturuldu.")

elif choice == '2':
    # Basit bir frekans karşılaştırması (Demo)
    # Gerçek sistemlerde MFCC kullanılır.
    print("Lütfen şifreyi söyleyin...")
    new_rec = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    
    # Referans sesi yükle
    import scipy.io.wavfile as wav
    _, ref_data = wav.read("my_voice.wav")
    
    # Farkı hesapla (Basit ortalama fark)
    diff = np.abs(np.mean(ref_data) - np.mean(new_rec))
    
    print(f"Ses Farkı Skoru: {diff:.4f}")
    if diff < 0.001: # Eşik değer
        print("🔓 ERİŞİM ONAYLANDI: Hoşgeldiniz!")
    else:
        print("🔒 ERİŞİM REDDEDİLDİ: Ses eşleşmedi.")