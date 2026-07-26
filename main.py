from chatbot import ChatBot


bot = ChatBot()


print("=" * 40)
print("        AI CHATBOT")
print("=" * 40)

print("Type 'bye' to exit.")


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break


    response = bot.get_response(user_input)

    print("Bot:", response)
