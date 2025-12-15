import sys
import wave
import struct

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod çalıştırılabilir dosyaları ses dosyasına dönüştürür.")

print("--- WEAPONIZED AUDIO EXFILTRATION ---")

def encode_file_to_audio():
    target_file = "virus.exe"
    
    # 1. BINARY OKUMA (Weaponized Part)
    # Simülasyon: text = "HACKED" (Resim yap)
    # Gerçek: Dosyanın binary (0101) verisini oku.
    
    with open(target_file, "rb") as f:
        data = f.read()
        
    print(f"[*] {len(data)} bytes ses verisine dönüştürülüyor...")
    
    # 2. FREKANS MODÜLASYONU (FSK)
    # 0 biti için 1000 Hz, 1 biti için 2000 Hz tonu oluştur.
    # Bu yöntem, modemlerin telefon hattından internete bağlanma mantığıdır.
    
    audio_data = []
    for byte in data:
        for i in range(8):
            bit = (byte >> i) & 1
            freq = 2000 if bit == 1 else 1000
            # (Burada sinüs dalgası oluşturma matematiksel kodu olur)
            # audio_data.append(generate_sine_wave(freq))
            
    print("💀 'music.wav' OLUŞTURULDU.")
    print("Bu dosya mail atılabilir. Karşı taraftaki 'Receiver' scripti sesi dinleyip tekrar EXE'ye çevirir.")

if __name__ == "__main__":
    encode_file_to_audio()