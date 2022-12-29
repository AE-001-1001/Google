import pyautogui, time as t,ctypes as ct,tkinter as tk, time as t, threading as th, ctypes as ct, os, sys, subprocess as sp

# create a class that will hold all the functions
class PyGui:
    def __init__(self):
        pass

    # function to move the mouse to a specific location
    def move_mouse(self, x, y):
        pyautogui.moveTo(x, y)

    # function to click the mouse
    def click_mouse(self):
        pyautogui.click()

    # function to type a string
    def type_string(self, string):
        pyautogui.typewrite(string)

    # function to press a key
    def press_key(self, key):
        pyautogui.press(key)

    # function to press a key and hold it
    def press_key_hold(self, key):
        pyautogui.keyDown(key)

    # function to release a key
    def release_key(self, key):
        pyautogui.keyUp(key)

    # function to press a key combination
    def press_key_combo(self, key1, key2):
        pyautogui.hotkey(key1, key2)

    # function to press a key combination and hold it
    def press_key_combo_hold(self, key1, key2):
        pyautogui.hotkey(key1, key2)

    # function to release a key combination
    def release_key_combo(self, key1, key2):
        pyautogui.hotkey(key1, key2)

    # function to press a key combination
    def press_key_combo(self, key1, key2):
        pyautogui.hotkey(key1, key2)

    # function to press a key combination and hold it
    def press_key_combo_hold(self, key1, key2):
        pyautogui.hotkey(key1, key2)

    # function to release a key combination
    def release_key_combo(self, key1, key2):
        pyautogui.hotkey(key1, key2)

class Window(object):
    def __init__(data):
        data = pygui
        pass 
    def __str__(data):
        return "Window"
# create a instance of the class
pygui = PyGui()

print("PyGui is ready to use")

# set up the window
window = ct.windll.user32.ShowWindow(ct.windll.kernel32.GetConsoleWindow(), ct.WinDLL("user32.dll").GetSystemMetrics(0))
# get the details of the window
for i in range(0, 5):
    i += 1
    rewritten = window + i
    print(rewritten)
    pass
if window is not None:
    print("Window is not None!")
else:
    if window is None:
        print("None in window!")


