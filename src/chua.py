from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import odeint

plt.rcParams['text.usetex'] = True

m0 = -1.22
m1 = 0.628
tmax = 100


def chua(x, t, a=10.0, b=16.4):
    f_x = m1*x[0] + 0.5*(m0-m1) * (np.abs(x[0] + 1) - np.abs(x[0] - 1))
    return [a * (x[1] - (f_x)),
            x[0] - x[1] + x[2],
            -b*x[1]]


time = np.linspace(0, tmax, 50000)
x0 = [0.1, 0.15, 0.01]

xs = odeint(chua, x0, time)
plt.figure(1)
plt.subplot(311)
plt.plot(time, xs[:, 0], 'r')
plt.subplot(312)
plt.plot(time, xs[:, 1], 'g')
plt.subplot(313)
plt.plot(time, xs[:, 2], 'b')
#plt.show()
plt.savefig('chua.pdf', transparent=True, bbox_inches='tight')