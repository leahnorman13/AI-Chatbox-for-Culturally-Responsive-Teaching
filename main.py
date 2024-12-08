# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(Lauren):
    #(f'Hi,Lauren}')
    print(f'Hi, )  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __Lauren__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Import necessary libraries
import openai  # For AI-based responses
from datetime import datetime

# OpenAI API key setup
openai.api_key = "your_openai_api_key"

# Knowledge base for CRT and Sustainability
knowledge_base = {
    "culturally responsive teaching": "CRT emphasizes integrating students' cultural identities into the learning process to foster inclusivity.",
    "sustainability": "Sustainability involves meeting the needs of the present without compromising the ability of future generations to meet theirs.",
    "SDG 4": "Quality Education - Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.",
    "SDG 11": "Sustainable Cities and Communities - Make cities inclusive, safe, resilient, and sustainable.",
}

# Function to generate AI responses
def generate_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error generating response: {e}"

# Function to handle user queries
def handle_query(user_input):
    # Check if the input matches the knowledge base
    for key, value in knowledge_base.items():
        if key in user_input.lower():
            return f"Here’s what I found on '{key}': {value}"

    # If not, pass the query to the AI for response
    ai_prompt = f"You are a culturally responsive and sustainability-focused chat assistant. Answer the user's query: {user_input}"
    return generate_response(ai_prompt)

# Main loop for the chatbox
def chatbox():
    print("Welcome to the Culturally Responsive Education and Sustainability Chatbox!")
    print("Type 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbox: Thank you for using the chatbox. Goodbye!")
            break
        response = handle_query(user_input)
        print(f"Chatbox: {response}")

# Start the chatbox
if __name__ == "__main__":
    chatbox()
