import pyautogui

# Media control functions
def volume_up():
    pyautogui.press('up')

def volume_down():
    pyautogui.press('down')

def seek_forward():
    pyautogui.press('right')

def seek_backward():
    pyautogui.press('left')

def seek_forward_10s():
    pyautogui.press('l')

def seek_backward_10s():
    pyautogui.press('j')

def seek_backward_frame():
    pyautogui.press(',')

def seek_forward_frame():
    pyautogui.press('.')

def seek_to_beginning():
    pyautogui.press('home')

def seek_to_end():
    pyautogui.press('end')

def seek_to_previous_chapter():
    pyautogui.hotkey('ctrl', 'left')

def seek_to_next_chapter():
    pyautogui.hotkey('ctrl', 'right')

def decrease_playback_speed():
    pyautogui.hotkey('shift', ',')

def increase_playback_speed():
    pyautogui.hotkey('shift', '.')

def move_to_next_video():
    pyautogui.hotkey('shift', 'n')

def move_to_previous_video():
    pyautogui.hotkey('shift', 'p')


def perform_media_action(text):
    text = text.lower()

    if "volume up" in text or "awaz badhao" in text:
        volume_up()
    elif "volume down" in text or "awaz kam karo" in text:
        volume_down()
    elif "forward" in text and "10" in text:
        seek_forward_10s()
    elif "backward" in text and "10" in text:
        seek_backward_10s()
    elif "seek forward" in text or "aage badho" in text:
        seek_forward()
    elif "seek backward" in text or "peeche jao" in text:
        seek_backward()
    elif "frame forward" in text:
        seek_forward_frame()
    elif "frame backward" in text:
        seek_backward_frame()
    elif "start" in text or "shuru" in text:
        seek_to_beginning()
    elif "end" in text or "khatam" in text:
        seek_to_end()
    elif "previous chapter" in text:
        seek_to_previous_chapter()
    elif "next chapter" in text:
        seek_to_next_chapter()
    elif "increase speed" in text or "tez karo" in text:
        increase_playback_speed()
    elif "decrease speed" in text or "slow karo" in text:
        decrease_playback_speed()
    elif "next video" in text:
        move_to_next_video()
    elif "previous video" in text:
        move_to_previous_video()
    else:
        pass



