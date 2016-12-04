import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.animation as animation




x_hi = 10; x_lo = 0; y_hi = 1; y_lo = -1
fig = plt.figure() # creates figure to plot
ax = plt.axes(xlim=(x_lo,x_hi), ylim=(y_lo,y_hi)) # axis of figure
line1, = ax.plot([],[]) # line is empty, will be added later to the plot
line2, = ax.plot([],[]) # second line obj for multiple in figure


def init(): # initializes line obj
    line1.set_data([],[])
    line2.set_data([],[])
    return line1,line2,

def animate(i): # creates a line sequentially called for animation
    x = np.linspace(x_lo, x_hi, 1000)
    y1 = np.exp(-(x-x[i])**4)
    y2 = (2*np.sin(2*x) + 0.5*np.tanh(0.5*(x-3))) + 0.2*np.exp(-(x-4)**2)\
     + 1.5*np.sin(5*x) + 2*np.cos(3*(x-6)**2)/10+(x/20)**3
    y2 = y2/max(y2)
    line1.set_data(x,y1)
    line2.set_data(x,y2)
    return line1,line2,

# frames is number of total frames to animate, interval is ms delay btw frames
# blit = True tells to only redraw changed pieces of plot
anim = animation.FuncAnimation(fig, animate, init_func = init,
                                frames = 1000, interval=1, blit = True, repeat = False)

pylab.show()
