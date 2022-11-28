# path
# !/usr/bin/env python

import os
from ctypes import *
import sys
import time

# define windll

kernal32 = windll.kernel32

# use kernal32 to create a handle to the console

hStdOut = kernal32.GetStdHandle(-11)

# create a handle to the console

class COORD(Structure):
    pass
COORD._fields_ = [("X", c_short), ("Y", c_short), ("Z", c_short)]

# create a handle to the console

class SMALL_RECT(Structure):
    pass
SMALL_RECT._fields_ = [("Left", c_short), ("Top", c_short), ("Right", c_short), ("Bottom", c_short)]

# create a handle to the console

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    pass
CONSOLE_SCREEN_BUFFER_INFO._fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", c_short), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]

# create a handle to the console

class CONSOLE_CURSOR_INFO(Structure):
    pass
CONSOLE_CURSOR_INFO._fields_ = [("dwSize", c_int), ("bVisible", c_byte)]

# create a handle to the console

class CONSOLE_FONT_INFO(Structure):
    pass
CONSOLE_FONT_INFO._fields_ = [("nFont", c_int), ("dwFontSize", COORD)]

# create a handle to the console
class CONSOLE_SCREEN_BUFFER_INFOEX(Structure):
    pass
CONSOLE_SCREEN_BUFFER_INFOEX._fields_ = [("cbSize", c_ulong), ("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", c_ushort), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD), ("wPopupAttributes", c_ushort), ("bFullscreenSupported", c_bool), ("ColorTable", c_ulong * 16)]

# create a handle to the console

class CONSOLE_FONT_INFOEX(Structure):
    pass
CONSOLE_FONT_INFOEX._fields_ = [("cbSize", c_ulong), ("nFont", c_ulong), ("dwFontSize", COORD), ("FontFamily", c_uint), ("FontWeight", c_uint), ("FaceName", c_wchar * 32)]

# create a handle to the console



class CHAR_INFO(Structure):
    pass
CHAR_INFO._fields_ = [("Char", c_wchar), ("Attributes", c_ushort)]

# create a handle to the console

class CONSOLE_SELECTION_INFO(Structure):
    _fields_ = [("dwFlags", c_ulong), ("dwSelectionAnchor", COORD), ("srSelection", SMALL_RECT)]

# use kernal32 to create a handle to the console

kernal32.GetConsoleScreenBufferInfo.argtypes = [c_void_p, POINTER(CONSOLE_SCREEN_BUFFER_INFO)]
kernal32.GetConsoleScreenBufferInfo.restype = c_bool

# create a function that checks all the attributes of the console
def get_console_info():
    csbi = CONSOLE_SCREEN_BUFFER_INFO()
    kernal32.GetConsoleScreenBufferInfo(hStdOut, byref(csbi))
    return csbi

# create a function that checks the size of the console
def get_console_size():
    csbi = get_console_info()
    return csbi.dwSize.X, csbi.dwSize.Y, csbi.dwMaximumWindowSize.X, csbi.dwMaximumWindowSize.Y

# create a function that checks the cursor position of the console

def get_console_cursor_pos():
    csbi = get_console_info()
    return csbi.dwCursorPosition.X, csbi.dwCursorPosition.Y

# create a function that gets the current PID of the console
def get_console_pid():
    pid = os.getpid()
    kernal32.GetConsoleProcessList.argtypes = [POINTER(c_ulong), c_ulong]
    kernal32.GetConsoleProcessList.restype = c_ulong
    n = kernal32.GetConsoleProcessList(byref(c_ulong(pid)), 1)
    if n == 0:
        return None
    else:
        print("n = %d" % n)
        return pid


# create a attach function that uses the get_console_pid function to attach to the console
def attach(pid):
    kernal32.AttachConsole(pid)
    return kernal32.GetConsoleWindow() != 0

# create a function that dumps the console screen buffer
def dump_console_screen_buffer():
    # create a handle to the console
    csbi = get_console_info()
    # create a handle to the console
    buffer = (CHAR_INFO * (csbi.dwSize.X * csbi.dwSize.Y))()
    # create a handle to the console
    kernal32.ReadConsoleOutputW.argtypes = [c_void_p, POINTER(CHAR_INFO), COORD, COORD, POINTER(SMALL_RECT)]
    # create a handle to the console
    kernal32.ReadConsoleOutputW.restype = c_bool
    # create a handle to the console
    kernal32.ReadConsoleOutputW(hStdOut, buffer, csbi.dwSize, COORD(0, 0), byref(csbi.srWindow))
    # create a handle to the console
    for y in range(csbi.dwSize.Y):
        s = 0
        y += csbi.srWindow.Top - s
        for x in range(csbi.dwSize.X):
            sys.stdout.write(buffer[y * csbi.dwSize.Z + x].Char)
        sys.stdout.write(' ' * (csbi.dwSize.X - x))
    return x, y

# create a function that sets the console cursor position to the middle of the console
def set_console_cursor_pos(x, y):
    kernal32.SetConsoleCursorPosition.argtypes = [c_void_p, COORD]
    kernal32.SetConsoleCursorPosition.restype = c_bool
    kernal32.SetConsoleCursorPosition(hStdOut, COORD(x, y))
    return get_console_cursor_pos()

# use the dump_console_screen_buffer function to dump the console screen buffer into a file
def dump_console_screen_buffer_to_file(filename):
    # create a handle to the console
    csbi = get_console_info()
    # create a handle to the console
    buffer = (CHAR_INFO * (csbi.dwSize.X * csbi.dwSize.Y))()
    # create a handle to the console
    kernal32.ReadConsoleOutputW.argtypes = [c_void_p, POINTER(CHAR_INFO), COORD, COORD, POINTER(SMALL_RECT)]
    # create a handle to the console
    kernal32.ReadConsoleOutputW.restype = c_bool
    # create a handle to the console
    kernal32.ReadConsoleOutputW(hStdOut, buffer, csbi.dwSize, COORD(0, 0), byref(csbi.srWindow))
    # write to file nicely
    with open(filename, 'w') as f:
        for y in range(csbi.dwSize.Y):
            for x in range(csbi.dwSize.X):
                f.write(buffer[y * csbi.dwSize.X - x].Char)
            
    return x, y

# use main function and then print out the console size and cursor position
def main():
    # use the dump_console_screen_buffer_to_file function to dump the console screen buffer into a file
    dump_console_screen_buffer_to_file('console.txt')
    # use the dump console screen buffer function
    os.system("cls")
    csbi = dump_console_screen_buffer()
    # print out Console Screen Buffer Info centered to the console cursor position
    print("\t\t\t\tConsole Screen Buffer Info: %s" % str(csbi))
    print("PID = %d" % get_console_pid())
    # print if the console is attached using attach function
    print("Attached = %s" % attach(get_console_pid()))
    print("Console size: %s" % str(get_console_size()))
    print("Console cursor position: %s" % str(get_console_cursor_pos()))
    # print success in blue color
    print("Sucessfully printed console size and cursor position using\nkernel32.dll[GetConsoleScreenBufferInfo{!s}]".format(get_console_info()))
    print(time.process_time())
    return 0

if __name__ == "__main__":
    sys.exit(main())