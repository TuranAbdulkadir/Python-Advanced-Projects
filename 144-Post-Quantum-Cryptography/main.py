import numpy as np

print("--- POST-QUANTUM CRYPTOGRAPHY (Lattice Simulation) ---")

# Learning With Errors (LWE) Problemi Simülasyonu
# A * s + e = b (mod q)
# s (gizli anahtar) vektörünü bulmak, gürültü (e) yüzünden çok zordur.

dimension = 5
modulus = 97

# Gizli Anahtar (Secret Key)
s = np.random.randint(0, modulus, dimension)
# Halka Açık Anahtar (Public Key - A)
A = np.random.randint(0, modulus, (dimension, dimension))
# Hata/Gürültü (Error - e)
e = np.random.randint(-2, 3, dimension)

# Public Key (b)
b = (np.dot(A, s) + e) % modulus

print(f"[*] Secret Key (s): {s}")
print(f"[*] Public Matrix (A):\n{A}")
print(f"[*] Public Vector (b) [With Noise]: {b}")

print("\n[ANALİZ] Bir saldırganın 'A' ve 'b' yi bilerek 's' yi bulması gerekir.")
print("Geleneksel bilgisayarlar ve Kuantum bilgisayarlar için bu 'Kafes Problemi' çok zordur.")