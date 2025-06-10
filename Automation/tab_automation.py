import pyautogui

# Function definitions
def open_new_tab():
    pyautogui.hotkey('ctrl', 't')

def close_tab():
    pyautogui.hotkey('ctrl', 'w')

def open_browser_menu():
    pyautogui.hotkey('alt', 'f')

def zoom_in():
    pyautogui.hotkey('ctrl', '+')

def zoom_out():
    pyautogui.hotkey('ctrl', '-')

def refresh_page():
    pyautogui.hotkey('ctrl', 'r')

def switch_to_next_tab():
    pyautogui.hotkey('ctrl', 'tab')

def switch_to_previous_tab():
    pyautogui.hotkey('ctrl', 'shift', 'tab')

def open_history():
    pyautogui.hotkey('ctrl', 'h')

def open_bookmarks():
    pyautogui.hotkey('ctrl', 'b')

def go_back():
    pyautogui.hotkey('alt', 'left')

def go_forward():
    pyautogui.hotkey('alt', 'right')

def open_dev_tools():
    pyautogui.hotkey('ctrl', 'shift', 'i')

def toggle_full_screen():
    pyautogui.hotkey('f11')

def open_private_window():
    pyautogui.hotkey('ctrl', 'shift', 'n')


# Function to perform action based on user input
def perform_action(text):
    text = text.lower()

    if "new tab" in text or "tab kholo" in text:
        open_new_tab()
    elif "close tab" in text or "tab band" in text:
        close_tab()
    elif "menu" in text:
        open_browser_menu()
    elif "zoom in" in text or "zoom badhao" in text:
        zoom_in()
    elif "zoom out" in text or "zoom ghatao" in text:
        zoom_out()
    elif "refresh" in text or "page reload" in text:
        refresh_page()
    elif "next tab" in text or "aage tab" in text:
        switch_to_next_tab()
    elif "previous tab" in text or "pichla tab" in text:
        switch_to_previous_tab()
    elif "history" in text or "itihaas" in text:
        open_history()
    elif "bookmark" in text or "bookmarks" in text:
        open_bookmarks()
    elif "go back" in text or "peeche jao" in text:
        go_back()
    elif "go forward" in text or "aage badho" in text:
        go_forward()
    elif "dev tools" in text or "developer tools" in text:
        open_dev_tools()
    elif "full screen" in text or "poora screen" in text:
        toggle_full_screen()
    elif "private window" in text or "incognito" in text or "gopniya window" in text:
        open_private_window()
    else:
        pass



