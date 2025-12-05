import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Kalite
seconds = int(input("How many seconds to record? "))

print("🔴 Recording...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Kayıt bitene kadar bekle
print("✅ Finished!")

write('output.wav', fs, myrecording)
print("Saved as output.wav")