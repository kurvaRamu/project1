responses={
    "greeting": "Hello!", 
    "help": "How can I help you?", 
    "name": "What is your name?", 
    "bot_info": "I'm just a bot, but I'm functioning well! How about you?", 
    "goodbye": "Goodbye! Have a great day!"
}
print("I am your chatBot assistant. How can I assist you today?")
while True:
    user_input = input("You: ")
    user_input = user_input.lower().strip()
    if user_input in ["exit", "quit", "bye"]:
        print("chatBot: " + responses["goodbye"])
        break
    elif user_input in ["hello", "hi", "hey"]:
        print("chatBot: " + responses["greeting"])      
    elif user_input in ["help", "assist"]:
        print("chatBot: " + responses["help"])
    elif user_input in ["what is your name", "who are you"]:
        print("chatBot: " + responses["name"])
    elif user_input in ["how are you", "how's it going"]:
        print("chatBot: " + responses["bot_info"])
    else:
        print("chatBot: I'm sorry, I didn't understand that. Can you please rephrase?")
        