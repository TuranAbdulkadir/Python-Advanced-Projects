import subprocess

print("Extracting Wi-Fi Profiles...\n")

try:
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    print("-" * 50)

    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print("{:<30}| {:<}".format(i, results[0]))
            except IndexError:
                print("{:<30}| {:<}".format(i, ""))
        except:
            pass
            
    input("\nPress Enter to exit...")
except Exception as e:
    print("Error (Admin rights might be needed):", e)