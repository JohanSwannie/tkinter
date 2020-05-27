import tkinter as tk
from tkinter import messagebox as mb
from tkinter import *

def move_ball2():
    global eSpeed, fSpeed, scoreCnt, strSc, player, gameOver
    e1, f1, e2, f2 = canvas.coords(ball2)

    if e1 <= 0 or e2 >= width:
        eSpeed = -eSpeed

    if f1 <= 0:
        fSpeed = -fSpeed
    elif f2 >= keerPlank_y2:
        bmx = (e1 + e2) // 2
        kpe1, _, kpe2, _ = canvas.coords(keerPlank)
        if kpe1 <= bmx <= kpe2:
            fSpeed = -fSpeed
            scoreCnt += 1
        else:
            gameOver = True
            if scoreCnt > 15:
                strSc = 'GAME OVER !!! - Excellent ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            elif scoreCnt > 10:
                strSc = 'GAME OVER !!! - Well Done ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            elif scoreCnt > 5:
                strSc = 'GAME OVER !!! - Not to Bad ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            else:
                strSc = 'GAME OVER !!! - Bad One ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            canvas.create_text((width//2), height//2, text=strSc,
                         font=('helvetica', 24, 'bold'), fill='olive')
            return

    canvas.move(ball2, eSpeed, fSpeed)
    canvas.after(22, move_ball2)

def move_ball():
    global xSpeed, ySpeed, scoreCnt, strSc, saveScore, newSpeed, player, gameOver, nb
    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= width:
        xSpeed = -xSpeed

    if y1 <= 0:
        ySpeed = -ySpeed
    elif y2 >= keerPlank_y2:
        bmx = (x1 + x2) // 2
        kpx1, _, kpx2, _ = canvas.coords(keerPlank)
        if kpx1 <= bmx <= kpx2:
            ySpeed = -ySpeed
            scoreCnt += 1
            saveScore += 1
            if saveScore == 5:
                saveScore = 0
                newSpeed += 0.5
                if newSpeed == 15.5:
                    newSpeed = 7
                if xSpeed < 0:
                    xSpeed = -newSpeed
                else:
                    xSpeed = newSpeed
                if ySpeed < 0:
                    ySpeed = -newSpeed
                else:
                    ySpeed = newSpeed
        else:
            gameOver = True
            if scoreCnt > 15:
                strSc = 'GAME OVER !!! - Excellent ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            elif scoreCnt > 10:
                strSc = 'GAME OVER !!! - Well Done ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            elif scoreCnt > 5:
                strSc = 'GAME OVER !!! - Not to Bad ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            else:
                strSc = 'GAME OVER !!! - Bad One ' + player + ' - Your Final Score is : ' + str(scoreCnt)
            canvas.create_text((width//2), height//2, text=strSc,
                         font=('helvetica', 24, 'bold'), fill='olive')
            return

    canvas.move(ball, xSpeed, ySpeed)

    if scoreCnt > 20:
        if nb == 0:
            nb = 1
            move_ball2()

    canvas.after(22, move_ball)

def keerPlank_regs(event):
    global gameOver
    if gameOver:
        return
    x1, y1, x2, y2 = canvas.coords(keerPlank)
    if x2 < width:
        dx = min(width -x2, 50)
        canvas.move(keerPlank, dx, 0)

def keerPlank_links(event):
    global gameOver
    if gameOver:
        return
    x1, y1, x2, y2 = canvas.coords(keerPlank)
    if x1 > 0:
        dx = min(x1, 50)
        canvas.move(keerPlank, -dx, 0)

def startGame(event=None):
    global player
    player = e1.get()
    e1.config(state='disabled')
    move_ball()

ev = tk.Tk()
ev.title('Johannes and his Bouncing Ball')
ev.geometry("1350x750")

width = 1300
height = 640
eSpeed = fSpeed = 3
xSpeed = ySpeed = 4
newSpeed = 4
scoreCnt = 0
saveScore = 0
strSc = ''
player = ''
nb = 0
gameOver = False

canvas = tk.Canvas(ev, bg='peach puff', width=width, height=height)
canvas.pack()

ball = canvas.create_oval(300, 40, 350, 90, fill='navy', outline='red')
ball2 = canvas.create_oval(550, 40, 600, 90, fill='orange', outline='red')

keerPlank_y = height - 4
keerPlank_y2 = keerPlank_y - 30
keerPlank = canvas.create_rectangle(width//2-50, keerPlank_y, width//2+750, keerPlank_y2, fill='black')

canvas.bind_all("<Button-1>", keerPlank_links)
canvas.bind_all("<Button-3>", keerPlank_regs)
canvas.bind_all("<Left>", keerPlank_links)
canvas.bind_all("<Right>", keerPlank_regs)
canvas.bind_all("<z>", keerPlank_links)
canvas.bind_all("<m>", keerPlank_regs)

etv = tk.StringVar()
etv.set('')

e1 = tk.Entry(ev, textvariable=etv, width=30, bg='peach puff', font=('courier', 18, 'bold'))
e1.place(x=420, y=670)
e1.focus()
e1.bind("<Return>", startGame)

b1 = tk.Button(ev, text='Quit Game', bg='peach puff', fg='blue', width=10, height=2, command=ev.destroy)

l1 = tk.Label(ev, text='Please enter Your Name to start the game', font=('arial', 14, 'bold'))
l1.place(x=10, y=670)
b1.place(x=1200, y=670)

ev.mainloop()
