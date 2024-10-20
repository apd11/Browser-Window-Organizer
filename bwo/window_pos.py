import pygetwindow as gw
import pyautogui
import time


def window_positions():
    time.sleep(1) 

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

    sizes = [
        (long_w_width, long_w_height),
        (small_w_width, small_w_height),
        (small_w_width, small_w_height)
    ]

    for i, window in enumerate(windows[:3]):
        if window.isMaximized: #check if window is maximized
            window.restore() #put window in normal size 
        
        #resize and position the three windows
        window.moveTo(position[i][0],position[i][1])
        window.resizeTo(sizes[i][0], sizes[i][1])
    