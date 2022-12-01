# path
# !/usr/bin/env python

import os
import re
from ctypes import *
import ctypes.util as Cutil
import sys
import time
import msvcrt 
import random as r
import subprocess
kernal32 = windll.kernel32
user32 = windll.user32
hStdOut = kernal32.GetStdHandle(-11)

# create a function using 
class COORD(Structure):
    """struct in wincon.h."""
    pass
COORD._fields_ = [("X", c_short), ("Y", c_short)]

class SMALL_RECT(Structure):
    """struct in wincon.h."""
    pass
SMALL_RECT._fields_ = [("Left", c_short), ("Top", c_short),
                       ("Right", c_short), ("Bottom", c_short)]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    """struct in wincon.h.""" 
    pass
CONSOLE_SCREEN_BUFFER_INFO._fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", c_short),
                                       ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]


class CONSOLE_CURSOR_INFO(Structure):
    """struct in wincon.h."""
    pass
CONSOLE_CURSOR_INFO._fields_ = [("dwSize", c_int), ("bVisible", c_byte)]

class CONSOLE_FONT_INFO(Structure):
    """CONSOLE_FONT_INFO Structure (consoleapi.h)"""
    pass
CONSOLE_FONT_INFO._fields_ = [("nFont", c_int), ("dwFontSize", COORD)]

class CONSOLE_SCREEN_BUFFER_INFOEX(Structure):
    """Console Screen Buffer InfoEx"""
    pass
CONSOLE_SCREEN_BUFFER_INFOEX._fields_ = [("cbSize", c_ulong), ("dwSize", COORD), ("dwCursorPosition", COORD),
                                         ("wAttributes", c_ushort), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD),
                                         ("wPopupAttributes", c_ushort), ("bFullscreenSupported", c_bool), ("ColorTable", c_ulong * 16)]


class CONSOLE_FONT_INFOEX(Structure):
    """CONSOLE_FONT_INFOEX structure (ConsoleFontInfoEx in MSDN)"""
    pass
CONSOLE_FONT_INFOEX._fields_ = [("cbSize", c_ulong), ("nFont", c_ulong), ("dwFontSize", COORD),
                                ("FontFamily", c_uint), ("FontWeight", c_uint), ("FaceName", c_wchar * 32)]

class CHAR_INFO(Structure):
    """struct in wincon.h"""
    pass
CHAR_INFO._fields_ = [("Char", c_wchar), ("Attributes", c_ushort)]

# create a handle to the console

class CONSOLE_SELECTION_INFO(Structure):
    """struct in wincon.h."""
    pass
CONSOLE_SELECTION_INFO._fields_ = [("dwFlags", c_ulong), ("dwSelectionAnchor", COORD), ("srSelection", SMALL_RECT)]

# use kernal32 to create a handle to the console

kernal32.GetConsoleScreenBufferInfo.argtypes = [c_void_p, POINTER(CONSOLE_SCREEN_BUFFER_INFO)]
kernal32.GetConsoleScreenBufferInfo.restype = c_bool

# create a function using Cutil
def CtypesUtil(dllname):
    """CtypesUtil function"""
    Cutil.find_library(dllname)
    if Cutil.find_library(dllname) is Exception:
        print("{} not found".format(dllname))
        return 1
    else:
        print("{} found".format(dllname))
    return 0
    


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
    if kernal32.GetConsoleWindow() == 0:
        kernal32.SetConsoleTextAttribute(hStdOut, 0x0004)
        print("[!]")
    # reset the color of the console
        kernal32.SetConsoleTextAttribute(hStdOut, 0x0007)
        print("AttachConsole failed")
        return kernal32.FreeConsole()
    else:
        # kernal32.SetConsoleTextAttribute(hStdOut, 0x0009) sets it to blue
        kernal32.SetConsoleTextAttribute(hStdOut, 0x0009)
        print("AttachConsole succeeded")
        # resets the color of the console before the rest of the program runs
        kernal32.SetConsoleTextAttribute(hStdOut, 0x0007)
        print("Console window handle: 0x%08x" % kernal32.GetConsoleWindow())
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
            sys.stdout.write(buffer[y * csbi.dwSize.X + x].Char)
        sys.stdout.write(' ' * (csbi.dwSize.X - x))
    return x, y

# create a function that sets the console cursor position to the middle of the console
def set_console_cursor_pos(x, y):
    """Set the console cursor position to the middle of the console"""
    kernal32.SetConsoleCursorPosition.argtypes = [c_void_p, COORD]
    kernal32.SetConsoleCursorPosition.restype = c_bool
    var = COORD(x, y)
    kernal32.SetConsoleCursorPosition(hStdOut, var)
    return set_console_cursor_pos(var.X, var.Y)

# create a function that will use re to find all ip addresses running backdoor
def find_ip():
    """find_ip function"""
    a = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(subprocess.check_output("netstat -ano", shell=True)))
    for i in a:
        if i == " ":
            print("No IP addresses found")
            continue
        else:
            print(i)
    return a



# create a function that will make a animation in the console of a duck
def Symbol():
    dictionary = {1:'\u256D', 2:'\u256E', 3:'\u2570', 4:'\u256F', 5:'\u256B'}

    while True:
        for i in range(1, 6):
            print(dictionary[i], end='\r')
        for i in range(0, 20):
            print(dictionary[r.randint(1, 5)])
        for x in range(0,10):
            print("*" * x + "-" * (10-i) + "*" * i , end='\r')
        return None


# use the dump_console_screen_buffer function to dump the console screen buffer into a file
def dump_console_screen_buffer_to_file(filename):
    """dump_console_screen_buffer_to_file function"""
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
                # write it to the file
                f.write(buffer[y * csbi.dwSize.X + x].Char)
                msvcrt.heapmin()
    return x, y

def _prerunner_():
    """_prerunner_ function"""
        # use the dump_console_screen_buffer_to_file function to dump the console screen buffer into a file
    dump_console_screen_buffer_to_file('console.txt')
    # use the dump console screen buffer function
    os.system("cls")
    csbi = dump_console_screen_buffer()
    # print out Console Screen Buffer Info centered to the console cursor position
    # make the ! colored blue
    # using kernal32
    kernal32.SetConsoleTextAttribute.argtypes = [c_void_p, c_ushort]
    print(c_bool(kernal32.SetConsoleTextAttribute(hStdOut, 0x0005))._objects)
    kernal32.SetConsoleTextAttribute.restype = c_bool
    kernal32.SetConsoleTextAttribute(hStdOut, 0x0002)
    
    a = ("Console Screen Buffer Info: %s" % str(csbi))
    print("[!]".center(85, "="))
    # reset the color of the console
    kernal32.SetConsoleTextAttribute(hStdOut, 0x0007)
    print(a.center(95, " "))

    print("PID = %d" % get_console_pid())
    # print if the console is attached using attach function
    print("Attached = %s" % attach(get_console_pid()))
    print("Console size: %s" % str(get_console_size()))
    print("Console cursor position: %s" % str(get_console_cursor_pos()))
    # print success in blue color
    print("Sucessfully printed console size and cursor position using\nkernel32.dll[GetConsoleScreenBufferInfo{!s}]".format(get_console_info()))
    print(time.process_time())
    Symbol()
    return csbi
# use main function and then print out the console size and cursor position
def main():
    _prerunner_()
    CtypesUtil("kernel32.dll")
    find_ip()
    return 0
