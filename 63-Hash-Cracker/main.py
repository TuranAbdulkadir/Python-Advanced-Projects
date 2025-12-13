import hashlib
import sys
from colorama import Fore, init
init(autoreset=True)

print("--- HASH CRACKER ---")
target_hash = input("Kırılacak Hash: ")
hash_type = input("Türü (md5/sha256): ").lower()
wordlist = "wordlist.txt"

print("Sözlük saldırısı başlatılıyor...")

try:
    with open(wordlist, "r", encoding='latin-1') as file:
        for line in file:
            password = line.strip()
            
            if hash_type == "md5":
                hashed = hashlib.md5(password.encode()).hexdigest()
            elif hash_type == "sha256":
                hashed = hashlib.sha256(password.encode()).hexdigest()
            else:
                print("Desteklenmeyen tür.")
                sys.exit()
                
            if hashed == target_hash:
                print(f"\n{Fore.GREEN}🎉 ŞİFRE BULUNDU: {password}")
                sys.exit()
                
    print(f"\n{Fore.RED}❌ Şifre wordlist içinde yok.")
    
except FileNotFoundError:
    print("wordlist.txt dosyası yok.")