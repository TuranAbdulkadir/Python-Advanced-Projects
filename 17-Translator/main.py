from deep_translator import GoogleTranslator

text = input("Enter text to translate: ")
lang = input("Target language code (e.g. 'tr', 'fr', 'es'): ")

try:
    translated = GoogleTranslator(source='auto', target=lang).translate(text)
    print(f"\nOriginal: {text}")
    print(f"Translated: {translated}")
except Exception as e:
    print("Error:", e)