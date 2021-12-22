import numpy as np
import matplotlib.pyplot as plt

from Malyshkina import calc



l = 5
T = 50
h_t = 0.01
h_x = 0.5



x_point = 3
t_point = 10

points = np.zeros(5)

I = int(l / h_x) + 1
K = int(T / h_t) + 1
x = np.linspace(0, l, I)
t = np.linspace(0, T, K)

I = int(l / h_x) + 1
K = int(T / h_t) + 1

scale_x = int(1 / h_x)
scale_t = int(1 / h_t)

u_mass = calc(I,K)

u_plt = np.zeros(K)
print(u_mass.shape)
for i in range(0, K):
 u_plt[i] = u_mass[x_point*scale_x][i]

print(x_point*scale_x)

plt.plot(t, u_plt)
points[0] = u_plt[x_point*scale_x]


h_t = h_t/2
h_x = h_x/2


I = int(l / h_x) + 1
K = int(T / h_t) + 1
x = np.linspace(0, l, I)
t = np.linspace(0, T, K)

I = int(l / h_x) + 1
K = int(T / h_t) + 1

scale_x = int(1 / h_x)
scale_t = int(1 / h_t)

u_mass = calc(I,K)

u_plt = np.zeros(K)

for i in range(0, K):
 u_plt[i] = u_mass[x_point*scale_x][i]

plt.plot(t, u_plt)
points[1] = u_plt[x_point*scale_x]
print(x_point*scale_x)

h_t = h_t/2
h_x = h_x/2

I = int(l / h_x) + 1
K = int(T / h_t) + 1
x = np.linspace(0, l, I)
t = np.linspace(0, T, K)

I = int(l / h_x) + 1
K = int(T / h_t) + 1

scale_x = int(1 / h_x)
scale_t = int(1 / h_t)

u_mass = calc(I,K)

u_plt = np.zeros(K)

for i in range(0, K):
 u_plt[i] = u_mass[x_point*scale_x][i]

plt.plot(t, u_plt)
points[2] = u_plt[x_point*scale_x]
print(x_point*scale_x)
h_t = h_t/2
h_x = h_x/2

I = int(l / h_x) + 1
K = int(T / h_t) + 1
x = np.linspace(0, l, I)
t = np.linspace(0, T, K)

I = int(l / h_x) + 1
K = int(T / h_t) + 1

scale_x = int(1 / h_x)
scale_t = int(1 / h_t)

u_mass = calc(I,K)

u_plt = np.zeros(K)

for i in range(0, K):
 u_plt[i] = u_mass[x_point*scale_x][i]

plt.plot(t, u_plt)
points[3] = u_plt[x_point*scale_x]

plt.legend(['h_t = 0.01, h_x = 0.5','h_t = 0.005, h_x = 0.25','h_t = 0.0025, h_x = 0.125', 'h_t = 0.00125, h_x = 0.0625'])
plt.title("x = 3")
plt.xlabel('t, c')
plt.ylabel('U, ед. температуры')
plt.grid()
plt.show()

