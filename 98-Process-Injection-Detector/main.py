import psutil

print("--- MEMORY PROCESS INJECTION DETECTOR ---")

# Şüpheli ebeveyn-çocuk ilişkileri (Örn: Word, Powershell açarsa şüphelidir)
suspicious_parents = {
    "winword.exe": ["cmd.exe", "powershell.exe"],
    "excel.exe": ["cmd.exe", "powershell.exe"],
    "chrome.exe": ["cmd.exe"]
}

for proc in psutil.process_iter(['pid', 'name', 'ppid']):
    try:
        name = proc.info['name'].lower()
        ppid = proc.info['ppid']
        pid = proc.info['pid']
        
        if psutil.pid_exists(ppid):
            parent = psutil.Process(ppid)
            parent_name = parent.name().lower()
            
            if parent_name in suspicious_parents:
                if name in suspicious_parents[parent_name]:
                    print(f"🚨 KRİTİK UYARI! Injection Şüphesi!")
                    print(f"   Ana Süreç: {parent_name} -> Çalıştırdığı: {name} (PID: {pid})")
                    print("   Açıklama: Bir ofis belgesi veya tarayıcı komut satırı açmaya çalıştı!")

    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

print("Tarama Bitti.")