# 🦗 Project 222: WMI Persistence
**Tech:** WMI (Windows Management Instrumentation)
**Realism:** Concept

Demonstrates **Fileless Persistence**. Instead of placing a file in the Startup folder, this creates a WMI Subscription. Windows itself monitors for the event (e.g., system uptime, user logon) and executes the payload. Extremely stealthy.