import ctypes
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Direct Syscall tekniğini uygular.")

print("--- WEAPONIZED SYSCALLS ---")

def direct_syscall():
    # 1. SYSCALL ID (Weaponized Part)
    # Simülasyon: kernel32.OpenProcess(...) -> EDR bunu görür.
    # Gerçek: Doğrudan Kernel'e git.
    
    # NtOpenProcess Syscall ID (Windows 10 sürümüne göre değişir, örn: 0x26)
    syscall_id = 0x26 
    
    print(f"[*] NtOpenProcess Syscall ID: {hex(syscall_id)}")
    print("[*] EDR Kancaları (Hooks) atlanıyor...")
    
    # 2. ASSEMBLY STUB
    # mov r10, rcx
    # mov eax, 0x26 (Syscall ID)
    # syscall
    # ret
    
    # (Python'da bu kısmı çalıştırmak için shellcode buffer oluşturulur)
    # Bu teknik "Hell's Gate" olarak bilinir.
    
    print("💀 KERNEL İLE DOĞRUDAN İLETİŞİM KURULDU.")
    print("ntdll.dll kullanılmadığı için EDR/Antivirüs işlemi göremedi.")

if __name__ == "__main__":
    direct_syscall()