# Description: Sorts the data from the registry and the data from the program
import re, subprocess, platform, os, ctypes,time as t,numpy as np, binascii as ba, pandas as pd, sys
from ctypes import *

interface_list = (c_byte * 128)()
interface_amount = c_int()
# use windll to load the dll
win32 = ctypes.windll.kernel32

# use the dll to get the PID of the process
pid = win32.GetCurrentProcessId()

path = os.getcwd().replace("\\", "/")
# create a class that will store the data with key value pairs
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
# create a class that will use re
class Re:
    def __init__(self, regex, string):
        self.regex = regex
        self.string = string
    def search(self):
        return re.search(self.regex, self.string)

# use Data to create a framework for the data
class Framework:
    def __init__(self, data):
        self.data = data
    def __iter__(data):
        return iter(data.data)

# use Data to create a list of data
init_data = [Data("PID:", pid), Data("Time:", t.strftime("%Y:%H:%M:%S:%p")), Data("Path:", os.getcwd().replace("\\", "/"))]

# use Data to create a list of data from the registry
registry_data = [
                 Data("HWID:", re.search(r"([A-Z0-9]{5}-){4}[A-Z0-9]{5}", str(subprocess.check_output("wmic path softwarelicensingservice get OA3xOriginalProductKey", shell=True))).group(0)),
                 Data("Username:", os.getlogin()), Data("OS:", platform.system()), Data("Version:", platform.version()), 
                 Data("Machine:", platform.machine()), Data("Processor:", platform.processor()), Data("Release:", platform.release()), 
                 Data("Node:", platform.node()), Data("Platform:", platform.platform()), Data("Architecture:", platform.architecture()),
                 Data("IP:", subprocess.check_output("ipconfig", shell=True).decode("utf-8").split("IPv6 Address. . . . . . . . . . . :")[2].split("Temporary IPv6 Address. . . . . . :")[1]),
                 Data("Running as Admin:", "Yes" if os.getpid() == 0 else "No"),Data("ISP Provider : ", subprocess.check_output("ipconfig", shell=True).decode("utf-8").split("Connection-specific DNS Suffix  . : ")[1].split(" ")[0].zfill(2).replace(" ", "0"))
                ]



# create a framework for the data
framework = Framework(init_data)
# create a framework for the data from the registry
registry_framework = Framework(registry_data)
frameworks = [ framework, registry_framework ]

# create a dataframe from the list of data
array = np.array([[init_data[0].key, init_data[0].value], [init_data[1].key, init_data[1].value], [init_data[2].key, init_data[2].value]])

# create a dataframe from the list of data from the registry
registry_array = np.array([
                        [registry_data[0].key, registry_data[0].value], [registry_data[1].key, registry_data[1].value],
                        [registry_data[2].key, registry_data[2].value], [registry_data[3].key, registry_data[3].value],
                        [registry_data[4].key, registry_data[4].value], [registry_data[5].key, registry_data[5].value],
                        [registry_data[6].key, registry_data[6].value], [registry_data[7].key, registry_data[7].value],
                        [registry_data[8].key, registry_data[8].value], [registry_data[9].key, registry_data[9].value],
                        [registry_data[10].key, registry_data[10].value],[registry_data[11].key, registry_data[11].value],
                        [registry_data[12].key, registry_data[12].value]
                        ], 
                        dtype=object)
                        
# create a dataframe from the array
df = pd.DataFrame(array, columns=["Key", "Value"], dtype=object)

# create a dataframe from the array
registry_df = pd.DataFrame(registry_array, columns=["Key", "Value"])
printable_data = [df, registry_df]

# create a dataframe from the list of dataframes
printable_df = pd.concat(printable_data)

# print out the dataframe
os.system("cls" if os.name == "nt" else "clear")


def main():
    """Main function"""
    for f in frameworks:
        # print index name of the framework
        if f == framework:
            print("\033[0;34m Framework Data Loaded\033[0m\033[0;32m[!] \033[0m \033[0;36m x1 \033[0m")
            if f == framework:
                # make x2 colored using [0;33m and [0m
                print("\033[0;33m Framework Data Loaded\033[0m\033[0;31m[!] \033[0m \033[0m \033[0;35mx2 \033[0m")
        for d in f:
            # if IP is found in the data
            if d.key == "IP:":
                DefaultGateWay = subprocess.check_output("ipconfig", shell=True).decode("utf-8").split("Connection-specific DNS Suffix  . : ")[1].split(" ")[0].zfill(2).replace(" ", "0")
                # print the data
                print("Default Gate: {}".format(DefaultGateWay))
            print("{} {}".format(d.key, d.value))
    # create a create_string_buffer in ctypes that will give you a mutable char buffer that's initialized to null bytes
    buffer = ctypes.create_string_buffer(2)
    buff_address = ctypes.addressof(buffer)
    # print out the current buffer contents
    print("Bytes Created: {}".format(buffer.raw.hex()))
    # rewrite the buffer to the pid but in bytes and split it into 4 bytes
    memmove(buffer, pid.to_bytes(4, "little"), 4)
    # print out the current buffer contents
    print("Bytes Written: {}".format(buffer.raw.hex()))
    # say if the buffer is ascii or not
    print("Bytes Written: {}".format(buffer.raw.isascii())) 
    # print out the buffer in ascii
    print("Bytes Decoded: {}".format(buffer.raw.decode("ascii")))
    # use buffer.raw.maketrans
    handle = win32.OpenProcess(0x0400 | 0x0010, False, pid)
    if handle is not None:
        print("Process opened\033[0;31m[!] \033[0m ")
        print("Process handle: {}".format(hex(handle)))
        # use create_string_buffer to get the buffer and remove the null bytes
        breakpoint = ctypes.create_string_buffer(b"\xCC\x90")
        # if breakpoint has 00 in it
        if b"\x00" in breakpoint.raw:
            # remeove the null bytes
            breakpoint.raw.replace(b"\x00", b"")
        # use ctypes.addressof to get the address of the buffer
        bp_address = ctypes.addressof(breakpoint)
        # print out the current buffer contents
        print("Breakpoint Bytes Created: {}".format(breakpoint.raw.hex()))
        print("BP Address: {}".format(hex(bp_address)))
    else:
        if not handle:
            print("Failed to open process")
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())