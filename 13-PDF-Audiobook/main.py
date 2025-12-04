import PyPDF2
import pyttsx3

print("Starting PDF Reader...")

try:
    # 'book.pdf' dosyasını arar
    reader = PyPDF2.PdfReader(open('book.pdf', 'rb'))
    speaker = pyttsx3.init()

    # İlk sayfayı oku
    page = reader.pages[0]
    text = page.extract_text()
    
    print("Reading:\n", text)
    speaker.say(text)
    speaker.runAndWait()
except FileNotFoundError:
    print("❌ Error: Please put a PDF file named 'book.pdf' in this folder.")