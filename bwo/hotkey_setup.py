import threading
import time
import keyboard
from chrome_utility import open_in_chrome, close_windows
from window_pos import window_positions

def open_windows(urls):
    open_in_chrome(urls)
    window_positions()

def create_hotkey(urls):
    keyboard.add_hotkey('ctrl+q', lambda: open_windows(urls))
    keyboard.add_hotkey('ctrl+shift+q', close_windows)

def rm_hotkey(): #remove hotkey 
    keyboard.remove_hotkey('ctrl+q')
    keyboard.remove_hotkey('ctrl+shift+q')

def setup_hotkeys(urls):
    # Start the hotkey listener in a separate thread
    listener_thread = threading.Thread(target=create_hotkey, args=(urls,), daemon=True)
    listener_thread.start()

    keyboard.wait()
    '''
    while True:
        time.sleep(1)
        '''