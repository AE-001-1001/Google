import numpy, re, os, matplotlib.pyplot as plt,cmath

class Numpy_array:
    def __init__(self, array):
        for i in range(len(array)):
            if re.search(r"([a-z0-9]{5}-){4}[A-Z0-9]{5}", str(array[i])):
                array[i] = re.search(r"([A-Z0-9]{5}-){4}[A-Z0-9]{5}", str(array[i])).group(0)
            self.array = array
    # create a function that will make the array iterable
    def __iter__(self):
        return iter(self.array)

# create a list of data
a = Numpy_array([" " + str(numpy.random.randint(0, 255)) + "." + str(numpy.random.randint(0, 255)) + "." + str(numpy.random.randint(0, 255)) + "." + str(numpy.random.randint(0, 255)) + " " for i in range(0, 15)])
# print the amount of ips loaded

os.system("cls" if os.name == "nt" else "clear")
# use cmath to loop through the array

for i in range(0,1):
    for ip in a:
        # plot the number of ips loaded
        plt.plot(i, len(a.array), "ro")
        print("Scanning " +ip+ "...")
plt.show()