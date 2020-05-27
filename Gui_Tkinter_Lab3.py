import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *
import random

def startTime():
    global s, f
    s += 1
    b26.config(text=s)
    if ac == 25:
        wi.after_cancel(startTime)
        m = s / 60
        if int(m) > 1:
            md = 'minutes'
        else:
            md = 'minute'
        if int(m) > 0:
            r = s % 60
            f = "Completed time =  " + str(int(m)) + "  " + md + "  and   " + str(r) + "  Seconds"
        else:
            f = "Completed time =  " + str(s) + "  Seconds"
        b28.config(text=f)
    else:
        wi.after(1000, startTime)

def clickButton(event=None):
    global lst3, t, ac
    if t == 0:
        wi.after(1000, startTime)
        t = 1
    if ac < 25:
        btn = event.widget
        cv = (btn.cget("text"))
        if cv == lst3[0]:
            del lst3[0]
            btn.config(bg='lightgray')
            btn.config(font=('helvetica', 7, 'bold'))
            btn["text"] = 'YES'
            btn["state"] = DISABLED
            ac += 1

def getNum():
    global lst1
    r=0
    c=0
    for x in range(0, 25):
        bt = random.randint(0, 999)
        b1 = tk.Button(wi, text='', width=28, height=8, bg='peach puff')
        b1.grid(row=r, column=c)
        b1.config(text=bt)
        b1.bind("<Button-1>", clickButton)
        rn = int(bt)
        lst1.append(rn)
        c += 1
        if c == 5:
            r += 1
            c = 0

wi = tk.Tk()
wi.geometry("1030x900")
wi.title('Click Me')
wi.config(bg='powderblue')

ac = 0
s = 0
t = 0
f = ''

lst1 = []
getNum()
lst3 = sorted(lst1)

l1 = tk.Label(wi, text='Clock in Seconds :', fg='black', bg='powderblue',
              font=('new courier', 11, 'bold'))
l1.place(x=100, y=675)

b26 = tk.Label(wi, text=s, fg='black', bg='yellow', width=10, height=2)
b26.place(x=248, y=660)

b27 = tk.Label(wi, text='The aim of this game is to click from the lowest to the highest numbers on the board',
                        fg='black', bg='powderblue', font=('new courier', 16, 'bold'))
b27.place(x=10, y=740)


b28 = tk.Label(wi, text=f, fg='navy', bg='powderblue', width=68, height=3)
b28.place(x=330, y=660)
b28.config(font=('helvetica', 14, 'bold'))

wi.mainloop()

