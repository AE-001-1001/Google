from ctypes import *
from tkinter import simpledialog,messagebox
import os 
import platform
from sys import argv
import sys
from AppTurtle import *
import time
class BackEndButtons:
        def PROCESSOR_IDENTIFIER():
            """Prints a message when the button is clicked"""
            data_to_return = ["PROCESSOR_IDENTIFIER", "PROCESSOR_ARCHITECTURE", "PROCESSOR_LEVEL", "PROCESSOR_REVISION", "NUMBER_OF_PROCESSORS"]
            for i in data_to_return:
                print(i + ": " + os.environ[i])
            return 0
        # create a function that will use ip to get location of ip
        def ip_location():
            """Get the location of an ip address"""
            # automatically get ip address that are running in background
            ip = simpledialog.askstring("IP Address", "Enter IP Address")
            # return all the information about the ip address
            os.system("curl ipinfo.io/{}".format(ip))

        # create a function that will check the internet speed by pinging ookla
        def internet_speed():
            """Check the internet speed"""
            # curl ookla speedtest and get the download and upload speed
            a = os.popen("curl -s https://www.speedtest.net/#").read()
            if a == " ":
                print("Internet Speed: {}".format(a))
            print(a)
            return 1

        def GetTurtle():
            """Get the turtle module"""
            # get the turtle module
            
            return 

        def sort_tasklist():
            """Sort the output of tasklist from smallest to largest"""
            return os.system("tasklist | sort /R")
        
        def AttachToPID():
            """Attach to a process id"""
            id = simpledialog.askstring("PID", "Enter PID")
            inject = messagebox.askyesno("Inject", "Do you want to inject?")

            # get data from the tasklist of given pid
            if inject == True:
                kernal32 = windll.kernel32
                print("Injecting...")
                # get the handle of the process
                hProcess = kernal32.OpenProcess(0x1F0FFF, False, int(id))
                # check if the handle is valid
                if hProcess is not None:
                    
                    # get the address of the loadlibraryA function
                    lpLoadLibraryA = kernal32.GetProcAddress(kernal32.GetModuleHandleA("kernel32.dll"), "LoadLibraryA")
                    # allocate memory for the dll name
                    lpBuffer = kernal32.VirtualAllocEx(hProcess, 0, len(argv[0]), 0x3000, 0x40)
                    # write the dll name to the allocated memory
                    kernal32.WriteProcessMemory(hProcess, lpBuffer, argv[0], len(argv[0]), byref(c_ulong(0)))
                    # create a thread that will run the dll
                    kernal32.CreateRemoteThread(hProcess, None, 0, lpLoadLibraryA, lpBuffer, 0, byref(c_ulong(0)))
                    # type in the console of the process
                    kernal32.WriteProcessMemory(hProcess, 0x7FFD0000, "Hello World", len("Hello World"), byref(c_ulong(0)))
                    # create a remote thread that will write to the console
                    kernal32.CreateRemoteThread(hProcess, None, 0, 0x7FFD0000, 0x7FFD0000, 0, byref(c_ulong(0)))
                    # create a variable that will hold the handle of the process
                    hProcess = kernal32.OpenProcess(0x1F0FFF, False, int(id))
                    print("Injected")
                                       #print the remote thread
                    a = kernal32.CreateRemoteThread(hProcess, None, 0, 0x7FFD0000, 0x7FFD0000, 0, byref(c_ulong(0)))
                    if a:
                        kernel32 = kernal32
                        print(argv[0] + " " + str(a))

                        time.sleep(5)
                        kernel32.CloseHandle(hProcess)
                        # print out the data from handle
                        print("Handle: " + str(hProcess))
                        print("Closed Handle after 5 seconds")
                        return None
                    else:
                        print("Error: " + str(kernal32.GetLastError()))
                        # use hex to print the handle
                        #print(sys.stderr, hex(kernal32.GetLastError))
                    # close the handle
                    kernal32.CloseHandle(hProcess)
                else:
                    print("Failed to inject")
            else:
                print("Not Injecting")
            return 0