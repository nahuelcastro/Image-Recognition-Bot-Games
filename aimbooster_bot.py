from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

######################## GAME URL ################################

# http://www.aimbooster.com

########################  Vars ###################################
region_game = (0,0,0,0) #(678,332,600,420)
color_center = (255, 219, 195)
pixel_step = 5
##################################################################

def locate_region():
    global region_game
    while True:
        loc = pyautogui.locateOnScreen('locator/aimbooster_locator.png', grayscale=True, confidence=0.7)
        if loc:
            # print(loc)
            region_game = loc
            break

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    time.sleep(0.01) #This pauses the script for 0.01 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


# only start the bot if press 's'
def startBotLoop():
    while True:
        if(keyboard.is_pressed('s')): 
            break
        if(keyboard.is_pressed('q')): 
            break

def main():
    global region_game

    startBotLoop()
    locate_region()

    while keyboard.is_pressed('q') == False:
        pic = pyautogui.screenshot(region=region_game)
        width, height = pic.size

        for x in range(0, width, pixel_step):
            for y in range(0, height, pixel_step):
                r, g, b = pic.getpixel((x, y))
                if r == color_center[0] and g == color_center[1] and b == color_center[2]:
                    click(x + region_game[0], y + region_game[1])
                    break


main()
