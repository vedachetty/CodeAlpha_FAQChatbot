from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

questions = [
    "What is your name",
    "What are your working hours",
    "Where are you located",
    "What services do you provide",
    "How can I contact support",
    "Do you provide internships",
    "What is AI",
    "What is machine learning"
]

answers = [
    "I am an AI FAQ Chatbot.",
    "We work from 9 AM to 6 PM.",
    "We are located in Hyderabad.",
    "We provide AI and software services.",
    "You can contact support at support@gmail.com.",
    "Yes, we provide internships.",
    "Artificial Intelligence is simulation of human intelligence by machines.",
    "Machine Learning is a subset of AI that learns from data."
]

root = Tk()
root.title("FAQ Chatbot")
root.geometry("700x600")
root.config(bg="#1e1e1e")

title = Label(
    root,
    text="AI FAQ Chatbot",
    font=("Arial", 24, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)
title.pack(pady=10)

chat_area = Text(
    root,
    height=20,
    width=70,
    font=("Arial", 12),
    bg="white"
)
chat_area.pack(pady=10)

user_input = Entry(
    root,
    width=50,
    font=("Arial", 14)
)
user_input.pack(pady=10)

def chatbot():

    user_question = user_input.get()

    all_text = questions + [user_question]

    cv = CountVectorizer()

    matrix = cv.fit_transform(all_text)

    similarity = cosine_similarity(matrix[-1], matrix[:-1])

    index = similarity.argmax()

    response = answers[index]

    chat_area.insert(END, "You: " + user_question + "\n\n")
    chat_area.insert(END, "Bot: " + response + "\n\n")

    user_input.delete(0, END)

ask_button = Button(
    root,
    text="Ask",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    padx=15,
    command=chatbot
)
ask_button.pack(pady=10)

root.mainloop()