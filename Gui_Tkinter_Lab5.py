import tkinter as tk
from tkinter import messagebox as mb

ev = tk.Tk()
ev.title("                                               Tic Tac Toe")

def disable_Buttons():
    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)
    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)
    b6.config(state=tk.DISABLED)
    b7.config(state=tk.DISABLED)
    b8.config(state=tk.DISABLED)
    b9.config(state=tk.DISABLED)

def checkForWin():
    global notComplete
    st1, st2, st3, st4, st5, st6, st7, st8 = '', '', '', '', '', '', '', ''
    for x in range(3):
        st4 = st4 + btchg[x][0]
        st5 = st5 + btchg[x][1]
        st6 = st6 + btchg[x][2]
        if x == 0:
            st7 = st7 + btchg[x][0]
            st8 = st8 + btchg[x][2]
        elif x == 1:
            st7 = st7 + btchg[x][1]
            st8 = st8 + btchg[x][1]
        else:
            st7 = st7 + btchg[x][2]
            st8 = st8 + btchg[x][0]
        for y in range(3):
            if x == 0:
                st1 = st1 + btchg[x][y]
            elif x == 1:
                st2 = st2 + btchg[x][y]
            else:
                st3 = st3 + btchg[x][y]

    if (st1 == 'OOO') or (st2 == 'OOO') or (st3 == 'OOO') or (st4 == 'OOO') or (st5 == 'OOO') or (st6 == 'OOO') or (st7 == 'OOO') or (st8 == 'OOO'):
        mb.showinfo("WINNER", 'YOU WIN !')
        disable_Buttons()
        return

    if (st1 == 'XXX') or (st2 == 'XXX') or (st3 == 'XXX') or (st4 == 'XXX') or (st5 == 'XXX') or (st6 == 'XXX') or (st7 == 'XXX') or (st8 == 'XXX'):
        mb.showinfo("WINNER", 'I WIN !')
        disable_Buttons()
        return

    notComplete = 0
    for i in range(3):
        for j in range(3):
            if btchg[i][j] == 'n':
                notComplete += 1

    if notComplete == 0:
        mb.showinfo("DRAW", 'GAME IS A DRAW !')
        disable_Buttons()
        return

def btn1Click():
    global movecntr, btchg
    if btchg[0][0] == 'O' or btchg[0][0] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b1.config(text='X', fg='red')
            btchg[0][0] = 'X'
        else:
            b1.config(text='O', fg='green')
            btchg[0][0] = 'O'
        movecntr += 1
        checkForWin()

def btn2Click():
    global movecntr, btchg
    if btchg[0][1] == 'O' or btchg[0][1] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b2.config(text='X', fg='red')
            btchg[0][1] = 'X'
        else:
            b2.config(text='O', fg='green')
            btchg[0][1] = 'O'
        movecntr += 1
        checkForWin()

def btn3Click():
    global movecntr, btchg
    if btchg[0][2] == 'O' or btchg[0][2] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b3.config(text='X', fg='red')
            btchg[0][2] = 'X'
        else:
            b3.config(text='O', fg='green')
            btchg[0][2] = 'O'
        movecntr += 1
        checkForWin()

def btn4Click():
    global movecntr, btchg
    if btchg[1][0] == 'O' or btchg[1][0] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b4.config(text='X', fg='red')
            btchg[1][0] = 'X'
        else:
            b4.config(text='O', fg='green')
            btchg[1][0] = 'O'
        movecntr += 1
        checkForWin()

def btn5Click():
    global movecntr, btchg
    if btchg[1][1] == 'O' or btchg[1][1] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b5.config(text='X', fg='red')
            btchg[1][1] = 'X'
        else:
            b5.config(text='O', fg='green')
            btchg[1][1] = 'O'
        movecntr += 1
        checkForWin()

def btn6Click():
    global movecntr, btchg
    if btchg[1][2] == 'O' or btchg[1][2] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b6.config(text='X', fg='red')
            btchg[1][2] = 'X'
        else:
            b6.config(text='O', fg='green')
            btchg[1][2] = 'O'
        movecntr += 1
        checkForWin()

def btn7Click():
    global movecntr, btchg
    if btchg[2][0] == 'O' or btchg[2][0] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b7.config(text='X', fg='red')
            btchg[2][0] = 'X'
        else:
            b7.config(text='O', fg='green')
            btchg[2][0] = 'O'
        movecntr += 1
        checkForWin()

def btn8Click():
    global movecntr, btchg
    if btchg[2][1] == 'O' or btchg[2][1] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b8.config(text='X', fg='red')
            btchg[2][1] = 'X'
        else:
            b8.config(text='O', fg='green')
            btchg[2][1] = 'O'
        movecntr += 1
        checkForWin()

def btn9Click():
    global movecntr, btchg
    if btchg[2][2] == 'O' or btchg[2][2] == 'X':
        mb.showinfo("Box already Clicked", "This box is already used - Use another box")
    else:
        if movecntr % 2 == 0:
            b9.config(text='X', fg='red')
            btchg[2][2] = 'X'
        else:
            b9.config(text='O', fg='green')
            btchg[2][2] = 'O'
        movecntr += 1
        checkForWin()

fnt = 'Times 20 bold'

movecntr = 1
notComplete = 0

btchg = [['n', 'n', 'n'],
         ['n', 'X', 'n'],
         ['n', 'n', 'n']]

b1 = tk.Button(ev, text=" ", font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn1Click)
b1.grid(row=3, column=0)

b2 = tk.Button(ev, text=' ', font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn2Click)
b2.grid(row=3, column=1)

b3 = tk.Button(ev, text=' ',font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn3Click)
b3.grid(row=3, column=2)

b4 = tk.Button(ev, text=' ', font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn4Click)
b4.grid(row=4, column=0)

b5 = tk.Button(ev, text='X', font=fnt, bg='lightskyblue', fg='red', height=4, width=8, command=btn5Click)
b5.grid(row=4, column=1)
b6 = tk.Button(ev, text=' ', font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn6Click)
b6.grid(row=4, column=2)

b7 = tk.Button(ev, text=' ', font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn7Click)
b7.grid(row=5, column=0)

b8 = tk.Button(ev, text=' ', font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn8Click)
b8.grid(row=5, column=1)

b9 = tk.Button(ev, text=' ', font=fnt, bg='lightskyblue', fg='white', height=4, width=8, command=btn9Click)
b9.grid(row=5, column=2)

ev.mainloop()