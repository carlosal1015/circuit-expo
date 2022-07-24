#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.integrate import odeint

plt.rcParams['text.usetex'] = True
plt.rcParams['font.serif'] = ['Computer Modern']

m0: float = -1.22
m1: float = 0.628
tmax: float = 300


def chua(x, t, a=10.0, b=16.4):
    f_x = m1*x[0] + 0.5*(m0-m1) * (np.abs(x[0] + 1) - np.abs(x[0] - 1))
    return [a * (x[1] - (f_x)),
            x[0] - x[1] + x[2],
            -b*x[1]]


time = np.linspace(0, tmax, 50000)
x0 = [0.1, 0.15, 0.01]

xs = odeint(chua, x0, time)

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(xs[:, 0], xs[:, 1], xs[:, 2], 'r-', lw=0.5)

ax.set_xlabel(r'$v_{C_{1}}$', fontsize=15)
ax.set_ylabel(r'$v_{C_{2}}$', fontsize=15)
ax.set_zlabel(r'$i_{L}$', fontsize=15)
plt.tick_params(labelsize=15)
ax.set_title(r'Atractor de doble espiral', fontsize=15)
# plt.show()
plt.savefig('chua_double.pdf', transparent=True, bbox_inches='tight')
