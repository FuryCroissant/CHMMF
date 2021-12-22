import numpy as np
import matplotlib.pyplot as plt



def calc(I,K, k_coef = 0.09, c = 1.64, T = 50, l = 5):
    h_x = l / I  # шаг разбиения диапазона изменения переменной x
    h_t = T / K  # шаг разбиения диапазона изменения переменной t
    x = np.linspace(0, l, I + 1)
    t = np.linspace(0, T, K + 1)
    a = k_coef/c
    u = np.zeros((I + 1, K + 1))
    for i in range(I + 1):
        u[i][0] = np.cos(np.pi * x[i] / (2*l)) ** 2

    for k in range(0, K):
        u[1][k + 1] = u[1][k] + h_t / (h_x ** 2) * a * (u[2][k] - 2*u[1][k] + u[0][k])
        u[0][k + 1] = u[1][k+1]
        for i in range(2, I):
            u[i][k + 1] = u[i][k] + h_t / (h_x ** 2) * a * (u[i + 1][k] - 2 * u[i][k] + u[i - 1][k])
        u[I][k + 1] = 0

    return u



if __name__ == "__main__":
    l = 5
    T = 50
    I = 10
    K = 1000
    x = np.linspace(0, l, I + 1)
    t = np.linspace(0, T, K + 1)
    u = calc(I, K)
    u_plt_x = np.zeros(I + 1)
    for i in range(0, I + 1):
        u_plt_x[i] = u[i][50]
    u_plt_t = np.zeros(K + 1)
    for k in range(0, K + 1):
        u_plt_t[k] = u[6][k]

    plt.plot(x, u_plt_x)
    plt.title("t = 45")
    plt.grid()
    plt.show()
    plt.plot(t, u_plt_t)
    plt.title("x = 3")
    plt.grid()
    plt.show()

