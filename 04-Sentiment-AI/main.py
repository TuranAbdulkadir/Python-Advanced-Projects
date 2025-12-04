from textblob import TextBlob

print("--- AI SENTIMENT ANALYSIS ---")
while True:
    text = input("\nEnter text (q to quit): ")
    if text == 'q': break
    
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    
    if score > 0: print("Result: 😊 POSITIVE")
    elif score < 0: print("Result: 😠 NEGATIVE")
    else: print("Result: 😐 NEUTRAL")