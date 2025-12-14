import subprocess
import os

print("--- REAL MAC CHANGER (Linux/macOS) ---")
# Windows'ta registry ayarı gerektirir, bu kod Linux/Kali mantığındadır.
interface = input("Ağ Arayüzü (örn: eth0 veya wlan0): ")
new_mac = input("Yeni MAC Adresi (örn: 00:11:22:33:44:55): ")

print(f"{interface} arayüzü indiriliyor...")
subprocess.call(["ifconfig", interface, "down"])

print(f"MAC adresi değiştiriliyor: {new_mac}")
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

print(f"{interface} arayüzü açılıyor...")
subprocess.call(["ifconfig", interface, "up"])

print("✅ MAC Adresi değiştirildi! (ifconfig ile kontrol et)")