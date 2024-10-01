import os
#import webbrowser
import time
import subprocess
import platform
import keyboard
import pygetwindow as gw 
import pyautogui

def find_chrome_path():
    system = platform.system()
    if system == 'Windows':
        possible_paths = [
            'C:/Program Files/Google/Chrome/Application/chrome.exe',
            'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
        ]
    elif system == 'Darwin':  # macOS
        possible_paths = [
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        ]
    elif system == 'Linux':
        possible_paths = [
            '/usr/bin/google-chrome',
            '/usr/bin/chromium-browser'
        ]
    else:
        raise OSError('Unsupported OS')

    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None

def open_in_chrome(urls):
    chrome_path = find_chrome_path()
    if chrome_path:
        for url in urls:
            subprocess.Popen([chrome_path, '--new-window', url])
           # browser.open_new(url)

def window_positions():
    time.sleep(0.6) 
    windows = gw.getWindowsWithTitle("Google Chrome")

    if len(windows) < 3:
        print("could not find all windows")

    s_width, s_height = pyautogui.size() # find screen size

    long_w_width = s_width // 2 #calculate width for windows
    long_w_height = s_height # calculate height for windows

    small_w_width = s_width // 2
    small_w_height = s_height // 2
    
    position = [
        (0,0), #left long window
        (long_w_width, 0),# top right
        (long_w_width, small_w_height)
    ]

    windows[0].moveTo(position[0][0], position[0][1])  # Left window
    windows[0].resizeTo(long_w_width, long_w_height)
    
    windows[1].moveTo(position[1][0], position[1][1])  
    windows[1].resizeTo(small_w_width, small_w_height)
    
    windows[2].moveTo(position[2][0], position[2][1])  # Bottom right window
    windows[2].resizeTo(small_w_width, small_w_height)

def open_windows():
    open_in_chrome(url)
    window_positions()


def close_windows():
    windows = gw.getWindowsWithTitle("Google Chrome")
    for window in windows:
        window.close()

def hotkey():
    keyboard.add_hotkey('ctrl+q', open_windows)
    keyboard.add_hotkey('ctrl+shift+q', close_windows)

    while True:
        time.sleep(1)

# URL List
url = [
    'https://www.google.com',
    'https://www.github.com',
    'https://www.Youtube.com',

]


hotkey()