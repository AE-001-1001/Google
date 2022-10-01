import numpy as np 

class Private(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def __str__(x,y):
        x = input('What #')
        y = input('What #')
        return x,y
    def GatherData(x,y):
        print(" X data from %s" % x,"\n Y Data from %s" % y)
        return x,y
a = Private.__str__(3,3)
b = Private.__str__(1,0)
Private.GatherData(a[0],a[1])
Private.GatherData(b[1],b[0])