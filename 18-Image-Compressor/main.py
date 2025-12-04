from PIL import Image
import os

try:
    print("Compressing 'input.jpg'...")
    img = Image.open("input.jpg")
    img.save("compressed.jpg", optimize=True, quality=50)
    print("✅ Done! Saved as 'compressed.jpg'")
except FileNotFoundError:
    print("❌ Error: 'input.jpg' not found.")