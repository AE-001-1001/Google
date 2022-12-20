import matplotlib.pylab as plt
from matplotlib import animation
import numpy as np
import pandas as pd 

# create a gif that is a broken heart
# create a figure
fig = plt.figure()
# change the background color
fig.patch.set_facecolor('black')
# change the background color of the subplot
# create a subplot
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2), aspect='equal', facecolor='black')
# create a scatter plot
scatter = ax.scatter([], [], linewidths=2, edgecolors='black', s=100, c='white', marker='o')
# create a line
line, = ax.plot([], [],lw=2, c='black', marker='o', markersize=10, markerfacecolor='white', markeredgecolor='black')
line2, = ax.plot([], [], lw=2, c='black', marker='o', markersize=10, markerfacecolor='white', markeredgecolor='black')
# create a function that will be called sequentially
def init():
    line.set_data([], [])
    line2.set_data([], [])
    # print out the line and line2
    print(line, line2)
    return line, line2,


# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(-100, 50, 1000)
    y = np.array([np.sqrt(1 + np.random.randint(0,25) - (abs(i/100) - 1)**2) for i in x])
    y2 = np.array([-2 + np.random.randint(0,100) * i for i in y])
    line.set_data(x, y)
    line2.set_data(x, y2)
    # when loading print out the percentage
    print(F'{i/2004*100}'+'%', end='\r')
    if i == i-1:
        print('Done')
    return line, line2,




# call the animator.  blit=True means only re-draw the parts that have changed.
wave = animation.FuncAnimation(fig, animate, init_func=init, frames=2004, interval=10, blit=True)


wave.save('basic_animation.gif', writer='Pillow', fps=60)

plt.show()