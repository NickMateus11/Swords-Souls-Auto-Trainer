import pyautogui
import sys
from PIL import ImageGrab
from time import sleep


def getRGBPixel(x,y):
    pixel = (x,y,x+1,y+1)
    return ImageGrab.grab(pixel).load()[0,0]


def showRGB():
    try:
        print("Use ctrl-c to stop")
        print("R G B:")
        while True:
            data = getRGBPixel(*pyautogui.position())
            strData = f' ({str(data[0]).rjust(3)},'
            strData += f' {str(data[1]).rjust(3)},'
            strData += f' {str(data[2]).rjust(3)})'
            sys.stdout.write(strData)
            sys.stdout.write('\b' * len(strData))
            sys.stdout.flush()
    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.stdout.flush()


showRGB()
# pyautogui.displayMousePosition()