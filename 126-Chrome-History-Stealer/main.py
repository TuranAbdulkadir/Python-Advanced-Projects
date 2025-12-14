import sqlite3
import os
import shutil

print("--- CHROME HISTORY EXTRACTOR ---")

# Chrome Geçmiş Dosyası Yolu (Windows)
user = os.environ.get('USERNAME')
history_path = f"C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
temp_path = "History_Copy"

try:
    # Dosya kullanımda olabilir, kopyasını al
    shutil.copyfile(history_path, temp_path)
    
    # SQL ile bağlan
    con = sqlite3.connect(temp_path)
    cursor = con.cursor()
    
    # URL'leri çek
    cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY visit_count DESC LIMIT 20")
    results = cursor.fetchall()
    
    print(f"\n🔍 {user} Kullanıcısının En Çok Girdiği Siteler:\n")
    for url, title, count, _ in results:
        print(f"[{count}] {title[:30]} -> {url[:50]}")
        
    con.close()
    os.remove(temp_path)
    
except Exception as e:
    print(f"Hata: Chrome açık olabilir veya yol yanlış. {e}")