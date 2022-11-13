import ctypes
from tkinter import simpledialog,messagebox
import os 
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
                print("Handle: {}".format(handle))
                if not handle:
                    print("[!] Couldn't get handle to PID: {}".format(id))
                    print("[!] Are you sure you have permission to attach?")
                    return False
            if inject == False:
                print("Not Attaching")
