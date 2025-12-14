import asyncio
from bleak import BleakScanner

print("--- BLUETOOTH CİHAZ TARAYICI (MODERN) ---")
print("Etraftaki cihazlar taranıyor... (Lütfen 5-10 saniye bekle)")

async def scan_devices():
    # Windows uyumlu tarama
    devices = await BleakScanner.discover()
    
    if not devices:
        print("[-] Hiçbir cihaz bulunamadı. Bluetooth'un açık olduğundan emin ol.")
        return

    print(f"\n[+] {len(devices)} Cihaz Bulundu:\n")
    print(f"{'MAC ADRESİ':<25} | {'CİHAZ ADI'}")
    print("-" * 50)
    
    found_any = False
    for d in devices:
        # İsmi boş olanları 'Bilinmeyen' olarak göster
        name = d.name if d.name else "Bilinmeyen Cihaz"
        address = d.address
        print(f"{address:<25} | {name}")
        found_any = True

    if found_any:
        print("\n[*] Saldırı yapmak istediğin cihazın MAC adresini kopyala.")
        print("[*] (Örn: 54:A1:D5:XX:XX:XX)")

# Asenkron çalıştırma (Windows için şart)
try:
    asyncio.run(scan_devices())
except Exception as e:
    print(f"Hata oluştu: {e}")