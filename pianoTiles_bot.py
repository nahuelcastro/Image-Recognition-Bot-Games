from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import numpy as np
######################## GAME URL ################################

# https://www.agame.com/game/magic-piano-tiles

##################### Set Tiles Positions ########################
Tiles_y = 330
Tile_x1 = 620
Tile_x2 = 705
Tile_x3 = 790
Tile_x4 = 875
##################################################################

def set_tiles_positions(region):
    global Tiles_y, Tile_x1, Tile_x2, Tile_x3, Tile_x4
    start_x, start_y = region[0], region[1]
    width, height = region[2], region[3]
    step_column_tile = width / 4
    offset_column_tile = step_column_tile / 2

    Tiles_y = int(start_y + height // 3 + 20)
    Tile_x1 = int(start_x + offset_column_tile)
    Tile_x2 = int(Tile_x1 + step_column_tile)
    Tile_x3 = int(Tile_x2 + step_column_tile)
    Tile_x4 = int(Tile_x3 + step_column_tile)

def locate_region():
    while True:
        loc = pyautogui.locateOnScreen('locator/piano_tiles_locator.png', grayscale=True, confidence=0.6)
        if loc != None:
            set_tiles_positions(loc)
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

    startBotLoop()
    locate_region()

    while keyboard.is_pressed('q') == False:

        if pyautogui.pixel(Tile_x1, Tiles_y)[0] == 0:
            click(Tile_x1, Tiles_y)
        if pyautogui.pixel(Tile_x2, Tiles_y)[0] == 0:
            click(Tile_x2, Tiles_y)
        if pyautogui.pixel(Tile_x3, Tiles_y)[0] == 0:
            click(Tile_x3, Tiles_y)
        if pyautogui.pixel(Tile_x4, Tiles_y)[0] == 0:
            click(Tile_x4, Tiles_y)
    

main()

