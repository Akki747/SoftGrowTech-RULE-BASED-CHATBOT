def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hi there! 👋")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just code, but I'm doing great! 😄")

        elif "your name" in user_input or "who are you" in user_input:
            print("🤖 Chatbot: I'm a rule-based chatbot created for an AI project.")

        elif "help" in user_input:
            print("🤖 Chatbot: You can greet me, ask time/date, ask my name, or say bye.")

        elif "time" in user_input:
            import datetime
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: Current time is {now}")

        elif "date" in user_input:
            import datetime
            today = datetime.date.today()
            print(f"🤖 Chatbot: Today's date is {today}")

        elif "thank you" in user_input or "thanks" in user_input:
            print("🤖 Chatbot: You're welcome! 😊")

        elif "what can you do" in user_input:
            print("🤖 Chatbot: I can chat with you using simple rules and answer basic questions!")

        elif "who created you" in user_input:
            print("🤖 Chatbot: I was created as part of an AI internship project.")

        elif "joke" in user_input:
            print("🤖 Chatbot: Why did the computer go to the doctor? 🤔 Because it caught a virus! 😂")

        elif "weather" in user_input:
            print("🤖 Chatbot: I can't check live weather yet, but I hope it's nice outside! ☀️")

        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye!")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that. Try asking something else.")

chatbot()