#make sure to wipe memory each time hotkey is pressed
import tkinter as tk
from tkinter import messagebox
from hotkey_setup import create_hotkey, rm_hotkey  

current_hotkey = None
# make all urls start with https://www.
def format_url(url):
    if not url.startswith("https://"):
        url = "https://" + url
    if not url.startswith("https://www."):
        url = url.replace("https://", "https://www.")
    return url

#open inputted urls with hotkeys
def open_with_hotkey():
    global current_hotkey

    if current_hotkey: #remove current hotkey
        rm_hotkey()

    urls = [format_url(url_entry3.get()),format_url(url_entry1.get()),format_url(url_entry2.get())]

    create_hotkey(urls) # use hot keys to open entered urls

    current_hotkey = True

def create_gui():
    root = tk.Tk()
    root.title("Browser Window Organizer")
    root.geometry("700x500")

    label = tk.Label(root, text="Welcome to the Browser Window Organizer", font=("Arial", 14))
    label.pack(pady=10)

    global url_entry1, url_entry2, url_entry3

#url label 1 
    url_label1 = tk.Label(root, text="URL 1 (Left Long Window):", font=("Arial", 10))
    url_label1.pack(pady=5)
    
# url entry 1
    url_entry1 = tk.Entry(root, width=50, font=("Arial", 12))
    url_entry1.pack(pady=5)

#url label 2
    url_label2 = tk.Label(root, text="URL 2 (Top Right Window):", font=("Arial", 10))
    url_label2.pack(pady=5)
   
# url entry 2
    url_entry2 = tk.Entry(root, width=50, font=("Arial", 12))
    url_entry2.pack(pady=5)

#url label 3
    url_label3 = tk.Label(root, text="URL 3 (Bottom Right Window):", font=("Arial", 10))
    url_label3.pack(pady=5)

# url entry 3
    url_entry3 = tk.Entry(root, width=50, font=("Arial", 12))
    url_entry3.pack(pady=5)


# instruction window
    instruction_button = tk.Button(root, text="Show Instructions", command=show_instructions, font=("Arial", 12))
    instruction_button.pack(pady=20)

#hotkey button
    hotkey_button = tk.Button(root, text = "Activate Hotkeys", command=open_with_hotkey, font= ("Arial, 12"))
    hotkey_button.pack(pady=10)

#exit button
    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
    exit_button.pack(pady=10)

#exit button functionality
    root.protocol("WM_DELETE_WINDOW", root.quit)  
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
