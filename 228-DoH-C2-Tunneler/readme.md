# 🚇 Project 228: DoH C2 Tunneler
**Type:** Exfiltration / C2
**Tech:** DNS over HTTPS (Google API)

Uses Google's legitimate **DNS-over-HTTPS** API to create a covert command and control channel. Since the connection is SSL encrypted to `dns.google`, network security appliances cannot inspect the traffic, and blocking it would break legitimate internet usage.