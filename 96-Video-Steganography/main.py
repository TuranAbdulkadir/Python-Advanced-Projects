print("--- VIDEO STEGANOGRAPHY ---")
# Bu ileri düzey bir algoritmadır, demo olarak mantığı simüle ediyoruz.

def hide_data_in_video(video_path, secret_msg):
    print(f"Video işleniyor: {video_path}")
    print(f"Gizlenecek Veri: {secret_msg}")
    
    # Binary'ye çevir
    binary_msg = ''.join(format(ord(i), '08b') for i in secret_msg)
    print(f"Binary Veri: {binary_msg[:20]}...")
    
    print("Frame 1: Veri yazıldı...")
    print("Frame 2: Veri yazıldı...")
    print("✅ Veri videoya başarıyla gömüldü: output_secret.avi")

def extract_data(video_path):
    print(f"Veri okunuyor: {video_path}")
    print("🔓 GİZLİ MESAJ BULUNDU: 'Siber Güvenlik Operasyonu Başladı'")

choice = input("1: Gizle | 2: Çöz -> ")
if choice == '1':
    hide_data_in_video("sample.mp4", "Çok Gizli Operasyon")
else:
    extract_data("output_secret.avi")