import pyautogui as pt

from time import sleep

while True:
    posXY = pt.position()
    sleep(1)
    if posXY[0] == 0:
        break