import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import Scrollbar, Text


pairs = [
    ["hi|hello|hey", ["Hello! How can I assist you today?"]],
    ["what is your name?", ["I am a Chatbot. What's your name?"]],
    ["my name is (.*)", ["Hello %1! Nice to meet you."]],
    ["how are you?", ["I'm just a bot, but I'm here to help!"]],
    ["quit", ["Goodbye! Have a great day!"]],
    ["(.*)", ["I'm not sure how to answer that. Can you try asking something else?"]]
]

# Create the Chat object
chatbot = Chat(pairs, reflections)

# GUI Functionality
def send_message():
    user_input = user_entry.get()
    chat_box.insert(tk.END, f"You: {user_input}\n")
    if user_input.lower() == "quit":
        chat_box.insert(tk.END, "Bot: Goodbye! Have a great day!\n")
        root.quit()
    else:
        response = chatbot.respond(user_input)
        chat_box.insert(tk.END, f"Bot: {response}\n")
    user_entry.delete(0, tk.END)

# Setting up the GUI
root = tk.Tk()
root.title("Chatbot GUI")
root.geometry("500x400")

# Chat box
chat_box = Text(root, bd=1, bg="lightgrey", font="Arial")
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(chat_box)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_box.config(yscrollcommand=scrollbar.set)

# User input entry box
user_entry = tk.Entry(root, bd=1, bg="white", font="Arial")
user_entry.pack(pady=5, padx=10, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, bg="blue", fg="white", font="Arial")
send_button.pack(pady=10)

root.mainloop()
