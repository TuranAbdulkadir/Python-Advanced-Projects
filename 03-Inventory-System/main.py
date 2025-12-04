import tkinter as tk
from tkinter import messagebox
import sqlite3
import pandas as pd

conn = sqlite3.connect('store.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER)''')

def add():
    try:
        c.execute("INSERT INTO products (name, stock) VALUES (?, ?)", (entry_name.get(), int(entry_stock.get())))
        conn.commit()
        list_products()
    except: messagebox.showerror("Error", "Invalid Input")

def list_products():
    listbox.delete(0, tk.END)
    for row in c.execute("SELECT * FROM products"):
        listbox.insert(tk.END, f"{row[1]} - Stock: {row[2]}")

def export():
    df = pd.read_sql_query("SELECT * FROM products", conn)
    df.to_excel("inventory.xlsx", index=False)
    messagebox.showinfo("Success", "Exported to Excel")

root = tk.Tk()
root.title("Inventory")
root.geometry("300x400")

tk.Label(root, text="Product:").pack()
entry_name = tk.Entry(root); entry_name.pack()
tk.Label(root, text="Stock:").pack()
entry_stock = tk.Entry(root); entry_stock.pack()
tk.Button(root, text="Add", command=add).pack(pady=5)
tk.Button(root, text="Export Excel", command=export).pack(pady=5)
listbox = tk.Listbox(root); listbox.pack()

list_products()
root.mainloop()