import re

responses = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I'm just a chatbot, but I'm doing great! How about you?",
    "what is your name": "I'm your friendly chatbot. What's yours?",
    "bye": "Goodbye! Have a great day!",
    "thank you": "You're welcome! Anything else you need help with?",
    "help": "Sure! I'm here to assist you. What do you need help with?",
    "what can you do": "I can chat with you, answer simple questions, and help you with basic tasks. What do you need?",
    "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
    "what is the time": "I'm sorry, I can't tell time. But you can check the clock on your device!",
    "where are you from": "I'm from the digital realm, created to assist and entertain you!",
    "what is your purpose": "My purpose is to help you with tasks, answer questions, and make your day a little better!",
    "who created you": "I was created by Revanth an enthsiastic AI developer."
}

def get_response(user_input):
    
    user_input = user_input.lower().strip()
    
    if user_input in responses:
        return responses[user_input]
    
    
    elif re.search(r'\bhow\b.*\byou\b', user_input):
        return "I'm doing well, thank you! How can I assist you?"
    elif re.search(r'\bwhat\b.*\byour name\b', user_input):
        return "I'm a chatbot here to help you. What can I do for you?"
    elif re.search(r'\bwho\b.*\byou\b', user_input):
        return "I'm your friendly chatbot. How can I assist you today?"
    
    else:
        return "I'm not sure I understand that. Can you please rephrase?"


def chat():
    print("Chatbot: Hello! Type 'bye' to exit the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)


chat()
