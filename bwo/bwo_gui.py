import tkinter as tk
from tkinter import messagebox
from hotkey_setup import create_hotkey  

urls = [
    'https://www.google.com',
    'https://www.github.com',
    'https://www.youtube.com',

]

def create_gui():
    root = tk.Tk()
    root.title("Browser Window Organizer")
    root.geometry("400x200")

    label = tk.Label(root, text="Welcome to the Browser Window Organizer", font=("Arial", 14))
    label.pack(pady=10)

    instruction_button = tk.Button(root, text="Show Instructions", command=show_instructions, font=("Arial", 12))
    instruction_button.pack(pady=20)

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
    exit_button.pack(pady=10)

    # Call create_hotkeys to register hotkeys
    create_hotkey(urls)

    root.protocol("WM_DELETE_WINDOW", root.quit)  # Ensure proper exit
    root.mainloop()

def show_instructions():
    instructions = (
        "Instructions:\n\n"
        "1. Press Ctrl + Q to open the browser windows.\n"
        "2. Press Ctrl + Shift + Q to close all browser windows."
    )
    messagebox.showinfo("Instructions", instructions)

if __name__ == "__main__":
    create_gui()
