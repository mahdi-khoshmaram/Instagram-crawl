import pyautogui
from time import sleep
from links import *
from write_drag import *


scroll_time = 80
name = "victoria"

links = links(name)
crawled = {}
sleep(10)

id = 1
crawled_before = 408
for _,url in links.items():
    skip = list(range(crawled_before))
    if id in skip:
        crawled[url] = 1
    else:
        crawled[url] = 0
    id += 1

number = 0
for date, url in links.items():
    if crawled[url] == 1:
        continue
    # move to search bar
    pyautogui.moveTo(753, 63)
    # click on search bar
    pyautogui.click()
    # enter the url
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(url)
    # press enter to go to the site
    pyautogui.press('enter')
    sleep(8)
#---------------------------------------------------------------- 
    pyautogui.moveTo(1413, 204)
    pyautogui.mouseDown()
    pyautogui.moveTo(1408, 684,0.5)

    sleep(scroll_time)
    pyautogui.mouseUp()
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'c')
# ----------------------------------------------------------------
    # goes to notepad
    with pyautogui.hold('alt'):
        pyautogui.press(['tab'])
    # paste comments
    sleep(1)
    pyautogui.click()

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.5)
    pyautogui.hotkey('ctrl', 's')

    write(date)
    # back to chrome
    with pyautogui.hold('alt'):
        pyautogui.press(['tab'])

    crawled[url] = 1
    print(f"{number + 1} crawled! ")
    number += 1


print(crawled)