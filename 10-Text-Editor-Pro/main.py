import tkinter as tk
from tkinter import filedialog

def open_file():
    path = filedialog.askopenfilename()
    if path:
        with open(path, 'r') as f:
            text.delete(1.0, tk.END)
            text.insert(tk.END, f.read())

def save_file():
    path = filedialog.asksaveasfilename()
    if path:
        with open(path, 'w') as f:
            f.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("Pro Text Editor")
root.geometry("600x400")

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)

text = tk.Text(root, font=("Consolas", 12))
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()