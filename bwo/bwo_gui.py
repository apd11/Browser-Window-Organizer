import time
import tkinter as tk
from tkinter import messagebox
from hotkey_setup import create_hotkey, rm_hotkey, open_windows

current_hotkey = None #custom url hotkey
 
current_hotkey_google = None #google custom hotkey

# make all urls start with https://www.
def format_url(url):
    if not url.startswith("https://"):
        url = "https://" + url
    if not url.startswith("https://www."):
        url = url.replace("https://", "https://www.")
    return url

#open inputted urls with hotkeys
def open_with_hotkey():
    global current_hotkey, current_hotkey_google

    if current_hotkey: #remove current hotkey
        rm_hotkey()
        current_hotkey = None
    
    if current_hotkey_google:
        rm_hotkey()
        current_hotkey_google = None


    urls = [format_url(url_entry3.get()),format_url(url_entry2.get()),format_url(url_entry1.get())]

    create_hotkey(urls) # use hot keys to open entered urls
    open_windows(urls)

    current_hotkey = True

def all_google():
    global current_hotkey_google, current_hotkey

    if current_hotkey: #remove current hotkey
        rm_hotkey()
        current_hotkey = None

    if current_hotkey_google: #remove current google hotkey
        rm_hotkey()
        current_hotkey_google = None

    timestamp = str(int(time.time()))
    urls = [
        f"https://www.google.com?time={timestamp}_1",
        f"https://www.google.com?time={timestamp}_2",
        f"https://www.google.com?time={timestamp}_3"
    ]
    open_windows(urls)
    create_hotkey(urls)

    current_hotkey_google = True

def create_gui():
    root = tk.Tk()
    root.title("Browser Window Organizer")
    root.geometry("700x500") #gui  size

    label = tk.Label(root, text="Welcome to the Browser Window Organizer", font=("Arial", 14))
    label.pack(pady=10)

    global url_entry1, url_entry2, url_entry3

    # instruction window
    instruction_button = tk.Button(root, text="Show Instructions", command=show_instructions, font=("Arial", 12))
    instruction_button.pack(pady=10)

    #button to open all windows as google.com
    google_button = tk.Button(root, text ="Open Google in All Windows",command = all_google, font=("Arial", 12))
    google_button.pack(pady=10)

#url label 1 
    url_label1 = tk.Label(root, text="URL 1 (Left Long Window):", font=("Arial", 10))
    url_label1.pack(pady=10)
    
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


#hotkey button
    hotkey_button = tk.Button(root, text = "Open Custom URLS", command=open_with_hotkey, font= ("Arial", 12))
    hotkey_button.pack(pady=10)


#exit button functionality
    root.protocol("WM_DELETE_WINDOW", root.quit)  
    root.mainloop()

def show_instructions():
    instructions = (
        " Instructions:\n\n"
        "\n"
        "Open All Windows in Google.com:\n"
        "1. Press Open Google in All Windows to open 3 windows in google.com\n"
        "\n"
        "Using Custom URLS:\n"
        "1. Type in 3 URLS (ex. flightaware.com)\n"
        "2. Press open custom URLS button\n"
        "\n"
        "Hotkeys Usage:\n"
        "1. Press Ctrl + Q to open the browser windows.\n"
        "2. Press Ctrl + Shift + Q to close all browser windows."
    )
    messagebox.showinfo("Instructions", instructions)

if __name__ == "__main__":
    create_gui()
