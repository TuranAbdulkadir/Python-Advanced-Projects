from PyPDF2 import PdfReader, PdfWriter

file_name = "file.pdf" # Şifrelenecek dosya
password = input("Set a password: ")

writer = PdfWriter()
reader = PdfReader(file_name)

for page in reader.pages:
    writer.add_page(page)

writer.encrypt(password)

with open("protected.pdf", "wb") as f:
    writer.write(f)

print(f"✅ Locked! Saved as 'protected.pdf' with password: {password}")