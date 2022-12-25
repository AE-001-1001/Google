import binascii as ba
import pandas as pd
import numpy as np
import time as t
import re, subprocess, platform, os, ctypes
# use windll to load the dll
win32 = ctypes.windll.kernel32

# use the dll to get the PID of the process
pid = win32.GetCurrentProcessId()

# create a class that will store the data with key value pairs
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# use Data to create a list of data
data = [Data("PID", pid), Data("Time", t.strftime("%Y:%H:%M:%S:%p")), Data("Path", os.getcwd())]
# use Data to create a list of data from the registry
registry_data = [
                 Data("HWID", re.search(r"([A-Z0-9]{5}-){4}[A-Z0-9]{5}", str(subprocess.check_output("wmic path softwarelicensingservice get OA3xOriginalProductKey", shell=True))).group(0)),
                 Data("Username", os.getlogin()), Data("OS", platform.system()), Data("Version", platform.version()), 
                 Data("Machine", platform.machine()), Data("Processor", platform.processor()), Data("Release", platform.release()), 
                 Data("Node", platform.node()), Data("Platform", platform.platform()), Data("Architecture", platform.architecture()),
                 Data("IP", subprocess.check_output("ipconfig", shell=True).decode("utf-8").split("IPv4 Address. . . . . . . . . . . : ")[1].split(" ")[0]),
                ]
# create a dataframe from the list of data
array = np.array([[data[0].key, data[0].value], [data[1].key, data[1].value], [data[2].key, data[2].value]])
# create a dataframe from the list of data from the registry
registry_array = np.array([
                        [registry_data[0].key, registry_data[0].value], [registry_data[1].key, registry_data[1].value],
                        [registry_data[2].key, registry_data[2].value], [registry_data[3].key, registry_data[3].value],
                        [registry_data[4].key, registry_data[4].value], [registry_data[5].key, registry_data[5].value],
                        [registry_data[6].key, registry_data[6].value], [registry_data[7].key, registry_data[7].value],
                        [registry_data[8].key, registry_data[8].value], [registry_data[9].key, registry_data[9].value],
                        [registry_data[10].key, registry_data[10].value]
                           ], dtype=object)
# create a dataframe from the array
df = pd.DataFrame(array, columns=["Key", "Value"])
# create a dataframe from the array
registry_df = pd.DataFrame(registry_array, columns=["Key", "Value"])
printable_data = [df, registry_df]
# create a dataframe from the list of dataframes
printable_df = pd.concat(printable_data)
# print out the dataframe
os.system("cls" if os.name == "nt" else "clear")
print(printable_df)