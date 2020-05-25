import tkinter as tk
from tkinter import *

def control_Traffic():
    global a, b, c, i, phases, phase
    if phase == 0:
        i = 'Light is RED - Wait !!!'
    elif phase == 1:
        i = 'Light is RED + ORANGE - Still Wait !!! - It will turn green soon'
    elif phase == 2:
        i = 'Light is GREEN - You can GO now'
    elif phase == 3:
        i = 'Light is ORANGE - Prepare now because light will soon turn RED !!!'
    l1.config(text=i)
    if phases[phase][0] == True:
        a = 'red'
    else:
        a = 'lightgray'
    canvas.create_oval(319, 68, 400, 148, fill=a)
    if phases[phase][1] == True:
        b = 'orange'
    else:
        b = 'lightgray'
    canvas.create_oval(319, 168, 400, 248, fill=b)
    if phases[phase][2] == True:
        c = 'green'
    else:
        c = 'lightgray'
    canvas.create_oval(319, 268, 400, 348, fill=c)
    phase += 1
    if phase == 4:
        phase = 0

ev = tk.Tk()
ev.title("Traffic Lights")
ev.geometry("750x700")
canvas = tk.Canvas(ev, width=750, height=750, bg='peach puff')

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))

a, b, c = 'red', 'lightgray', 'lightgray'
phase = 1
i = 'Light is RED - Wait !!!'

canvas.create_oval(319, 68, 400, 148, fill=a)
canvas.create_oval(319, 168, 400, 248, fill=b)
canvas.create_oval(319, 268, 400, 348, fill=c)

l1 = tk.Label(ev, text=i, bg='peach puff', fg='black')
l1.place(x=100, y=400)
l1.config(font=('new courier', 14, 'bold'))

b1 = tk.Button(ev, text='Next', bg='pink', fg='navy', width=10, height=2, command=control_Traffic)
b1.place(x=325, y=460)

b2 = tk.Button(ev, text='Quit', bg='pink', fg='navy', width=10, height=2, command=ev.destroy)
b2.place(x=325, y=520)

canvas.grid(row=0)

ev.mainloop()