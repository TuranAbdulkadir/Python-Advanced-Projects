import instaloader

ig = instaloader.Instaloader()
user = input("Enter Instagram Username: ")

print(f"Downloading profile picture for {user}...")

try:
    ig.download_profile(user, profile_pic_only=True)
    print("✅ Download Successful! Check the folder.")
except Exception as e:
    print("Error:", e)