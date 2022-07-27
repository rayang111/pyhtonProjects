# coding: utf-8

from tkinter import *
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def keybord(event):
    key = event.keysym

def adding():
    global clos
    wind.destroy()
    wind.quit()
    clos = 1

def continuing():
    wind.destroy()
    wind.quit()

def Window1():
    global wind
    wind = Tk()
    f = Figure(figsize=(5,5), dpi=100)
    plt = f.add_subplot(111)
    plt.set_title('P(Crashing)',loc='center')
    plt.plot([0,1,2,3],[0,0.25,0.75,1], label='Crash probability')
    plt.plot([0,1,2,3],[1,0.75,0.25,0], label='Survive probability')
    plt.axis([0, 3, 0, 1])
    plt.set_ylabel('Probability')
    plt.set_xlabel('Time (seconds)')
    plt.grid(True)
    plt.text(1,0.9,r'Make your choice...')
    plt.legend()
    canvas = FigureCanvasTkAgg(f,wind)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand= True)
    wind.protocol("WM_DELETE_WINDOW", adding)
    bouton=Button(wind, text="Continue", command=continuing)
    bouton.pack()

def Window2():
    global wind2
    wind2 = Tk()
    

Window1()
clos = 0
wind.mainloop()
if clos == 1:
    quit()
else:
    pass

Window2()
wind2.mainloop()
