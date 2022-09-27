import math as m
import random as r
import numpy as np
import pandas as p
class Random(object):
    def __init__(self, seed):
        self.seed = seed

    def Test(seed):
        a = np.array([seed])
        return print('id:', a*r.random())

class Generate_Random(object):
    def __init__(self, seed):
        self.seed = seed
        return seed
    def iter(x):
        Random.Test(x) 
        return x


a = np.array([(Generate_Random.iter(1),Generate_Random.iter(2),Generate_Random.iter(3),Generate_Random.iter(5),Generate_Random.iter(6),Generate_Random.iter(7),Generate_Random.iter(8),Generate_Random.iter(9)),
             (Generate_Random.iter(4),Generate_Random.iter(5),Generate_Random.iter(6),Generate_Random.iter(8),Generate_Random.iter(9),Generate_Random.iter(10),Generate_Random.iter(11),Generate_Random.iter(12)),
             (Generate_Random.iter(7),Generate_Random.iter(8),Generate_Random.iter(9),Generate_Random.iter(11),Generate_Random.iter(12),Generate_Random.iter(13),Generate_Random.iter(13),Generate_Random.iter(15)),
             (Generate_Random.iter(10),Generate_Random.iter(11),Generate_Random.iter(12),Generate_Random.iter(14),Generate_Random.iter(15),Generate_Random.iter(16),Generate_Random.iter(16),Generate_Random.iter(18)),
             (Generate_Random.iter(13),Generate_Random.iter(14),Generate_Random.iter(15),Generate_Random.iter(17),Generate_Random.iter(18),Generate_Random.iter(24),Generate_Random.iter(25),Generate_Random.iter(21)),
             (Generate_Random.iter(16),Generate_Random.iter(17),Generate_Random.iter(18),Generate_Random.iter(20),Generate_Random.iter(21),Generate_Random.iter(22),Generate_Random.iter(23),Generate_Random.iter(26))])

b = p.DataFrame(a,columns={'S','A','D','B','O','I','<','/3'}).sort_index().head(8)

c = b.describe()
d = c.hist()
def getData(x):
    print(a.dtype,'\n',x)
    return x

getData(c)
getData(d)