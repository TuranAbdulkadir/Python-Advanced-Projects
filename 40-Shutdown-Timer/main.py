import os
import tkinter as tk

def shutdown():
    min = int(entry.get())
    sec = min * 60
    os.system(f"shutdown /s /t {sec}")
    lbl.config(text=f"PC will shutdown in {min} mins!")

def cancel():
    os.system("shutdown /a")
    lbl.config(text="Shutdown Cancelled!")

root = tk.Tk()
root.geometry("300x200")
root.title("Shutdown Timer")

tk.Label(root, text="Minutes to Shutdown:").pack(pady=10)
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="SET TIMER", command=shutdown, bg="red", fg="white").pack(pady=10)
tk.Button(root, text="CANCEL", command=cancel, bg="green", fg="white").pack()

lbl = tk.Label(root, text="")
lbl.pack(pady=10)

root.mainloop()