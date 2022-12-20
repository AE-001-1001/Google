# create a 3D plot 
import matplotlib.pylab as plt
import numpy as np
import matplotlib.animation as animation
import matplotlib as mpl
import ctypes 

win32 = ctypes.windll.kernel32
# creates the function that's the basis of the plot
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))

    
# creates the x and y values for the plot
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
y = np.linspace(-np.pi, np.pi, 256, endpoint=True)
X, Y = np.meshgrid(x, y)

# creates the figure and the axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# creates the surface plot
surf = ax.plot_surface(X, Y, f(X, Y), rstride=1, cstride=1, cmap=plt.cm.cool, linewidth=2, antialiased=True)
# loop through the cmap to get the colors

# creates the animation
def update(i):
    ax.view_init(elev=10., azim=i)
    # print the progress in color (green)
    win32.SetConsoleTextAttribute(win32.GetStdHandle(-11), 10)
    # with frame number
    print("Rendering Frame: " + str(i) + " Progress: " + str(round(i/360*100, 2)) + "%", end="\r")
    win32.SetConsoleTextAttribute(win32.GetStdHandle(-11), 7)
    for updatedFrame in surf._facecolors:
        surf._facecolors[i] = surf._facecolors[i][0] + updatedFrame
    # print the Frame Number it is Rendering
    return fig, 

# creates the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=20, blit=True, repeat=True , repeat_delay=1000)

# saves the animation
ani.save('3Dplot.gif', writer='imagemagick', fps=15)