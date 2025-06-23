import random

# Dictionary of keywords and possible funny responses
responses = {
    "hello": ["Hi there, human!", "Greetings, mortal!", "Oh hey, it's you again!"],
    "how are you": ["I'm just code, but emotionally stable.", "Living the digital dream!", "Better than your WiFi connection."],
    "bye": ["Goodbye! Don’t miss me too much.", "Later, tater!", "Farewell, flesh-being!"],
    "name": ["I'm ChatPy3000, the budget Siri.", "You can call me Boss Bot.", "Just a friendly ghost in your machine."],
    "weather": ["It's always cloudy in my server.", "I prefer electric storms. I'm solar-powered."],
    "joke": ["Why did the computer go to therapy? It had too many 'bytes' of emotional baggage.", 
             "Why was the JavaScript developer sad? Because he didn't 'null' his feelings."],
}

def get_response(message):
    message = message.lower()

    # Loop through keywords to find a match
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    
    # Default response if no keyword matches
    return random.choice([
        "Hmm... I didn’t quite catch that. Try typing 'joke' maybe?",
        "I'm not trained for that yet. But give me coffee and I’ll learn.",
        "You speak in riddles, stranger.",
        "Error 404: Witty response not found."
    ])

print("🤖 ChatPy3000: Hello! I'm your friendly chatbot. (Type 'bye' to quit)\n")

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("🤖 ChatPy3000:", response)
    if "bye" in user_input.lower():
        break
