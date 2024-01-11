import random

# Define a list of medical-related questions and answers
questions = [
    "What are the symptoms of COVID-19?",
    "How can I prevent heart disease?",
    "What are the common side effects of medication X?",
    # Add more questions here
]

answers = [
    "The symptoms of COVID-19 include fever, cough, and difficulty breathing.",
    "To prevent heart disease, you should maintain a healthy diet, exercise regularly, and avoid smoking.",
    "Common side effects of medication X may include nausea, headache, and dizziness.",
    # Add more answers here
]

# Define a function to generate a random response
def get_response(question):
    if question in questions:
        index = questions.index(question)
        return answers[index]
    else:
        return "I'm sorry, I don't have an answer for that question."

# Main loop
while True:
    user_input = input("User: ")
    response = get_response(user_input)
    print("Chatbot:", response)

