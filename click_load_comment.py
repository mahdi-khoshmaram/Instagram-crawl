import pyautogui
from time import sleep
from links import *
from write_click import *

# name for wrting file
name = "zara"

numofloads = 74
numofrows = 1

def load(numofloads):
    for i in range(numofloads):
        pyautogui.moveTo(1239,830)
        pyautogui.scroll(-1000)
        pyautogui.moveTo(1239,830)
        pyautogui.click()
        sleep(3)


def drag():
    pyautogui.moveTo(1400,938)
    pyautogui.mouseDown()
    pyautogui.moveTo(939, 0)
    sleep(2)
    pyautogui.mouseUp()
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
    with pyautogui.hold('alt'):
        pyautogui.press(['tab'])
    # paste comments
    sleep(0.5)
    pyautogui.moveTo(755,630)
    pyautogui.click()

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.hotkey('ctrl', 's')
    write(name)
    with pyautogui.hold('alt'):
        pyautogui.press(['tab'])
    pyautogui.moveTo(1771,319, 1)
    pyautogui.click()
    sleep(0.4)



def main(numofrows, numofloads):
    for i in range(numofrows):
        positions = [(805,251)]
        # positions = [(805,251), (1117, 262), (1428, 252)]
        for position in positions:
            x = position[0]
            y = position[1]
            pyautogui.moveTo(x,y,0.3)
            pyautogui.click()
            sleep(10)
            load(numofloads)
            drag()
        pyautogui.press('esc')
        pyautogui.press('down', presses=8)


sleep(7)
main(numofrows=numofrows, numofloads=numofloads)