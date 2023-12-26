import tkinter as tk
from tkinter import messagebox
import random

# Read affirmations from a text file
def read_affirmations(filename):
    with open(filename, 'r') as file:
        affirmations = file.readlines()
    return [line.strip() for line in affirmations]

# Show a random affirmation in a pop-up window
def show_affirmation(affirmations):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    affirmation = random.choice(affirmations)

    messagebox.showinfo("Affirmation", affirmation)
    root.destroy()  # Close the pop-up window

if __name__ == "__main__":
    affirmation_file = "affirmations.txt"
    affirmations = read_affirmations(affirmation_file)

    show_affirmation(affirmations)
