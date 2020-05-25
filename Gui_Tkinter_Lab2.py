import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import random

def Catch(dummy):
    a = random.randint(0, 650)
    b = random.randint(0, 650)
    b1.place(x=a, y=b)

ev = tk.Tk()
ev.title('Catch me if you can')
ev.geometry("900x900")

b1 = tk.Button(ev, text='Catch me if you can', bg='powderblue', fg='navy')
b1.config(font=('courier new', 15, 'bold'))
b1.place(x=20, y=30)
b1.bind("<Enter>", Catch)

ev.mainloop()

