from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

######################## GAME URL ################################

# https://www.agame.com/game/magic-piano-tiles

##################### Set Tiles Positions ########################
Tiles_y = 330
Tile_x1 = 620
Tile_x2 = 705
Tile_x3 = 790
Tile_x4 = 875
##################################################################


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

    startBotLoop()

    while keyboard.is_pressed('q') == False:
        # pyautogui.pixel(x,y)[0] indicates the value R of the RGB pixel, the [1] is G and [2] is B
        if pyautogui.pixel(Tile_x1, Tiles_y)[0] == 0:
            click(Tile_x1, Tiles_y)
        if pyautogui.pixel(Tile_x2, Tiles_y)[0] == 0:
            click(Tile_x2, Tiles_y)
        if pyautogui.pixel(Tile_x3, Tiles_y)[0] == 0:
            click(Tile_x3, Tiles_y)
        if pyautogui.pixel(Tile_x4, Tiles_y)[0] == 0:
            click(Tile_x4, Tiles_y)
    

main()

