import easyocr

# Klasöre 'text_image.jpg' koy
reader = easyocr.Reader(['en', 'tr'])
print("Reading image...")

try:
    result = reader.readtext('text_image.jpg', detail=0)
    print("\n--- EXTRACTED TEXT ---")
    print(" ".join(result))
except:
    print("Error: 'text_image.jpg' not found.")