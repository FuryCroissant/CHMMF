from Malyshkina import calc
import matplotlib.pyplot as plt

import numpy as np

t = [10,20,30,40]
T = 50
I = 50
K = 1000
l = 5

u = calc(I,K)
x = np.linspace(0, l, I + 1)
for el in t:
    u_plt = np.zeros(I + 1)
    for i in range(0, I + 1):
        u_plt[i] = u[i][int(el * K / T)]
    plt.plot(x, u_plt)

plt.legend(['t = 10','t = 20','t = 30','t = 40'])
plt.xlabel('x, см')
plt.ylabel('U, ед. температуры')
plt.grid()
plt.show()


x_p = [1,2,3,4]
T = 50
I = 50
K = 1000
l = 5

u = calc(I,K)
t = np.linspace(0, T, K + 1)
for el in x_p:
    u_plt = np.zeros(K + 1)
    for i in range(0, K + 1):
        u_plt[i] = u[int(el * I / l)][i]
    plt.plot(t, u_plt)

plt.legend(['x = 1','x = 2','x = 3','x = 4'])
plt.xlabel('t, с')
plt.ylabel('U, ед. температуры')
plt.grid()
plt.show()