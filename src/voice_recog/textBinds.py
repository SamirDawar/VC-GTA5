import pyautogui


def forward():
    pyautogui.press('w', presses=10)


def backwards():
    pyautogui.press('s', presses=10)

def left():
    pyautogui.press('a', presses=5)

def long_left():
    pyautogui.press('a', presses=10)

def right():
    pyautogui.press('d', presses=5)

def long_right():
    pyautogui.press('d', presses=10)


