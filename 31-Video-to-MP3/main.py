import moviepy.editor as mp

try:
    print("Loading video...")
    # Klasörde 'video.mp4' olmalı
    clip = mp.VideoFileClip("video.mp4")
    
    print("Extracting audio...")
    clip.audio.write_audiofile("extracted_audio.mp3")
    
    print("✅ Success! Saved as 'extracted_audio.mp3'")
except Exception as e:
    print("Error:", e)