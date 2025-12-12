from textblob import TextBlob
from colorama import Fore, init

init(autoreset=True)

print("--- AI DUYGU ANALİZİ (Çıkış: q) ---")

while True:
    text = input("Bir cümle yaz (İngilizce): ")
    if text == 'q': break
    
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity # -1 (Negatif) ile +1 (Pozitif) arası
    
    if sentiment > 0.5:
        print(f"{Fore.GREEN}😊 ÇOK POZİTİF (Skor: {sentiment})")
    elif sentiment > 0:
        print(f"{Fore.CYAN}🙂 POZİTİF (Skor: {sentiment})")
    elif sentiment == 0:
        print(f"{Fore.YELLOW}😐 NÖTR (Skor: {sentiment})")
    elif sentiment > -0.5:
        print(f"{Fore.MAGENTA}☹️ NEGATİF (Skor: {sentiment})")
    else:
        print(f"{Fore.RED}😡 ÇOK NEGATİF (Skor: {sentiment})")