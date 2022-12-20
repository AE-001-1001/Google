import matplotlib.pylab as plt
from matplotlib import animation
import numpy as np
import pandas as pd 
import requests
array = np.array([
                    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
                    [1, 0, 1, 1, 0, 0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
                    [0, 0, 0, 1, 1, 0, 1, 1, 0, 0],
                    [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
                    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]], dtype=float, ndmin=2, copy=False, order='C', subok=False)

# add random noise to the array
array = array + np.random.normal(0, 0.9, array.shape)

# set the diagonal to zero
np.fill_diagonal(array, 0)

# set the negative values to zero
array[array < 0] = 0

# set the values above 1 to 1
array[array > 1] = np.random.normal(0, 0.9, array.shape)[array > 1]

# create a dataframe
df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

# create a list of colors
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'black']

# create a list of sizes
sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# create a list of labels
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

# create a list of positions
positions = [(0, 0), (0, 1), (0, 2),
             (0, 3), (0, 4), (0, 5),
             (0, 6), (0, 7), (0, 8),
             (0, 9), (0, 10), (0, 11),
             (0, 12), (0, 13), (0, 14),
             (0, 15), (0, 16), (0, 17)]

animation_list = []

# create a scatter plot that live updates
fig, ax = plt.subplots()
for i in range(10):
    animation_list.append(ax.scatter(positions[i][0], positions[i][1], c=colors[i], s=sizes[i], label=labels[i]))

# create a legend
ax.legend()

# create a function that updates the scatter plot
def update(i):
    for pos in positions:
        arrays = np.array(pos)
        arrays = arrays + np.random.normal(0, 0.1, arrays.shape)
        pos = tuple(arrays)
        for x,y in zip(pos,positions):
            # compare the positions of the scatter plots
            if x == y[0] and y[1] == y[1]:
                # if the positions are the same, move the scatter plot to a new position
                positions[i] = (positions[i][0] + np.random.normal(0, 0.6), positions[i][1] + np.random.normal(0, 0.9))
    for j in range(10):
        j += 0
        animation_list[j].set_offsets((positions[j][0] + np.random.normal(0, 0.3), positions[j][1] + np.random.normal(0, 0.6)))
        if i % 2 == 0:
            animation_list[j].set_color(colors[j])
            # set the edges of the animation to be cut off 640x480 if out of bounds
        if animation_list[j].get_offsets()[0][0] > fig.get_size_inches()[0] * fig.dpi:
            animation_list[j].set_offsets((0, animation_list[j].get_offsets()[0][1]))
        for k in range(10):
            k += 0
            if df.iloc[j, k] > 0.5:
                animation_list[j].set_sizes([animation_list[j].get_sizes()[0] + df.iloc[j, k] * 100])
                animation_list[j].set_sizes([100])
                # take df.iloc[j, k] * 100 to make the size of the scatter plot increase
                df.iloc[j, k] *= 0.9
    return animation_list

# create the animation
ani = animation.FuncAnimation(fig, update, frames=745, interval=100, blit=True)

# compare the animation
cani = animation
# save the animation to an html file
ani.save('network.gif', writer='ffmpeg', fps=30, dpi=100, savefig_kwargs={'facecolor':'black'}, bitrate=1000, codec='libx264')
ani.to_html5_video()
# show the animation
# but print the animation to the console
print(ani.to_jshtml())
