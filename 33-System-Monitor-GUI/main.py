import customtkinter as ctk
import psutil

def update_stats():
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    battery = psutil.sensors_battery().percent if psutil.sensors_battery() else "N/A"
    
    lbl_cpu.configure(text=f"CPU Usage: {cpu}%")
    lbl_ram.configure(text=f"RAM Usage: {ram}%")
    lbl_bat.configure(text=f"Battery: {battery}%")
    
    root.after(1000, update_stats)

ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.geometry("300x200")
root.title("System Monitor")

lbl_cpu = ctk.CTkLabel(root, text="CPU: ...", font=("Arial", 18))
lbl_cpu.pack(pady=10)

lbl_ram = ctk.CTkLabel(root, text="RAM: ...", font=("Arial", 18))
lbl_ram.pack(pady=10)

lbl_bat = ctk.CTkLabel(root, text="Battery: ...", font=("Arial", 18))
lbl_bat.pack(pady=10)

update_stats()
root.mainloop()