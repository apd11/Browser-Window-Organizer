import time
import keyboard
from Chrome_utility import open_in_chrome, close_windows
from window_pos import window_positions

def open_windows(urls):
    open_in_chrome(urls)
    window_positions()

def create_hotkey(urls):
    keyboard.add_hotkey('ctrl+q', lambda: open_windows(urls))
    keyboard.add_hotkey('ctrl+shift+q', close_windows)

    while True:
        time.sleep(1)