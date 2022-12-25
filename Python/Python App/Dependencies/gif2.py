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
surf = ax.plot_surface(X, Y, f(X, Y), rstride=1, cstride=1, cmap=plt.cm.RdYlGn, linewidth=2, antialiased=True)
# increase loading time
fig.canvas.draw()


def update(i):
    ax.view_init(elev=10., azim=i)
    # print the progress in color (green)
    win32.SetConsoleTextAttribute(win32.GetStdHandle(-11), 10)
    # with frame number
    for frame in range(0, i):
        i += 1
        print("Rendering Frame: " + str(frame) + " Progress: " + str(round(frame/360*100, 2)) + "%", end="\r")
    win32.SetConsoleTextAttribute(win32.GetStdHandle(-11), 7)
    for updatedFrame in surf._facecolors:
        surf._facecolors[i] = surf._facecolors[i][0] + updatedFrame
        # make sure the surf color is not too bright
        for color in surf._facecolors[i]:
            # check if the color is too bright using floats
            if color > np.random.uniform(0.8, 1):
                # make it a little darker
                color = color - np.random.uniform(0.1, 0.2)
            # check if the color is too bright using ints
            elif color > np.random.randint(200, 255):
                # make it a little darker
                color = color - np.random.randint(50, 100)
            
    # print the Frame Number it is Rendering
    return fig, 

# creates the animation
ani = animation.FuncAnimation(fig, update, frames=360, interval=20, blit=True, repeat=True , repeat_delay=1000, save_count=360, cache_frame_data=False, init_func=None)

# saves the animation
ani.save('3Dplot.gif', writer='Pillow', fps=15)