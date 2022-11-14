from ctypes import *
from tkinter import simpledialog,messagebox
import os 
import sys
from colorama import Fore, Back, Style
from AppTurtle import *

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

        # create a function that will check the internet speed by pinging ookla
        def internet_speed():
            """Check the internet speed"""
            # curl ookla speedtest and get the download and upload speed
            a = os.popen("curl -s https://www.speedtest.net/#").read()
            if a == "guid":
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
                pid = int(id)
                h_process = kernal32.OpenProcess(0x1F0FFF, False, pid)
                for h in h_process:
                    print(h)
                print(h_process, pid)
                if not h_process:
                    print("[*] Couldn't acquire a handle to PID: %s" % pid)
                    print("[*] Are you sure you have permission to inject into this process?")
                    print("[*] Exiting.")
                    sys.exit(0)
                
            return 1