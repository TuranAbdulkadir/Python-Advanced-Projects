from langdetect import detect

text = input("Enter text in any language: ")

try:
    lang = detect(text)
    print(f"🔴 Detected Language Code: {lang.upper()}")
except:
    print("Error: Could not detect language.")