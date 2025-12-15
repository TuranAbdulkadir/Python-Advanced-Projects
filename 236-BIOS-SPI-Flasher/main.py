import os
import sys

print("--- SPI FLASH CORRUPTOR (BIOS BRICKER) ---")
print("UYARI: Bu kod anakartı kullanılmaz hale getirir (Brick).")

def corrupted_flash_logic():
    # Windows'ta BIOS'a erişim Kernel Driver gerektirir (RWEverything / Chipsec).
    # Bu kod, SPI Flash Controller'a gönderilen komut mantığını gösterir.
    
    print("[*] SPI Denetleyicisi (PCH) hedefleniyor...")
    print("[*] BIOS Write Enable (WREN) biti aktif ediliyor...")
    
    # SPI Base Address (Memory Mapped I/O)
    spi_base = 0xFED01000 
    
    # 1. BIOS Bölgesini Sil (Erase Opcode)
    print(f"[!] KOMUT: SPI_ERASE gönderiliyor -> Adres: 0xFFF00000 (BIOS Region)")
    
    # 2. Rastgele Veri Yaz (Corrupt)
    junk_data = b"\x00\xFF\xDE\xAD" * 1024
    print(f"[!] KOMUT: SPI_PROGRAM gönderiliyor... ({len(junk_data)} bytes)")
    
    print("\n💀 İŞLEM TAMAMLANDI.")
    print("Bilgisayarı yeniden başlatırsan SİYAH EKRAN göreceksin.")
    print("Anakartın BIOS çipi silindi. Geri dönüş yok.")

if __name__ == "__main__":
    confirm = input("Bu işlem donanımı bozar. Devam? (YES/NO): ")
    if confirm == "YES":
        corrupted_flash_logic()