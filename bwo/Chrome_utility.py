import os
import subprocess
import platform
import pygetwindow as gw

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
           
    else:
        print("Google Chrome not found. Please install it or specify the path manually.")

def close_windows():
    windows = gw.getWindowsWithTitle("Google Chrome")
    for window in windows:
        window.close()
