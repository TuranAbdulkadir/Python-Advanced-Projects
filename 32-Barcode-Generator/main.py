import barcode
from barcode.writer import ImageWriter

number = input("Enter 12-digit number for Barcode: ")
# EAN-13 formatı kullanılır
ean = barcode.get('ean13', number, writer=ImageWriter())

filename = ean.save('my_barcode')
print(f"✅ Barcode generated: {filename}")