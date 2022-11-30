# imports
import os

import sqlite3

from time import strftime
from tkinter import *
from tkinter import Menu, Menubutton
from backEndButton import *
from AppReq import *
import Webserver 
import win32dll

class App:
    
    def new_window(name):
        """Create a new window"""
        root = Tk()
        root.geometry('455x345')
        os.system('title ' + name)
        for i in range(10):
            root.update()
            break
        root.title(name)

        def update_total_memory():
            """Update the total physical memory"""
            # get the total free physical memory
            total_memory = os.popen("wmic OS get FreePhysicalMemory /Value").read()
            # print the total physical memory
            os.system('cls')
            print("Total Physical Memory: {}".format(total_memory))
            # update the total physical memory every 1000 milliseconds
            root.after(1000, update_total_memory)
            return 0
        
        # create a function that will count when New Window is activated

        def update_time_in_titletk():
            """Update the time in the title"""
            current_time = strftime("%H:%M:%S")
            root.title("Current Time: {}".format(current_time))
            # update the time in the title every 1000 milliseconds
            root.after(1000, update_time_in_titletk)
            # create a clock in the window
            return 0
        
        def update_total_virtual_memory():
            """Update the total virtual memory"""
            # get the total free virtual memory
            total_virtual_memory = os.popen("wmic OS get FreeVirtualMemory /Value").read()
            # print the total virtual memory
            os.system('cls')
            print("Total Virtual Memory: {}".format(total_virtual_memory))
            # update the total virtual memory every 1000 milliseconds
            root.after(1000, update_total_virtual_memory)
            return 0
        #create a function that will get ip of given website
        def get_ip():
            """gets the ip of a website"""
            website = simpledialog.askstring("Input", "Enter a website", parent=root)
            # get the ip of the website
            ip = os.popen("curl -4 {}".format(website)).read()
            print(ip)
            return 0
        # create a function that uses sqlite3 to create a database
        def create_database():
            """Create a database"""
            # create a database
            conn = sqlite3.connect('test.db')
            # create a cursor
            c = conn.cursor()
            # put names in the table
            c.execute("INSERT INTO stocks VALUES ('2006-01-05')")
            # commit the changes
            conn.commit()
            # close the connection
            conn.close()
            return conn

        def syn_ack():
            """Send a syn_ack packet"""
            # get the ip address
            ip = simpledialog.askstring("IP Address", "Enter IP Address")
            # send a syn_ack packet 
            os.system("ping -a {}".format(ip))
            return 0

        def ScanOpenPorts():
            a = os.popen("netstat -ano").read()
            with open("PID.csv", "w") as f:
                f.writelines(a)
            return 0

        def get_mac():
            import socket
            import uuid
            mac = None
            try:
                hostname = socket.gethostname()
                IPAddr = socket.gethostbyname(hostname)
                mac = uuid.getnode()
                mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
            except:
                pass
            print("Hostname: {}".format(hostname))
            print("IP Address: {}".format(IPAddr))
            print("MAC Address: {}".format(mac))
            return 0

        def get_network_info():
            """Get the network info"""
            # get the network info
            network_info = os.popen("ipconfig").read()
            # print the network info
            print(network_info)
            # get all the mac addresses for the network adapters
            mac_addresses = os.popen("arp -a").read()
            print(mac_addresses)
            return 0

        
        btn1 = Button(root, text="PROCESSOR", command=BackEndButtons.PROCESSOR_IDENTIFIER)
        btn2 = Button(root, text="IP Address", command=lambda: (os.system("curl ipinfo.io/ip")))
        btn3 = Button(root, text="IP Location", command=BackEndButtons.ip_location)
        btn4 = Button(root, text="Internet Speed", command=BackEndButtons.internet_speed)
        btn5 = Button(root, text="Send SYN_ACK", command=syn_ack)
        btn6 = Button(root, text="All Running Processes", command=BackEndButtons.sort_tasklist)
        btn7 = Button(root, text="Attach to PID", command=BackEndButtons.AttachToPID)
        btn8 = Button(root, text="Clear Console", command=lambda: os.system('cls'))
        btn9 = Button(root, text="Exit", command=root.destroy)
        
        # another array of buttons
        Scan = Button(root, text="Scan Open Ports", command=ScanOpenPorts)
        Get_IP = Button(root, text="Get IP", command=get_ip)
        Request = Button(root, text="Request Website", command=CustomRequester.get)
        Post = Button(root, text="Post Website", command=CustomRequester.Post)
        OpenServer = Button(root, text="Open Web Server", command=Webserver.main)
        Get_MAC = Button(root, text="Get MAC Address", command=get_mac)
        Get_Network_Info = Button(root, text="Get Network Info", command=get_network_info)
        Kernal32 = Button(root,text="Kernal32", command=lambda: win32dll.main())
        Create_Database = Button(root, text="Create Database", command=create_database)

        buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9 ]
        another_buttons = [Scan, Get_IP, Request, OpenServer, Get_MAC, Get_Network_Info, Post, Kernal32, Create_Database]



        for i in range(len(buttons)):
            # align the buttons to the left to match the size of the window
            a = (buttons[i].pack(side='top', fill=Y, ipadx=4, ipady=4, after=print("Button {} Initialized".format(buttons[i]))))
            b = (buttons[i].config(font=("Courier", 9), background="black", foreground="white", activebackground="black", activeforeground="white"))
            root.after(125, a)
            root.after(75, b)

        for xyz in another_buttons:
            xyz.config(bg="black", fg="white")
            
        for ZYX in range(len(another_buttons)):
            another_buttons[ZYX].place(x=0, y=(ZYX * 30))
            # print the button has been placed along with the name of the button
            print("Placed {}".format(another_buttons[ZYX]))

        #Menu bar at the top of window

        menu = Menu(root)
        
        menu.add_checkbutton(label='Time', command=update_time_in_titletk)
        menu.add_checkbutton(label='Date', command=lambda: print(strftime("%d/%m/%Y/%H:%M:%S/%a")))
        menu.add_checkbutton(label="GPU Information", command=lambda: os.system("nvidia-smi "))
        menu.add_checkbutton(label='CPU Usage', command=lambda: os.system("wmic cpu get loadpercentage /value"))
        menu.add_checkbutton(label='Memory Usage', command=update_total_memory)
        menu.add_checkbutton(label='Virtual Memory Usage', command=update_total_virtual_memory)
        menu.add_checkbutton(label='Deploy IP Addresses Reader', command=lambda: os.system("netstat | findstr /R /C:\"[0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]*\""))
        menu.add_checkbutton(label='Turtle Drawing', command=Turtle.rhombicosidodecahedron)

        menu.config(font=("Courier", 9), background="black", foreground="white", relief="raised", border=3)
        root.config(menu=menu, background="black", bd=5, relief="sunken", border=3)
        
        root.mainloop()
