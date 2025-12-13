import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Verileri birleştir ve SHA256 al
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # İstenen zorlukta (örn: başında 4 tane 0 olan) hash bulana kadar dene
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"⛏️ Blok Kazıldı: {self.hash}")

print("--- PYTHON BLOCKCHAIN ---")
difficulty = 4 # Başında 4 sıfır olan hash bulmalı (Zorluk)

# İlk Blok (Genesis)
genesis_block = Block(0, "0", "Genesis Block")
genesis_block.mine_block(difficulty)

chain = [genesis_block]

# Yeni Blok Ekleme
print("Yeni bloklar ekleniyor...")
for i in range(1, 4):
    new_data = f"Transfer İşlemi #{i}: Ali -> Veli {i*10} Coin"
    new_block = Block(i, chain[-1].hash, new_data)
    new_block.mine_block(difficulty)
    chain.append(new_block)
    print(f"🔗 Zincire Eklendi: {new_data}\n")