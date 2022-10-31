#Create a script to make a neural network using classes, functions and methods, weights and biases and activation functions
#import modules to write to csv file
import numpy as np
import pandas as pd
import time as t
import os 
class Console(object):
    """Clean the Console Frame"""
    def __init__(self, cmd):
        self.cmd = cmd
    def callCommand(cmd):
        a = os.system(cmd)
        return a

#Create timer for how long it takes on each iteration
def timer():
    """ Timer for how long it takes on each iteration """
    start = t.time()
    for i in range(1000000):
        i = i*2
    end = t.time()
    print("Duration: %s" % (end - start))
    return end

#create a function every 5 minutes clears the csv file
def clear_csv():
    """ Clear the csv file every 5 minutes """
    while True:
        t.sleep(1)
        open("neo.csv", "w+").close()
        return timer()

# create a function to write to csv file
def write_to_csv(data, filename):
    """ Write data to a CSV file path """
    # make columns labeled for each column
    df = pd.DataFrame(data, index=None, columns=['a', 'b', 'c'], dtype=None, copy=False)
    df.to_csv(filename, index=True, header=True, sep=':',columns=df.columns,date_format='%Y-%m-%d %H:%M:%S',index_label='index',encoding='utf-8')
    return timer()

# create a function to read from csv file
def read_from_csv(filename):
    """ Read data from a CSV file path """
    df = pd.read_csv(filename, header=None)
    return df.values

#create a function to run the main program
def Run_Main(data):
    """ Run the main program """
    for (i, row) in enumerate(data):
        new_data = data + np.random.randn(3,6).transpose()
        write_to_csv(new_data, "neo.csv")
        print(i , row)
        for (j, col) in enumerate(new_data):
            new_data1 = new_data * np.random.randn(3,6).transpose()
            write_to_csv(new_data1, "neo.csv")
            print(j, col)
            for (k, val) in enumerate(new_data):
                new_data2 = new_data1 * np.random.randn(3,6).transpose() + val
                print("New Data: ", new_data2)
                write_to_csv(new_data2, "neo.csv")
                Console.callCommand("cls")
        return timer(),read_from_csv("neo.csv")


