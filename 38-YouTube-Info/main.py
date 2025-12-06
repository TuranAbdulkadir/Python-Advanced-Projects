from pytubefix import YouTube

link = input("YouTube Link: ")
yt = YouTube(link)

print("-" * 30)
print(f"Title: {yt.title}")
print(f"Author: {yt.author}")
print(f"Views: {yt.views}")
print(f"Length: {yt.length} seconds")
print("-" * 30)