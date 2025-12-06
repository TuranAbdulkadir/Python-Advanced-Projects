import requests

url = input("Enter Website URL (https://...): ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("✅ Website is ONLINE")
    else:
        print(f"⚠️ Website returned status: {response.status_code}")
except:
    print("❌ Website is OFFLINE or Invalid URL")