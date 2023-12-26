import tkinter as tk
from tkinter import messagebox
import random
import webbrowser

# Read affirmations from a text file
def read_affirmations(filename):
    with open(filename, 'r') as file:
        affirmations = file.readlines()
    return [line.strip() for line in affirmations]

# Show a random affirmation in a pop-up window and search for it in Google Images
def show_affirmation(affirmations):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    affirmation = random.choice(affirmations)

    messagebox.showinfo("Affirmation", affirmation)
    root.destroy()  # Close the pop-up window

    # Perform a web search for the affirmation in Google Images
    search_word = affirmation

    # Construct the search URL for Google Images
    search_url = f"https://www.google.com/search?q={search_word.replace(' ', '+')}&tbm=isch"

    # Open the web browser with the search results in Google Images
    webbrowser.open(search_url)

if __name__ == "__main__":
    affirmation_file = "affirmations.txt"
    affirmations = read_affirmations(affirmation_file)

    show_affirmation(affirmations)
