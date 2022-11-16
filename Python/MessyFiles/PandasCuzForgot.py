import pandas as pd
import numpy as np
from matplotlib import pylab as ply
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# create a class that makes a dataframe
class DataFrameMaker:
    def __init__(self, data, index, columns):
        self.data = data
        self.index = index
        self.columns = columns
    def makeDataFrame(self):
        df = pd.DataFrame(data=self.data, index=self.index, columns=self.columns)
        return df

# create a class that makes a plot
class PlotMaker:
    def __init__(self, df):
        self.df = df
    def makePlot(self):
        self.df.plot()
        plt.show()
    
#prepare a animation
def prepare_animation(df):

    def animate(frame_number):
        data = np.random(1000)
        n, _ = np.histogram(data, HIST_BINS)
        for count,rect in zip(n,df.patches):
            rect.set_height(count)
        return df.patches
    return animate


# create a function that makes a dataframe and then plots and returns it
def makeDataFrameAndPlot(data, index, columns):
    df = DataFrameMaker(data, index, columns).makeDataFrame()
    PlotMaker(df).makePlot()
    return df

data = np.random.randn(26, 26)
#create a random index (a-z)
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
columns = ['one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twentyone', 'twentytwo', 'twentythree', 'twentyfour', 'twentyfive', 'twentysix']
df = [index, columns]

np.random.seed(19680801)
HIST_BINS = ply.linspace(-4,4,100)
data = np.random.randn(100)
n, _ = np.histogram(data, HIST_BINS)
fig, ax = plt.subplots()
_, _, bar_container = ax.hist(data, HIST_BINS, lw=1,
                                ec="blue", fc="green", alpha=1)
ax.set_ylim(top=55)  # set safe limit to ensure that all data is visible.


ani = animation.FuncAnimation(fig, prepare_animation(df), 100,
                              repeat=False, blit=True)
plt.show()