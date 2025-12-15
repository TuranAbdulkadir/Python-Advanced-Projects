import ctypes
import sys
import os

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Process Tree (İşlem Ağacı) yapısını bozar.")

print("--- WEAPONIZED PPID SPOOFING ---")

def spoof_parent():
    # 1. HEDEF BABA (Weaponized Part)
    # Simülasyon: print("Baba değiştirildi")
    # Gerçek: explorer.exe'nin PID'sini bul ve "Baba" olarak ayarla.
    
    # (PID bulma kodu atlandı, varsayalım 1234 explorer.exe)
    parent_pid = 1234 
    
    print(f"[*] Sahte Baba PID: {parent_pid} (explorer.exe)")
    
    # 2. STARTUP INFO YAPILANDIRMASI
    # PROC_THREAD_ATTRIBUTE_PARENT_PROCESS (0x00020000)
    # Bu özellik, "Benim babam beni çağıran değil, şu PID'dir" dememizi sağlar.
    
    lpAttributeList = ctypes.create_string_buffer(100)
    # UpdateProcThreadAttribute(..., parent_pid, ...)
    
    print("[*] Virüs (Payload) başlatılıyor...")
    
    # EXTENDED_STARTUPINFO_PRESENT bayrağı ile süreç yarat
    # CreateProcessA(..., "virus.exe", ..., lpAttributeList, ...)
    
    print("💀 İŞLEM TAMAM.")
    print("EDR sistemleri virüsün Word'den değil, Masaüstünden (Explorer) açıldığını sanacak.")

if __name__ == "__main__":
    spoof_parent()