import pyautogui as pyg
import time


# create a function that will get the position of the mouse
def getMousePosition():
    # get the position of the mouse
    x, y = pyg.position()
    # print the position of the mouse
    print("Mouse Position: ({}, {})".format(x, y))
    return x,y

# create a function that will move the mouse
def moveMouse(x, y):
    # move the mouse to the x and y coordinates
    pyg.moveTo(x, y)
    return 1

# create a function that will click the mouse
def clickMouse():
    # click the mouse
    pyg.click()
    return 1

def main():
    """App main function"""
    # get the position of the mouse
    x = getMousePosition()[0]
    y = getMousePosition()[1]
    # move the mouse to the x and y coordinates

    # get the position of the mouse
    for i in range(0, 10):
        getMousePosition()
        moveMouse(x+i*5, y+i*10)
        time.sleep(1)
   # click the mouse with a hotkey
    clickMouse()
    return str("Mouse Position: ({}, {})".format(x, y))

if __name__ == '__main__':
    main()