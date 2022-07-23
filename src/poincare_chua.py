import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

plt.rcParams['text.usetex'] = True

alpha = 10
beta = 16.4
R = -1.22
C_2 = -0.728


def chua(t, u):
    x, y, z = u
    f_x = C_2*x + 0.5*(R-C_2)*(abs(x+1)-abs(x-1))
    return [alpha*(y-x-f_x), x - y + z, -beta * y]


t_0 = 0
dt = 1e-3
t_final = 300
t = np.linspace(t_0, t_final, 50000)

u0 = [0.1, 0.15, 0.01]
x_section = 1


def poincare(t, vector):
    x = vector[0]
    return x - x_section


poincare.direction = -1
sol = solve_ivp(chua,
                [0, 60000],
                u0,
                events=poincare,
                dense_output=True)

sol.sol

t = sol.t_events[0]
vectors = sol.sol(t)

chua_attractor = plt.figure()
ax = chua_attractor.add_subplot(111, projection='3d')
ax.plot(sol.y[0], sol.y[1], sol.y[2], ',', alpha=0.12)

x, y, z = vectors
# ax.plot(x, y, z, ".", alpha=0.4)
ax.set_xlabel(r'$v_{1}$', fontsize=15)
ax.set_ylabel(r'$v_{2}$', fontsize=15)
ax.set_zlabel(r'$i_{L}$', fontsize=15)
plt.tick_params(labelsize=15)
plt.savefig('chua_doble_atractor.pdf', transparent=True, bbox_inches='tight')
plt.close()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.view_init(30, -90)
# ax.plot(sol.y[0], sol.y[1], sol.y[2], ',')
# ax.plot(x, y, z, ".")
# ax.set_xlabel(r'$v_{1}$', fontsize=15)
# ax.set_ylabel(r'$v_{2}$', fontsize=15)
# ax.set_zlabel(r'$i_{L}$', fontsize=15)
# plt.savefig('chua_doble_atractor30.pdf', transparent=True, bbox_inches='tight')


plt.plot(y[:-1], y[:-1], ",")
plt.xlabel(r'$v_{2}\left(t_{n}\right)$', fontsize=15)
plt.ylabel(r'$v_{2}\left(t_{n+1}\right)$', fontsize=15)
plt.savefig('poincare_chua.pdf', transparent=True, bbox_inches='tight')
plt.close()
