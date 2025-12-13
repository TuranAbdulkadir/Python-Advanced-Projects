import scapy.all as scapy
import networkx as nx
import matplotlib.pyplot as plt

print("--- AĞ HARİTALANDIRICI ---")
target_ip = "192.168.1.1/24" # Kendi ağ aralığın

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    devices = []
    for element in answered_list:
        devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc})
    return devices

devices = scan(target_ip)
print(f"{len(devices)} cihaz bulundu. Harita çiziliyor...")

# Grafiği Çiz
G = nx.Graph()
G.add_node("Senin PC (Hacker)", color='red')

for device in devices:
    node_name = f"{device['ip']}\n{device['mac']}"
    G.add_node(node_name, color='blue')
    G.add_edge("Senin PC (Hacker)", node_name)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000)
plt.title("Ağ Topolojisi")
plt.show()