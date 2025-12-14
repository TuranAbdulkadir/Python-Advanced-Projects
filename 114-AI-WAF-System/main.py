from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

print("--- AI WEB APPLICATION FIREWALL (Training) ---")

# 1. Eğitim Verisi (Normal ve Saldırı URL'leri)
# 0: Temiz, 1: SQL Injection / XSS
data = [
    ("/home", 0), ("/contact", 0), ("/products?id=5", 0),
    ("/search?q=hello", 0), ("/login", 0),
    ("/products?id=1 OR 1=1", 1), ("/<script>alert(1)</script>", 1),
    ("/admin' --", 1), ("/union select 1,2,3", 1),
    ("/img src=x onerror=alert(1)", 1)
]

# Veriyi ayır
urls = [d[0] for d in data]
labels = [d[1] for d in data]

# 2. Modeli Eğit
vectorizer = CountVectorizer(analyzer='char', ngram_range=(2, 4))
X = vectorizer.fit_transform(urls)
model = MultinomialNB()
model.fit(X, labels)

print("✅ AI Modeli Eğitildi! Canlı Test Başlıyor...\n")

# 3. Canlı Test Fonksiyonu
def check_request(url):
    vec = vectorizer.transform([url])
    prob = model.predict_proba(vec)[0][1] # Saldırı olma ihtimali
    
    print(f"İstek: {url}")
    if prob > 0.5:
        print(f"🚫 BLOKLANDI! (Saldırı İhtimali: %{prob*100:.2f})")
    else:
        print(f"✅ İZİN VERİLDİ. (Temiz)")
    print("-" * 30)

# Testler
check_request("/about-us")
check_request("/products?id=10 UNION SELECT password FROM users")
check_request("/user/profile")