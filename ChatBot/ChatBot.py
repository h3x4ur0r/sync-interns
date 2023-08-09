import os
import openai
import dotenv

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI")


def get_chatbot_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()


def main():
    print("Chatbot: Hello! I'm your friendly chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        prompt = f"You: {user_input}\nChatbot:"

        bot_response = get_chatbot_response(prompt)
        print("Chatbot:", bot_response)


if __name__ == "__main__":
    main()
