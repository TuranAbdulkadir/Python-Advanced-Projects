import geocoder

ip = geocoder.ip("me")
print(f"IP: {ip.ip}")
print(f"City: {ip.city}")
print(f"Country: {ip.country}")
print(f"Coordinates: {ip.latlng}")
print(f"Google Maps: https://www.google.com/maps/search/?api=1&query={ip.lat},{ip.lng}")