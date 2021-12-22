from tkinter import *

import numpy as np
import matplotlib.pyplot as plt

from Malyshkina import calc


def count():
    try:
        k_coef = float(txt2.get())
        c = float(txt3.get())
        T = int(txt4.get())
        l = int(txt5.get())
        K = int(txt6.get())
        I = int(txt7.get())
        t_point = int(txt8.get())
        x_point = int(txt9.get())
    except:
        lbl13.configure(text="Проверьте данные")
        return

    if t_point > T or t_point < 0 or x_point > l or x_point < 0:
        lbl13.configure(text="Проверьте данные")
        return
    h_t = T / K
    h_x = l / I
    u_mass = calc(I+1, K+1, k_coef=k_coef, c=c, l=l, T=T)
    I = I + 1
    K = K + 1
    x = np.linspace(0, l, I)
    t = np.linspace(0, T, K)
    scale_x = 1 / h_x
    scale_t = 1 / h_t
    t_element = int(scale_t * t_point)
    x_element = int(scale_x * x_point)
    #print(t_element, x_element)
    lbl13.configure(text="")
    lbl11.configure(text="Ответ: " + str(u_mass[x_element][t_element]))
    u_plt_x = np.zeros(I)
    for i in range(0, I):
        u_plt_x[i] = u_mass[i][t_element]

    u_plt_t = np.zeros(K)
    for i in range(0, K):
        u_plt_t[i] = u_mass[x_element][i]
    #print(x_element)
    _, arr = plt.subplots(1, 2, figsize=(15, 5))
    arr[0].plot(x, u_plt_x, color='b')
    arr[0].grid()
    arr[0].set_title('t = ' + str(t_point))
    arr[0].set_xlabel('x, cм')
    arr[0].set_ylabel('U, ед. температуры')
    arr[1].plot(t, u_plt_t, color='b')
    arr[1].grid()
    arr[1].set_title('x = ' + str(x_point))
    arr[1].set_xlabel('t, c')
    arr[1].set_ylabel('U, ед. температуры')
    plt.show()


window = Tk()
window.title("Решение явной схемы")
window.geometry('550x300')
lbl = Label(window, text="Ввод данных (изначально указаны параметры по умолчанию)")
lbl.grid(column=2, row=0)

lbl = Label(window, text="Решение схемы")
lbl.grid(column=1, row=0)

lbl2 = Label(window, text="Введите параметр k:")
lbl2.grid(column=2, row=1)
txt2 = Entry(window, width=10)
txt2.grid(column=3, row=1)
txt2.insert(0, "0.09")

lbl3 = Label(window, text="Введите параметр c:")
lbl3.grid(column=2, row=2)
txt3 = Entry(window, width=10)
txt3.grid(column=3, row=2)
txt3.insert(0, "1.64")

lbl4 = Label(window, text="Введите длину интервала T:")
lbl4.grid(column=2, row=4)
txt4 = Entry(window, width=10)
txt4.grid(column=3, row=4)
txt4.insert(0, "50")

lbl5 = Label(window, text="Введите длину интервала l:")
lbl5.grid(column=2, row=5)
txt5 = Entry(window, width=10)
txt5.grid(column=3, row=5)
txt5.insert(0, "5")

lbl6 = Label(window, text="Введите количество разбиений K:")
lbl6.grid(column=2, row=6)
txt6 = Entry(window, width=10)
txt6.grid(column=3, row=6)

lbl7 = Label(window, text="Введите количество разбиений I:")
lbl7.grid(column=2, row=7)
txt7 = Entry(window, width=10)
txt7.grid(column=3, row=7)

lbl8 = Label(window, text="Введите точку t (0, T):")
lbl8.grid(column=2, row=8)
txt8 = Entry(window, width=10)
txt8.grid(column=3, row=8)

lbl9 = Label(window, text="Введите точку x (0, l):")
lbl9.grid(column=2, row=9)
txt9 = Entry(window, width=10)
txt9.grid(column=3, row=9)

btn = Button(window, text="Рассчитать", command=count)
btn.grid(column=2, row=10)

lbl11 = Label(window, text="Ответ: ")
lbl11.grid(column=2, row=11)

lbl12 = Label(window, text="")
lbl12.grid(column=2, row=12)

lbl13 = Label(window, text="")
lbl13.grid(column=2, row=13)

window.mainloop()
