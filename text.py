from textblob import TextBlob

while True:
    user_input = input("Enter your text: ")
    if user_input == "Exit":
        break
    analysis = TextBlob(user_input)
    print(analysis.sentiment.polarity)
    if analysis.sentiment.polarity > 0:
        print("Positive sentiment")
    elif analysis.sentiment.polarity < 0:
        print("Negative sentiment")
    else:
        print("Neutral sentiment")
        