import networkx as nx

print("--- GRAPH BASED OSINT MAPPER ---")

# İlişkisel Graf Oluştur
G = nx.Graph()

# Veri Noktaları
target_email = "admin@target.com"
target_domain = "target.com"
target_ip = "192.168.1.5"
linked_domain = "old-site.com"

# Bağlantıları Kur
G.add_edge(target_email, target_domain, relation="Registered")
G.add_edge(target_domain, target_ip, relation="Hosted On")
G.add_edge(target_ip, linked_domain, relation="Shared Hosting")

print(f"[*] Düğümler (Varlıklar): {G.nodes()}")
print(f"[*] Kenarlar (İlişkiler): {G.edges()}")

# Analiz: En merkezi nokta neresi?
print("\n[ANALİZ] En kritik bağlantı noktası aranıyor...")
centrality = nx.degree_centrality(G)
most_important = max(centrality, key=centrality.get)

print(f"✅ HEDEF MERKEZİ: {most_important} (Bu nokta saldırı için en iyi yer)")