import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm just a bot, but I'm doing fine!", "I'm doing well, thank you!", "I don't have feelings, but I'm here to help!"],
    "what's your name": ["I'm just a chatbot.", "I don't have a name, I'm a chatbot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def get_response(message):
    message = message.lower()
    
    for key in responses:
        if key in message:
            return random.choice(responses[key])
    
    return "I'm not sure how to respond to that."

print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)
