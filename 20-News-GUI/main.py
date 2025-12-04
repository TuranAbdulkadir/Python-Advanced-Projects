import tkinter as tk

def show_news():
    # Demo haberler (API key olmadan çalışması için)
    news = [
        "1. Python releases new version 3.14",
        "2. AI takes over coding jobs?",
        "3. Stock market hits all time high",
        "4. New tech discoveries in 2025"
    ]
    lbl.config(text="\n".join(news))

root = tk.Tk()
root.geometry("400x300")
root.title("News App")

btn = tk.Button(root, text="Load News", command=show_news, font=("Arial", 14), bg="blue", fg="white")
btn.pack(pady=20)

lbl = tk.Label(root, text="Press button to get news...", font=("Arial", 12), justify="left")
lbl.pack()

root.mainloop()