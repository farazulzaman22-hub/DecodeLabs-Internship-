import datetime

# Welcome message
print("=" * 50)
print("Bot: Hello! I am DecodeBot 🤖")
print("Bot: I'm a rule-based assistant created at DecodeLabs.")
print("Bot: Type 'exit', 'quit', or 'bye' anytime to end the chat.")
print("=" * 50)

# Knowledge base - dictionary of predefined responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to see you.",
    "hey": "Hey! What's up?",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "what is your name": "I'm DecodeBot, your friendly rule-based assistant.",
    "what can you do": "I can chat with you using predefined responses, tell you the time, and a few other tricks!",
    "who created you": "I was created as part of a DecodeLabs AI internship project.",
    "what is ai": "AI stands for Artificial Intelligence - the simulation of human intelligence by machines.",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "No problem, anytime!",
}

# Main loop - keeps running until user exits
while True:
    raw_input_text = input("You: ")
    user_input = raw_input_text.lower().strip()

    # Exit condition
    if user_input in ["exit", "quit", "bye"]:
        print("Bot: Goodbye! Have a great day. 👋")
        break

    # Special case: nested condition for time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time}.")

    # Special case: nested condition for name input
    elif "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().title()
        print(f"Bot: Nice to meet you, {name}! How can I help you?")

        # Help command
    elif user_input == "help":
        print("Bot: You can ask me things like:")
        print("Bot: - hello / hi / hey")
        print("Bot: - how are you")
        print("Bot: - what is your name")
        print("Bot: - what is ai")
        print("Bot: - tell me a joke")
        print("Bot: - my name is <your name>")
        print("Bot: - what is the time")
        print("Bot: - exit / quit / bye (to end chat)")

    # Keyword-based matching for "ai" related questions
    elif "ai" in user_input and "what" in user_input:
        print("Bot: AI stands for Artificial Intelligence - the simulation of human intelligence by machines.")

    else:
        # Lookup response, fallback if not found
        reply = responses.get(user_input, "I do not understand. Can you rephrase that, or type 'help' for options?")
        print("Bot:", reply)