import keyboard
import pyperclip
import random
import pyautogui as pt
import pyscreenshot as ImageGrab

from time import sleep

pos_f_mes_top = 399
pos_f_mes_left = 553

# Get message
def get_message(x, y):
    pt.tripleClick()
    keyboard.press_and_release('ctrl + c')
    sleep(1)
    whatsapp_message = pyperclip.paste()
    pt.click()
    return whatsapp_message


# Check for new messages
def check_for_green_noti():
    positionGreenNoti = pt.locateOnScreen("whatsapp/green_circle.png", confidence=.8)
    print(positionGreenNoti)
    return positionGreenNoti is not None


def get_white_messages(sender):
    print("get white messages")
    newMesX = 728
    newMesY = 884
    whatsapp_message_list = []
    if sender=="James":
        pt.moveTo(469, 284)
        pt.click()

        print("move to new messages")

        pt.moveTo(newMesX, newMesY,)
    if sender=="Matt":
        pt.moveTo(469, 284)
        pt.click()

        print("move to new messages")

        pt.moveTo(newMesX, newMesY,)

    isWhite = pt.pixelMatchesColor(newMesX, newMesY, (255, 255, 255), tolerance=10)

    while isWhite:
        isWhite = pt.pixelMatchesColor(newMesX, newMesY, (255, 255, 255), tolerance=10)
        if isWhite:
            whatsapp_message_list.insert(0, get_message(newMesX, newMesY))
        newMesY = newMesY - 44
        pt.moveTo(newMesX, newMesY)

    whatsapp_message = ""
    for i in range(len(whatsapp_message_list)):
        whatsapp_message += whatsapp_message_list[i] + "\n"

    print(whatsapp_message)
    return whatsapp_message


def get_sender():
    im = ImageGrab.grab(bbox=(95, 365, 175, 440))
    mattPicPos = pt.locateOnScreen("whatsapp/matt.png", confidence=.9)
    jamesPicPos = pt.locateOnScreen("whatsapp/james.png", confidence=.9)

    if mattPicPos is not None and 300 >= mattPicPos[1] >= 200:
        print("Sender: Matt")
        return "Matt"
    if jamesPicPos is not None and 380 >= jamesPicPos[1] >= 200:
        print("Sender: James")
        return "James"
    return "Others"

def get_position():
    while True:
        posXY = pt.position()
        sleep(3)
        print(posXY)
        if posXY[0] == 0:
            break

def main():
    while True:
        if(check_for_green_noti()):
            sender = get_sender()
            print("New messages from " + get_sender() +": ")

            # get the new messages
            whatsapp_message = get_white_messages(sender)

            # send to the other
            if(">>" not in whatsapp_message and sender == "James"):
                matPos = pt.locateOnScreen("whatsapp/matt.png", confidence=.9)
                pt.moveTo(matPos)
                # click profile
                pt.click()
                # click textbox
                pt.moveTo(767,960)
                pt.click()
                sleep(1)
                pt.write(whatsapp_message)
                sleep(1)
                keyboard.press("enter")
                pt.moveTo(337, 640)
            if (">>" not in whatsapp_message and sender == "Matt"):
                jamesPos = pt.locateOnScreen("whatsapp/james.png", confidence=.8)
                pt.moveTo(jamesPos)
                # click profile
                pt.click()
                # click textbox
                pt.moveTo(767, 960)
                pt.click()
                sleep(1)
                pt.write(whatsapp_message)
                sleep(1)
                keyboard.press("enter")
            pt.moveTo(337, 640)
            pt.click()
        else:
            currentPos = pt.position()
            if currentPos[0]==0 or currentPos[1]==0:
                break
            print("No new messages!")
            pt.moveTo(337, 640)
            pt.click()

# check_for_green_noti()
# check_for_white_messages()
# get_position()
main()