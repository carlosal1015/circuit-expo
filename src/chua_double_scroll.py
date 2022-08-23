#!/usr/bin/env python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from numpy.typing import ArrayLike
import numpy as np
from scipy.integrate import odeint

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]


def chua(
    t: float, X: ArrayLike, α: float, β: float, m_0: float, m_1: float
) -> ArrayLike:
    dX: ArrayLike = np.empty_like(X)
    g_x = m_1 * X[0] + 0.5 * (m_0 - m_1) * (np.abs(X[0] + 1) - np.abs(X[0] - 1))

    dX[0] = α * (X[1] - (g_x))
    dX[1] = X[0] - X[1] + X[2]
    dX[2] = -β * X[1]
    return dX


α: float = 10.0
β: float = 16.4
m_0: float = -1.22
m_1: float = 0.628

time = np.linspace(start=0, stop=300, num=50000)
X_0 = [0.1, 0.15, 0.01]

X_s = odeint(func=chua, y0=X_0, t=time, args=(α, β, m_0, m_1), tfirst=True)

plt.clf()
ax = plt.figure().add_subplot(projection="3d")
ax.plot(X_s[:, 0], X_s[:, 1], X_s[:, 2], "r-", lw=0.5)
ax.set_xlabel(r"$V_{C_{1}}$", fontsize=15)
ax.set_ylabel(r"$V_{C_{2}}$", fontsize=15)
ax.set_zlabel(r"$i_{L}$", fontsize=15)
# ax.set_title(r"Atractor de doble espiral", fontsize=15)
plt.tick_params(labelsize=8, width=1)
plt.savefig("img/chua_double_scroll.pdf", transparent=True, bbox_inches="tight")

plt.clf()
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, constrained_layout=True)
ax0.plot(time, X_s[:, 0], "r")
ax0.set_ylabel(r"$V_{C_{1}}$", fontsize=15)
ax0.set_xlim([0, 100])
ax1.plot(time, X_s[:, 1], "g")
ax1.set_ylabel(r"$V_{C_{2}}$", fontsize=15)
ax1.set_xlim([0, 100])
ax2.plot(time, X_s[:, 2], "b")
ax2.set_ylabel(r"$i_{L}$", fontsize=15)
ax2.set_xlim([0, 100])
fig.legend(
    [ax0.get_ylabel(), ax1.get_ylabel(), ax2.get_ylabel()],
    loc="upper center",
    shadow=True,
    title="Leyenda",
    fancybox=True,
    ncol=3,
    bbox_to_anchor=(0.5, 1.12),
)
plt.savefig("img/chua_solutions.pdf", transparent=True, bbox_inches="tight")

β_1: float = β + 1e-3
Xs_1 = odeint(func=chua, y0=X_0, t=time, args=(α, β_1, m_0, m_1), tfirst=True)

plt.clf()
fig, ax = plt.subplots(constrained_layout=True)
(line1,) = ax.plot(time, X_s[:, 0], "r", label=r"$\beta_{1}=16.4$")
(line2,) = ax.plot(time, Xs_1[:, 0], label=r"$\beta_{2}=16.401$")
ax.set_xlim([25, 105])
ax.legend(
    loc="upper center",
    shadow=True,
    title="Leyenda",
    fancybox=True,
    ncol=2,
    bbox_to_anchor=(0.5, 1.15),
)
plt.savefig("img/changing_beta.pdf", transparent=True, bbox_inches="tight")
