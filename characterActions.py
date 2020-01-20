import pyautogui
from time import sleep

def keyPress(key, hold_time=0):
    pyautogui.keyDown(key)
    if hold_time > 0:
        sleep(hold_time)
    pyautogui.keyUp(key)

