import sys

import pyautogui
from PIL import ImageGrab

from pynput.mouse import Listener
from pynput import mouse


def getRGBPixel(x,y):
    pixel = (x,y,x+1,y+1)
    return ImageGrab.grab(pixel).load()[0,0]


def showRGB():
    try:
        print("Use ctrl-c to stop")
        print("R G B:")

        while True:
            mouse_xy = pyautogui.position()
            RGBdata = getRGBPixel(*mouse_xy)
            strData = f' ({str(RGBdata[0]).rjust(3)},'
            strData += f' {str(RGBdata[1]).rjust(3)},'
            strData += f' {str(RGBdata[2]).rjust(3)})'
            sys.stdout.write(strData)
            sys.stdout.write('\b' * len(strData))
            sys.stdout.flush()

    except KeyboardInterrupt:
        sys.stdout.write('\n')
        sys.stdout.flush()


def on_click(x, y, button, pressed):
    if pressed and button != mouse.Button.right:
        f = open('mouse_x,y_and_pixel_RGB.txt','a')
        fileData = f'{x} {y}, RGB: {getRGBPixel(x,y)}'
        f.write(fileData + '\n')
        f.close()
    if button == mouse.Button.right:
        return False


# Clear file
f = open('mouse_x,y_and_pixel_RGB.txt','w')
f.close()

with Listener(on_click=on_click) as listener:
    listener.join()

# showRGB()
# pyautogui.displayMousePosition()