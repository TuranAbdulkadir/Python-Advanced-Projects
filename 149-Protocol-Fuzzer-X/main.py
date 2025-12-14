import random

print("--- SMART PROTOCOL FUZZER ---")

# FTP Protokol Durumları
states = ["USER", "PASS", "CWD", "LIST", "RETR"]

def fuzz_packet(command):
    # 1. Buffer Overflow Testi
    payload1 = command + " " + "A" * 5000
    # 2. Format String Testi
    payload2 = command + " " + "%x%n%x%n" * 10
    # 3. Integer Overflow
    payload3 = command + " " + "-1"
    
    return [payload1, payload2, payload3]

target = "USER"
print(f"[*] Hedef Komut: {target}")
mutations = fuzz_packet(target)

for i, m in enumerate(mutations):
    print(f"Test {i+1}: {m[:50]}... (Uzunluk: {len(m)})")
    # if send_to_server(m) == CRASH: print("BUG FOUND")

print("\n✅ Fuzzing paketleri oluşturuldu. Ağ üzerinden gönderilmeye hazır.")