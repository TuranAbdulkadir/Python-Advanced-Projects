import html

# Ekran görüntüsündeki karmaşık çıktı
encoded_title = "&#72;&#51;&#54;&#48;&#48;&#80;&#32;&#86;&#57;&#46;&#48;"

# HTML kodlarını okunabilir metne çevir
decoded_title = html.unescape(encoded_title)

print(f"[*] KODLANMIŞ BAŞLIK: {encoded_title}")
print("-" * 40)
print(f"[+] ÇÖZÜLMÜŞ CİHAZ KİMLİĞİ: {decoded_title}")
print("-" * 40)

if "ZTE" in decoded_title or "H3600" in decoded_title:
    print("[!] TESPİT: Bu cihaz muhtemelen bir Fiber Modem (ZTE H3600 Serisi).")