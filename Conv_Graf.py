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

u_plt = np.zeros(I)
print(u_mass.shape)
for i in range(0, I):
 u_plt[i] = u_mass[i][t_point*scale_t]

plt.plot(x, u_plt)



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

u_plt = np.zeros(I)

for i in range(0, I):
 u_plt[i] = u_mass[i][t_point*scale_t]

plt.plot(x, u_plt)



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

u_plt = np.zeros(I)

for i in range(0, I):
 u_plt[i] = u_mass[i][t_point*scale_t]

plt.plot(x, u_plt)


h_t = h_t/2
h_x = h_x/2

I = int(l / h_x) + 1
K = int(T / h_t) + 1
x = np.linspace(0, l, I)
t = np.linspace(0, T, K)

scale_x = int(1 / h_x)
scale_t = int(1 / h_t)

u_mass = calc(I,K)

u_plt = np.zeros(I)

for i in range(0, I):
 u_plt[i] = u_mass[i][t_point*scale_t]

plt.plot(x, u_plt)


plt.legend(['h_t = 0.01, h_x = 0.5','h_t = 0.005, h_x = 0.25','h_t = 0.0025, h_x = 0.125', 'h_t = 0.00125, h_x = 0.0625'])
plt.title("t = 10")
plt.xlabel('x, cм')
plt.ylabel('U, ед. температуры')
plt.grid()
plt.show()

