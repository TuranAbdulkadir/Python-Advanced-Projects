import time
import threading

print("--- TIMING BASED COVERT CHANNEL ---")

secret_msg = "101" # Binary mesaj (5)

def sender():
    print("[Sender] Başladı...")
    for bit in secret_msg:
        if bit == "1":
            time.sleep(2.0) # 1 saniye gönderim, 2.0 saniye bekleme = '1'
        else:
            time.sleep(0.5) # 0.5 saniye bekleme = '0'
        print(f"[Sender] Paket yollandı (Gecikme süresi ile)")

def receiver():
    print("[Receiver] Dinliyor...")
    # Simüle edilmiş zaman ölçümü
    # Gerçek ağda paketler arası süre ölçülür.
    for bit in secret_msg:
        start = time.time()
        # Burada paketin gelmesini bekliyoruz (Simülasyon)
        if bit == "1": time.sleep(2.0)
        else: time.sleep(0.5)
        end = time.time()
        
        diff = end - start
        decoded = "1" if diff > 1.5 else "0"
        print(f"[Receiver] Algılanan Gecikme: {diff:.2f}s -> Bit: {decoded}")

t1 = threading.Thread(target=sender)
t2 = threading.Thread(target=receiver)
t1.start(); t2.start()
t1.join(); t2.join()