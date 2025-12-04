from stegano import lsb
# Klasöre 'secret.jpg' koymayı unutma!

choice = input("1-Hide, 2-Reveal: ")

if choice == '1':
    msg = input("Message: ")
    try:
        lsb.hide("secret.jpg", msg).save("hidden.png")
        print("Saved as hidden.png")
    except: print("secret.jpg not found.")
    
elif choice == '2':
    try:
        print("Message:", lsb.reveal("hidden.png"))
    except: print("No message found.")