import shodan

print("--- SHODAN IOT SCANNER ---")
api_key = input("Shodan API Key: ")
api = shodan.Shodan(api_key)
target = input("Aranacak (örn: webcam, apache): ")

try:
    results = api.search(target)
    print(f"\nToplam Sonuç: {results['total']}\n")
    for result in results['matches'][:5]:
        print(f"IP: {result['ip_str']}")
        print(f"Veri: {result['data'][:50]}...")
        print("-" * 30)
except shodan.APIError as e:
    print(f"Hata: {e}")