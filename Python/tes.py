#import modules to write to csv file
import numpy as np
import pandas as pd


# create a function to write to csv file
def write_to_csv(data, filename):
    df = pd.DataFrame(data, index=None, columns=['a', 'b', 'c'])
    df.to_csv(filename, index=True, header=False, sep=':',columns=df.columns,date_format='%Y-%m-%d %H:%M:%S',index_label='index',encoding='utf-8')
    return

# create a function to read from csv file
def read_from_csv(filename):
    df = pd.read_csv(filename, header=None)
    return df.values


def Run_Main(data):
    for (i, row) in enumerate(data):
        new_data = data + np.random.randn(3,6).T
        print(i , row)
        for (j, col) in enumerate(new_data):
            new_data = new_data * np.random.randn(3,6).T
            print(j, col)

    if data is not None:
        write_to_csv(new_data, 'neo.csv')
        print('\n',read_from_csv('neo.csv'))
    return new_data