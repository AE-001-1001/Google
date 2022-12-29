import sys
import os
import socket
import struct
import threading
import time
import queue
import re
import ipaddress
import subprocess
import platform
import ctypes
import winreg
import scapy.all as scapy
from binascii import hexlify

def local_checker(): 

    # Check if the script is running on a Windows machine
    if platform.system() != "Windows":
        print("This script is only for Windows machines.")
        sys.exit(1)
    if platform.system() == "Windows":
        # Check if the script is running as administrator
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("Please run this script as administrator.")
            sys.exit(1)
    if platform.system() == "Windows":
        # Check if the script is running on a 64-bit machine
        if platform.machine() != "AMD64":
            print("This script is only for 64-bit machines.")
            sys.exit(1)
    # check if platform is windows 10 and is running it as admin
    if platform.system() == "Windows":
        if ctypes.windll.shell32.IsUserAnAdmin():
            if platform.release() == "10":
                print("Running as admin on Windows 10")
            else:
                print("Running as admin on Windows 7 or 8")
        else:
            print("Not running as admin")
    return platform.system() , platform.machine() , platform.release() , ctypes.windll.shell32.IsUserAnAdmin() , 0

# if local checker comes back with 0 then continue
def continuer():
    if local_checker()[4] == 0:
        print("Continuing")

        # get the data from the local_checker function
        system = local_checker()[0]
        machine = local_checker()[1]
        release = local_checker()[2]
        admin = local_checker()[3]

        # use re to get the ip address
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(subprocess.check_output("ipconfig")))
        ip = ip[0]

        # use re to get the subnet mask
        mask = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(subprocess.check_output("ipconfig")))
        mask = mask[1]

        # use re to get the default gateway
        gateway = re.findall(r'[0-9]+(?:\.[0-9]+){3}', str(subprocess.check_output("ipconfig")))
        gateway = gateway[2]

        # use struct to convert the ip address to binary
        ip2 = struct.unpack("!L", socket.inet_aton(ip))[0]
        # convert the ip address to binary
        ip2 = bin(ip2)
        # create a dictionary to store the data
        # use winreg to get all the data from the registry
        # assign them as keys and values
        dataVal = {"1":winreg.HKEY_CLASSES_ROOT, "2":winreg.HKEY_CURRENT_USER, "3":winreg.HKEY_LOCAL_MACHINE,
                   "4":winreg.HKEY_USERS, "5":winreg.HKEY_CURRENT_CONFIG, "6":winreg.HKEY_DYN_DATA}
        # loop through the dictionary
        for k,v in dataVal.items():
            # open the registry use dataVal
            reg = winreg.ConnectRegistry(None, v)
            # open the registry key
            key = winreg.OpenKey(reg, "SOFTWARE", 0, winreg.KEY_READ)
            # get the number of subkeys
            numSubKeys = winreg.QueryInfoKey(key)[0]
            # get the name of the subkeys
            subKeys = [winreg.EnumKey(key, i) for i in range(numSubKeys)]
            print("Subkeys of SOFTWARE: ", subKeys)
            # print the contents of the subkeys
            pass
            for i in range(numSubKeys):
                subKey = winreg.OpenKey(key, subKeys[i])
                print("Subkey: ", subKeys[i])
                numValues = winreg.QueryInfoKey(subKey)[1]
                for j in range(numValues):
                    print("Value: ", winreg.EnumValue(subKey, j))
                    # check if there are any vulnerabilities
                    # if there are any vulnerabilities then print them
                    # if there are no vulnerabilities then print that there are no vulnerabilities
                    # using re,struct,binascii,ipaddress,scapy
            pass
            data = {"System": system, "Machine": machine, "Release Ver": release, "Admin": admin, "IP": ip, "Mask": mask, "Gateway": gateway, "IP in struct": ip2}
            print("Contents of data[!]")
            for k,v in data.items():
                print("%s: %s" % (k, v))
    else:
        print("Exiting")
        sys.exit(1)
    return ip, mask, gateway

os.system("cls")
continuer()