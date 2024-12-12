import nltk
from nltk.chat.util import Chat, reflections

# Ensure NLTK data is downloaded
nltk.download('punkt', quiet=True)

# Pairs for the chatbot (pattern-response pairs)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!het How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"(what's|what is) your name?",
        ["I am a chatbot created to assist you.", "My name is Chatbot! What can I do for you?"]
    ],
    [
        r"how are you|how are you doing",
        ["I'm just a bunch of code, but I'm here to help you!", "I'm doing great, thanks for asking!"]
    ],
    [
        r"(.*) help (.*)",
        ["I am here to help with anything I can. Please tell me more about the issue."]
    ],
    [
        r"(.*) your favorite (.*)",
        ["I don't have preferences, but I enjoy helping you!"]
    ],
    [
        r"(bye|goodbye|see you)",
        ["Goodbye! Have a great day!", "See you later! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand that. Could you please clarify?", "Interesting! Tell me more."]
    ]
]


chatbot = Chat(pairs, reflections)

def start_chatbot():
    print("Chatbot: Hello! Type 'bye' to exit the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    start_chatbot()
