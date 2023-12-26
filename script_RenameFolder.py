import os
import tkinter as tk
from tkinter import filedialog

def rename_files_in_folder(folder_path, prefix):
    try:
        file_list = os.listdir(folder_path)
        for filename in file_list:
            if os.path.isfile(os.path.join(folder_path, filename)):
                extension = os.path.splitext(filename)[1]  # Get the file extension
                new_filename = f"{prefix}{extension}"
                new_path = os.path.join(folder_path, new_filename)
                counter = 1
                while os.path.exists(new_path):
                    new_filename = f"{prefix}_{counter}{extension}"
                    new_path = os.path.join(folder_path, new_filename)
                    counter += 1
                os.rename(os.path.join(folder_path, filename), new_path)
        result_label.config(text="Renaming completed.")
    except Exception as e:
        result_label.config(text=f"An error occurred: {e}")

def browse_folder():
    folder_path = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, folder_path)

def rename_files():
    folder_path = folder_entry.get()
    prefix = prefix_entry.get()
    rename_files_in_folder(folder_path, prefix)

# Create the main window
root = tk.Tk()
root.title("File Renamer")

# Create and pack widgets
folder_label = tk.Label(root, text="Select Folder:")
folder_label.pack()
folder_entry = tk.Entry(root, width=40)
folder_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_folder)
browse_button.pack()
prefix_label = tk.Label(root, text="Prefix:")
prefix_label.pack()
prefix_entry = tk.Entry(root, width=40)
prefix_entry.pack()
rename_button = tk.Button(root, text="Rename Files", command=rename_files)
rename_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
