import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray
def hit (k):
    pyautogui.keyDown(k)

def iscollide(value):
    for i in range(185,300):
        for j in range(420,450):
            if value[i,j]<100:
                hit("up")
                return True
    for i in range(185,300):
        for j in range(300,415):
            if value[i,j]<100:
                hit("down")
            return  True
    return  False


if __name__=="__main__":
    time.sleep(3)
    hit("up")
    while True:
        imag=ImageGrab.grab().convert("L")
        value=imag.load()
        iscollide(value)

        # for i in range(250,300):
        #     for j in range(375,420):
        #         value[i,j]=0
        # imag.show()
