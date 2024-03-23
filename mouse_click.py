import mouse
import time
import pyautogui

click_count = 0
while True:
    # mouse.click('left')
    # time.sleep(7)
    x, y = pyautogui.position()
    px = pyautogui.pixel(x, y)
    # print(px)
    if (px[0] < 200) and (px[1] < 200) and (px[2] < 100):
        mouse.click('left')
        click_count += 1
        print(click_count, px[0] < 200, px[1] < 200, px[2] < 100)
    else: 
        print('Wrong color')
    time.sleep(10)
