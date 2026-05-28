import random
from difflib import get_close_matches

BOT_NAME = "Nova"

knowledge_base = {
   "hello": [
        "Hi! I am Nova",
        "Hello! How can I help today?"
    ],
    "hi": [
        "Hi! I am Nova"
    ],
    "what is your name": [
        f"My name is {BOT_NAME}. I am a rule-based AI chatbot."
    ],
    "who are you": [
        f"I am {BOT_NAME}, a rule-based AI assistant created using Python and Flask."
    ],
    "how are you": [
        "I am working perfectly. Thanks for asking!",
        "I am doing great and ready to help."
    ],
    "what can you do": [
        "I can answer predefined questions, explain basic technology concepts, and guide this project."
    ],
    "help": [
        "Try asking: what is AI, what is GitHub, what is Python, what is Flask, or what is rule based chatbot."
    ],

    "thanks":[
        "You are welcome"
    ],

    "what is ai": [
        "AI means Artificial Intelligence. It allows machines to simulate human-like thinking and decision making."
    ],
    "what is artificial intelligence": [
        "Artificial Intelligence is a field of computer science where machines perform tasks that normally need human intelligence."
    ],
    "what is rule based chatbot": [
        "A rule-based chatbot gives answers using predefined rules, conditions, and a knowledge base."
    ],
    "what is python": [
        "Python is a popular programming language used for web development, AI, automation, and data science."
    ],
    "what is flask": [
        "Flask is a lightweight Python web framework used to build web applications and APIs."
    ],
    "what is github": [
        "GitHub is a platform used to store, manage, share, and collaborate on code projects."
    ],
    "what is git": [
        "Git is a version control system used to track changes in code."
    ],
    "what is html": [
        "HTML is used to create the structure of a web page."
    ],
    "what is css": [
        "CSS is used to style web pages with colors, layouts, fonts, and spacing."
    ],
    "what is javascript": [
        "JavaScript is used to make web pages interactive."
    ],
    "what is frontend": [
        "Frontend is the visible part of a website or app that users interact with."
    ],
    "what is backend": [
        "Backend is the server-side part that handles logic, data, and communication."
    ],

    "project goal": [
        "The goal of this project is to build a rule-based AI chatbot that responds to predefined user inputs."
    ],
    "project features": [
        "Main features: greeting response, predefined answers, fallback response, clean UI, and continuous chat."
    ],
    "how to run project": [
        "Run the project using: python app.py, then open http://127.0.0.1:5000 in the browser."
    ],
    "how to push github": [
        "Use: git add . then git commit -m \"message\" then git push origin main."
    ],

    "bye": [
        "Goodbye! Have a great day."
    ],
    "exit": [
        "Chat ended. See you again!"
    ],
    "quit": [
        "Okay, goodbye!"
    ]
}



def clean_text(text):
    return text.lower().strip().replace("?", "").replace(".", "").replace("!", "")


def get_bot_response(user_input):
    user_input = clean_text(user_input)

    if user_input == "":
        return "Please type something."

    if user_input in knowledge_base:
        return random.choice(knowledge_base[user_input])

    # keyword-based responses
    if "github" in user_input:
        return "GitHub helps developers store code, manage versions, and share projects online."

    if "python" in user_input:
        return "Python is easy to learn and useful for AI, web development, and automation."

    if "ai" in user_input or "artificial intelligence" in user_input:
        return "AI allows computers to perform tasks that need human-like intelligence."

    if "flask" in user_input:
        return "Flask helps connect Python backend logic with a web interface."

    if "project" in user_input:
        return "This project is a web-based rule-based AI chatbot using Python, Flask, HTML, CSS, and JavaScript."

    # fuzzy matching
    possible_questions = list(knowledge_base.keys())
    match = get_close_matches(user_input, possible_questions, n=1, cutoff=0.6)

    if match:
        return random.choice(knowledge_base[match[0]])

    return "Sorry, I don't understand that yet. Try asking about AI, Python, Flask, GitHub, or this project."
