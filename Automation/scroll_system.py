import pyautogui

# Scroll control functions
def scroll_up():
    for _ in range(5):
        pyautogui.press('up')

def scroll_down():
    for _ in range(5):
        pyautogui.press('down')

def scroll_to_top():
    pyautogui.hotkey('home')

def scroll_to_bottom():
    pyautogui.hotkey('end')


def perform_scroll_action(text):
    text = text.lower()

    if "scroll up" in text or "upar le jao" in text or "upar karo" in text:
        scroll_up()
    elif "scroll down" in text or "neeche le jao" in text or "neeche karo" in text:
        scroll_down()
    elif "top" in text or "scroll to top" in text or "shuru karo" in text:
        scroll_to_top()
    elif "bottom" in text or "scroll to bottom" in text or "khatam karo" in text:
        scroll_to_bottom()
    else:
        pass



