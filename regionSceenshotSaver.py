#This script saves the image of the region "
import pyautogui

# im1 = pyautogui.screenshot(region=(670,350,600,400))
im1 = pyautogui.screenshot(region=(678,332,600,420))
im1.save(r"./savedimage.png")