import numpy as np
import pandas as pd
import matplotlib.pylab as plt

class Graph(object):
    def __init__(self, object):
        self.object = object

    def __str__(object):
        print("Graph: \n" + str(object))
        return 
        
panda = np.array([(1,2.5,3,5),(2,5,7,5.6),(3,5,7,9)])
main_frame = pd.DataFrame(panda).sort_index(axis=1)
Graph.__str__(plt.plot(main_frame))
Graph.__str__(plt.show())