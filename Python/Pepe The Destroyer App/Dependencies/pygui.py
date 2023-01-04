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

# create a class that will print out the container
class Window:
    def __init__(self, title, width, height,background):
        self.title = title
        self.width = width
        self.height = height
        self.background = background
    # function to show the window
    def show(self):
        window = tk.Tk()
        window.title(self.title)
        window.configure(background=self.background)
        window.geometry("%sx%s" % (self.width, self.height))
        window.mainloop()


pygui = PyGui()

print("PyGui is ready to use")

# set up the window
window = ct.windll.user32.ShowWindow(ct.windll.kernel32.GetConsoleWindow(), ct.WinDLL("user32.dll").GetSystemMetrics(0))
# get the details of the window
Init_window = window
# print the details of the window
for _g in range(0, 5):
    _g += 1
    rewritten_winvar = window + _g
    print("Rewritten :  %s " % _g)
    pass
if window is not None:
    print("Window is not None!")
    Window('Test', "500", "500", "black").show()
    # print the size of the window 
    print("Window size: %s" % window.size)
else:
    if window is None:
        print("None in window!")


