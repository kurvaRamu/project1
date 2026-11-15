print("I am your chatBot assistant. How can I assist you today?")
print("Please type your message below:")
while True:
    user_input = input("You: ")
    user_input.lower().strip()
    if user_input=="hello":
        print("chatBot: Hello! How can I help you?")
    elif user_input=="hii":
        print("chatBot: Hi there! What can I do for you?")
    elif user_input=="how are you":
        print("chatBot: I'm just a bot, but I'm functioning well! How about you?")
    elif user_input=="what is your name":
        print("chatBot: I am your chatBot assistant. You can call me ChatBot!")
    elif user_input=="exit":
        print("chatBot: Goodbye! Have a great day!")
        break
    else:
        print("chatBot: I'm sorry, I didn't understand that. Can you please rephrase?")          
