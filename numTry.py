import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.animation as animation

def dats():
    L = dats.L; n = dats.n
    t = np.linspace(0, L, n);
    k = [x*2*np.pi/L for x in range(-n/2, n/2)]
    y1 =  (3*np.sin(2*t) + 0.5*np.tanh(0.5*(t-3))) + np.exp(-(t-4)**2)\
        + 1.5*np.sin(5*t) + 4*np.cos(3*(t-6)**2)/10+(t/20)**3
    y1 = y1/max(y1)
    j = 0

    while j < dats.n-1:
        j += 1
        y2 = np.exp(-(t-t[j])**4)
        y3 = y1 * y2
        y4 = np.fft.fft(y3)
        y4 = np.fft.fftshift(np.abs(y4))

        yield y1, y2, y3, y4, t, k

# domain length and descretization
dats.L = 4 * np.pi; dats.n = 528


fig, (ax1, ax2, ax3) = plt.subplots(3,1)

for ax in [ax1, ax2]:
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0,4*np.pi)


line1, = ax1.plot([],[])
line2, = ax1.plot([],[])
line3, = ax2.plot([],[])
line4, = ax3.plot([],[])
line = [line1, line2, line3, line4]




def anim8(data):
    y1, y2, y3, y4, t, k = data

    ax3.set_xlim(-50, 50)
    ax3.set_ylim( 0, 50)

    line[0].set_data(t,y1)
    line[1].set_data(t,y2)
    line[2].set_data(t,y3)
    line[3].set_data(k,y4)

    return line

ani = animation.FuncAnimation(fig, anim8, dats, blit = True, interval = 5, repeat = True)

plt.show()
