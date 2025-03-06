
import random
import nltk
import spacy
from textblob import TextBlob
from nltk.chat.util import Chat, reflections

# Download tokenizer if not already installed
nltk.download("punkt")

# Load spaCy language model
nlp = spacy.load("en_core_web_sm")

# Define chatbot responses
pairs = [
    [r"(hi|hello|hey)", ["Hello!", "Hi there!", "Hey! How can I help?"]],
    [r"how are you ?", ["I'm good! How about you?", "I'm fine, thanks for asking!"]],
    [r"what is your name ?", ["I am a chatbot!", "You can call me ChatBot."]],
    [r"(bye|goodbye)", ["Goodbye!", "See you later!", "Take care!"]],
    [r"(.*)", ["I don't understand. Can you rephrase?"]],
]

chatbot = Chat(pairs, reflections)

# Sentiment analysis function
def get_sentiment(text):
    """Analyze the sentiment of user input."""
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "You seem happy!"
    elif analysis.sentiment.polarity < 0:
        return "You seem upset. I'm here to help."
    else:
        return "That's interesting!"

# Process input with NLP
def process_input(user_input):
    """Process input using NLP and generate a response."""
    doc = nlp(user_input)

    if "name" in user_input and "my" in user_input:
        words = user_input.split()
        name_index = words.index("name") + 2
        if name_index < len(words):
            return f"Nice to meet you, {words[name_index]}!"

    sentiment_response = get_sentiment(user_input)
    
    response = chatbot.respond(user_input)
    return response if response else sentiment_response

# Run chatbot
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Take care!")
            break
        response = process_input(user_input)
        print(f"Chatbot: {response}")

chat()
