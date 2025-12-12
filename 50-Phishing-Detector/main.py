print("--- PHISHING LINK ANALYZER ---")
url = input("Şüpheli Linki Yapıştır: ").lower()

score = 0
reasons = []

# 1. Uzunluk kontrolü
if len(url) > 70:
    score += 20
    reasons.append("Link çok uzun (Şüpheli)")

# 2. IP Adresi kullanımı
if "http://" in url and any(char.isdigit() for char in url):
    score += 30
    reasons.append("IP adresi kullanılıyor (Güvensiz)")

# 3. @ işareti (Yönlendirme hilesi)
if "@" in url:
    score += 40
    reasons.append("@ işareti ile yönlendirme var")

# 4. Tire (-) kullanımı (Sahte domain hilesi)
if url.count("-") > 3:
    score += 20
    reasons.append("Çok fazla tire (-) işareti var")

print("-" * 30)
print(f"GÜVENSİZLİK SKORU: {score}/100")
if score > 50:
    print("🚨 TEHLİKE! Bu link yüksek ihtimalle PHISHING (Oltalama).")
else:
    print("✅ Link güvenli görünüyor.")

for r in reasons: print(f"- {r}")