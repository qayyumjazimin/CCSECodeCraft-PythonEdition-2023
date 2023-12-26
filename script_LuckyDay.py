import tkinter as tk
from tkinter import Toplevel, Label

# Dictionary of motivational phrases
motivational_phrases = {
    1: "Believe in yourself!",
    2: "The best is yet to come.",
    3: "You are doing great!",
    4: "Never give up.",
    5: "Chase your dreams.",
    6: "Stay strong and positive.",
    7: "Keep pushing forward.",
    8: "You are capable of amazing things.",
    9: "Every day is a new opportunity.",
    10: "Success is just around the corner."
}

def save_to_file(name, lucky_number, motivational_message):
    with open("This is from me to you.txt", "a") as file:
        file.write(f"Name: {name}, Lucky Number: {lucky_number}, Message: {motivational_message}\n")

def show_motivational_message(name, lucky_number):
    motivational_message = motivational_phrases.get(int(lucky_number), "")
    save_to_file(name, lucky_number, motivational_message)
    message_window = Toplevel(root)
    message_window.title("Motivational Message")
    Label(message_window, text=f"Name: {name}\nLucky Number: {lucky_number}\n\n{motivational_message}",
          font=("Arial", 16, "bold")).pack(pady=20)
    message_window.mainloop()

def submit_action():
    name = name_entry.get()
    lucky_number = number_entry.get()
    if name and lucky_number.isdigit() and 1 <= int(lucky_number) <= 10:
        show_motivational_message(name, lucky_number)
    else:
        tk.messagebox.showerror("Invalid Input", "Please enter a valid name and a lucky number between 1 and 10.")

# Create the main window
root = tk.Tk()
root.title("CCSE Code Craft: Python Edition")

# Maximize the window
root.state('zoomed')

# Add the title
title_label = tk.Label(root, text="CCSE Code Craft: Python Edition", font=("Arial", 18, "bold"))
title_label.pack(pady=20)

# Create and place the name label and entry field
name_label = tk.Label(root, text="Enter your name:", font=("Arial", 14))
name_label.pack(pady=10)
name_entry = tk.Entry(root, font=("Arial", 14), width=50)
name_entry.pack(pady=10)

# Create and place the number label and entry field
number_label = tk.Label(root, text="Enter your lucky number (1-10):", font=("Arial", 14))
number_label.pack(pady=10)
number_entry = tk.Entry(root, font=("Arial", 14), width=50)
number_entry.pack(pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_action, font=("Arial", 14))
submit_button.pack(pady=20)

# Start the GUI loop
root.mainloop()
