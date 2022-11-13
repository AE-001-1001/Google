import ctypes
from tkinter import simpledialog,messagebox
import os 
from colorama import Fore, Back, Style


class BackEndButtons:
        def PROCESSOR_IDENTIFIER():
            """Prints a message when the button is clicked"""
            print("{}".format(os.getenv("PROCESSOR_IDENTIFIER")))

        # create a function that will use ip to get location of ip
        def ip_location():
            """Get the location of an ip address"""
            # automatically get ip address that are running in background
            ip = simpledialog.askstring("IP Address", "Enter IP Address")
            # return all the information about the ip address
            os.system("curl ipinfo.io/{}".format(ip))

        def sort_tasklist():
            """Sort the output of tasklist from smallest to largest"""
            return os.system("tasklist | sort /R")
        
        def AttachToPID():
            """Attach to a process id"""
            id = simpledialog.askstring("PID", "Enter PID")
            inject = messagebox.askyesno("Inject", "Do you want to inject?")

            # get data from the tasklist of given pid
            if inject == True:
                print("Attaching to PID: {}".format(id))
                kernel32 = ctypes.windll.kernel32
                handle = kernel32.OpenProcess(0x1F0FFF, False, int(id))
                # allocate memory
                arg_address = kernel32.VirtualAllocEx(handle, 0, 0x1000, 0x3000, 0x40)
                # write process memory to google chrome
                b = kernel32.CreateRemoteThread(handle, None, 0, arg_address, None, 0, None)
                print("\n",b)
                return b
            
            if inject == False:
                print("Not Attaching")
            
            return 1