import math
import numpy as np
import pandas as pd
import random as ran

def NewTest(i):
    AR1D = np.array([(1+i, 2+i, 3+i, 4+i),(4+i, 5+i, 6+i, 7+i),(7+i, 8+i, 9+i, 10+i),(11+i, 12+i, 13+i, 14+i),(15+i,16+i,17+i,18+i),(19+i,20+i,21+i,22+i)]).reshape(4,6)
    x = AR1D[0:4]* ran.random() / 10 + i
    graph = pd.DataFrame((AR1D[0:4]+x+(AR1D[0:4]+x))+(AR1D[0:4]+x+(AR1D[0:4]+x)).argsort(axis=0))
    test = pd.DataFrame((graph[0:5] + graph[0:5] / graph[0:5]))
    Edtest = test.align(other=graph,axis=1)
    return Edtest

def RunNewTest(x):
    for i in range(0,x):
        print(NewTest(i))
    return 0

RunNewTest(2004)