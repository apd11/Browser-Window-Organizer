#make sure to wipe memory each time hotkey is pressed
import tkinter as tk
from tkinter import messagebox
from hotkey_setup import create_hotkey  

# make all urls start with https://www.
def format_url(url):
    if not url.startswith("https://"):
        url = "https://" + url
    if not url.startswith("https://www."):
        url = url.replace("https://", "https://www.")
    return url

#open inputted urls with hotkeys
def open_with_hotkey():
    urls = [format_url(url_entry1.get()),format_url(url_entry2.get()),format_url(url_entry3.get())]

    create_hotkey(urls) # use hot keys to open entered urls

def create_gui():
    root = tk.Tk()
    root.title("Browser Window Organizer")
    root.geometry("700x500")

    label = tk.Label(root, text="Welcome to the Browser Window Organizer", font=("Arial", 14))
    label.pack(pady=10)

    global url_entry1, url_entry2, url_entry3

    url_entry1 = tk.Entry(root, width=50, font = ("Arial", 12))
    url_entry1.pack(pady=5)

    url_entry2 = tk.Entry(root, width=50, font = ("Arial", 12))
    url_entry2.pack(pady=5)

    url_entry3 = tk.Entry(root, width=50, font = ("Arial", 12))
    url_entry3.pack(pady=5)

    instruction_button = tk.Button(root, text="Show Instructions", command=show_instructions, font=("Arial", 12))
    instruction_button.pack(pady=20)

    hotkey_button = tk.Button(root, text = "Activate Hotkeys", command=open_with_hotkey, font= ("Arial, 12"))
    hotkey_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
    exit_button.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", root.quit)  # Ensure proper exit
    root.mainloop()

def show_instructions():
    instructions = (
        "Instructions:\n\n"
        "1. Enter URLS in text field.\n "
        "2. Press Ctrl + Q to open the browser windows.\n"
        "3. Press Ctrl + Shift + Q to close all browser windows."
    )
    messagebox.showinfo("Instructions", instructions)

if __name__ == "__main__":
    create_gui()
