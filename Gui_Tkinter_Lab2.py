import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

def Catch1(dummy):
    a = random.randint(0, 650)
    b = random.randint(0, 650)
    b1.place(x=a, y=b)

def Catch2(dummy):
    a = random.randint(0, 650)
    b = random.randint(0, 650)
    b2.place(x=a, y=b)

def Catch3(dummy):
    a = random.randint(0, 650)
    b = random.randint(0, 650)
    b3.place(x=a, y=b)

def Catch4(dummy):
    a = random.randint(0, 650)
    b = random.randint(0, 650)
    b4.place(x=a, y=b)

def Catch5(dummy):
    a = random.randint(0, 650)
    b = random.randint(0, 650)
    b5.place(x=a, y=b)

ev = tk.Tk()
ev.title('Catch me if you can')
ev.geometry("1100x900")

b1 = tk.Button(ev, text='Catch me if you can', bg='powderblue', fg='navy')
b1.config(font=('courier new', 10, 'bold'))
b1.place(x=20, y=30)
b2 = tk.Button(ev, text='Catch me if you can', bg='pink', fg='red')
b2.config(font=('courier new', 14, 'bold'))
b2.place(x=260, y=188)
b3 = tk.Button(ev, text='Catch me if you can', bg='yellow', fg='black')
b3.config(font=('courier new', 18, 'bold'))
b3.place(x=160, y=300)
b4 = tk.Button(ev, text='Catch me if you can', bg='peach puff', fg='red')
b4.config(font=('courier new', 22, 'bold'))
b4.place(x=400, y=388)
b5 = tk.Button(ev, text='Catch me if you can', bg='lightgreen', fg='navy')
b5.config(font=('courier new', 26, 'bold'))
b5.place(x=300, y=520)
b1.bind("<Enter>", Catch1)
b2.bind("<Enter>", Catch2)
b3.bind("<Enter>", Catch3)
b4.bind("<Enter>", Catch4)
b5.bind("<Enter>", Catch5)

ev.mainloop()

