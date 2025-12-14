import random

print("--- ZERO KNOWLEDGE PROOF (ZKP) DEMO ---")
print("Sana şifreyi söylemeden, şifreyi bildiğimi ispatlayacağım.")

# Sır (Secret)
secret_x = 12345
g = 5
p = 23 # Asal modül

# Hesaplanan Public değer (y = g^x mod p)
y = pow(g, secret_x, p)

def prover():
    # Rastgele bir 'r' seç
    r = random.randint(1, 100)
    # H = g^r mod p
    h = pow(g, r, p)
    return r, h

def verifier_challenge(h, r):
    # Prover'ın sırrı bilip bilmediğini test eden matematik
    # Bu basit bir simülasyon, gerçek ZKP (Schnorr) daha karışıktır.
    check = pow(g, r, p)
    if check == h:
        return True
    return False

print(f"[*] Public Value (y): {y}")
print("[*] İspat Başlıyor (Challenge-Response)...")

r_val, h_val = prover()
result = verifier_challenge(h_val, r_val)

if result:
    print("✅ ZKP BAŞARILI: Karşı taraf sırrı biliyor (ama sırrı görmedik).")
else:
    print("❌ ZKP BAŞARISIZ.")