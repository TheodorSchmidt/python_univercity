from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.messagebox
from matplotlib.figure import Figure

x1 = 0
x2 = 0

def close_win():
    root.destroy()

def show_reference():
    ref_win = Toplevel(root)
    f = open('tkinter_lib.txt', encoding='utf-8')
    text = f.read()
    txt = Label(ref_win, text=text, anchor='w', justify=LEFT)
    txt.pack()

def clearall():
    title.cla()
    title.set_xlabel('x', fontsize=12)
    title.set_ylabel('y', fontsize=12)
    fig.canvas.draw()

def choose_X():
    def getV(graph_win):
        global x1
        global x2
        if int(scale1.get()) >= int(scale2.get()):
            tkinter.messagebox.showinfo("Ошибка", "Начальное значение Х должно быть меньше конечного значения Х")
        else: 
            x1 = int(scale1.get())
            x2 = int(scale2.get())    
        diap_win.destroy()
    diap_win = Toplevel(root)
    txt1 = Label(diap_win, text="Начальное значение X:")
    txt2 = Label(diap_win, text="Конечное значение Х:")
    scale1 = Scale(diap_win, orient=HORIZONTAL, length=500, from_=-1000, to=1000, tickinterval=200, resolution=1)
    scale2 = Scale(diap_win, orient=HORIZONTAL, length=500, from_=-1000, to=1000, tickinterval=200, resolution=1)
    btn_col = Button(diap_win, text="Получить значения")
    txt1.pack()
    scale1.pack()
    txt2.pack()
    scale2.pack()
    btn_col.bind("<Button-1>", getV)
    btn_col.pack()
    root.wait_window(diap_win)

def function(name):
    global x1, x2
    clearall()
    choose_X()
    if x1 == x2 == 0:
        return 0
    x = np.linspace(x1, x2, 1000)
    if name == 'sin':
        y = np.sin(x)
        title.set_title('sin(x)', fontsize=12)
        title.set_ylim(-1, 1)
    elif name == 'cos':
        y = np.cos(x)
        title.set_title('cos(x)', fontsize=12)
        title.set_ylim(-1, 1)
    elif name == 'tg':
        y = np.tan(x)
        y[:-1][np.diff(y) < 0] = np.nan
        title.set_title('tg(x)', fontsize=12)
        title.set_ylim(-10, 10)
    elif name == 'ctg':
        y = 1 / np.tan(x)
        y[:-1][np.diff(y) > 0] = np.nan
        title.set_title('ctg(x)', fontsize=12)
        title.set_ylim(-10, 10)
    elif name == 'x2':
        y = x * x
        title.set_title('x^2', fontsize=12)
        title.set_ylim(0, max(x1*x1, x2*x2))
    else:
        y = x * x * x  
        title.set_title('x^3', fontsize=12)
        title.set_ylim(min(x1*x1*x1, x2*x2*x2), max(x1*x1*x1, x2*x2*x2))
    title.plot(x, y)
    title.minorticks_on()
    title.grid(which='major')
    title.grid(which='minor', linestyle=':')
    fig.canvas.draw()
    x1 = x2 = 0   

root = Tk()
root.geometry("600x600")
m = Menu(root)
root.config(menu=m)
fm = Menu(m)
m.add_cascade(label="Построить график", menu=fm)
fm.add_command(label="y = sin(x)", command=lambda f='sin': function(f))
fm.add_command(label="y = cos(x)", command=lambda f='cos': function(f))
fm.add_command(label="y = tg(x)", command=lambda f='tg': function(f))
fm.add_command(label="y = ctg(x)", command=lambda f='ctg': function(f))
fm.add_command(label="y = x^2", command=lambda f='x2': function(f))
fm.add_command(label="y = x^3", command=lambda f='x3': function(f))
m.add_command(label="Справка", command=show_reference) 
m.add_command(label="Выход", command=close_win)
fig = Figure(figsize=(6,6), dpi=100)
title = fig.add_subplot(111)
canv = FigureCanvasTkAgg(fig, master=root)
title.set_xlabel('x', fontsize=12)
title.set_ylabel('y', fontsize=12)
title.minorticks_on()
title.grid(which='major')
title.grid(which='minor', linestyle=':')
canv._tkcanvas.pack(fill=X)
root.mainloop()