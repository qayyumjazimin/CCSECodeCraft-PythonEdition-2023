import tkinter as tk
from tkinter import messagebox
import random

def show_message(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Generate random coordinates
    x = random.randint(0, screen_width - 200)  # Adjust 200 as needed for your message size
    y = random.randint(0, screen_height - 100)  # Adjust 100 as needed for your message size
    
    root.geometry(f"+{x}+{y}")  # Set the window position

    def close_window():
        root.destroy()
    
    # Create an OK button to close the window
    ok_button = tk.Button(root, text="OK", command=close_window)
    ok_button.pack()

    result = messagebox.showinfo("Love Confession", message)
    
if __name__ == "__main__":
    messages = [
        "Hi",
        "I want to say something",
        "but I'm shy",
        "but if I don't tell now, I will regret it forever",
        "I've been thinking about you lately. You mean the world to me. I like you",
        "Hihi."
    ]

    for message in messages:
        show_message(message)
