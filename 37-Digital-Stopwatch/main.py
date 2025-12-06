import tkinter as tk

running = False
counter = 0

def count():
    if running:
        global counter
        counter += 1
        lbl.config(text=f"{counter} sec")
        root.after(1000, count)

def start():
    global running
    running = True
    count()

def stop():
    global running
    running = False

def reset():
    global running, counter
    running = False
    counter = 0
    lbl.config(text="0 sec")

root = tk.Tk()
root.geometry("300x200")
root.title("Stopwatch")

lbl = tk.Label(root, text="0 sec", font=("Arial", 40))
lbl.pack(pady=20)

tk.Button(root, text="Start", command=start).pack(side="left", padx=20)
tk.Button(root, text="Stop", command=stop).pack(side="left", padx=20)
tk.Button(root, text="Reset", command=reset).pack(side="left", padx=20)

root.mainloop()