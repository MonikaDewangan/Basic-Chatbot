def get_bot_response(user_input):
    """Returns a response based on user input."""

    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey","hii"]:
        return "Hi! How can I help you today?"

    elif user_input == "how are you":
        return "I'm fine, thanks! How about you?"

    elif user_input in ["what is your name", "who are you"]:
        return "I'm a simple rule-based chatbot."

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome!"

    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I don't understand that."


def run_chatbot():
    print("===== Simple Rule-Based Chatbot =====")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ")

        response = get_bot_response(user)

        print("Bot:", response)

        if user.lower().strip() in ["bye", "goodbye", "exit"]:
            break


if __name__ == "__main__":
    run_chatbot()