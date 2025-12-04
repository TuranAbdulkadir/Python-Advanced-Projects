from cryptography.fernet import Fernet
import os

# Anahtar oluşturma
if not os.path.exists("secret.key"):
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated!")
else:
    key = open("secret.key", "rb").read()

cipher = Fernet(key)

msg = input("Enter a message to encrypt: ")
encrypted_msg = cipher.encrypt(msg.encode())

print(f"\n🔒 Encrypted: {encrypted_msg}")
print(f"🔓 Decrypted: {cipher.decrypt(encrypted_msg).decode()}")