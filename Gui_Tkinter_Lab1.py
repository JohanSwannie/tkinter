import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
import re

def evaluate_Calculate():
    rv1, rv2 = e1.get(), e2.get()

    specialChar = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if (specialChar.search(rv1) == None):
        if rv1 > ' ':
            if not rv1.isalpha():
                cnt1 = 0
                for dg in rv1:
                    if dg == '.':
                        cnt1 += 1
                if cnt1 > 1:
                    mb.showerror('ERROR', 'Entry field 1 can NOT have more than one floating point !')
                    e1.focus()
                    return
                elif cnt1 == 1:
                    nv1 = float(rv1)
                else:
                    nv1 = int(rv1)
            else:
                mb.showerror('ERROR', 'Entry field 1 should only contain either integers or floats !')
                e1.focus()
                return
        else:
            mb.showerror('ERROR', 'Entry field 1 should not be an empty field !')
            e1.focus()
            return
    else:
        mb.showerror('ERROR', 'Entry field 1 should not have any special characters !')
        e1.focus()
        return

    if (specialChar.search(rv2) == None):
        if rv2 > ' ':
            if not rv2.isalpha():
                cnt2 = 0
                for dg in rv2:
                    if dg == '.':
                        cnt2 += 1
                if cnt2 > 1:
                    mb.showerror('ERROR', 'Entry field 2 can NOT have more than one floating point !')
                    e2.focus()
                    return
                elif cnt2 == 1:
                    nv2 = float(rv2)
                else:
                    nv2 = int(rv2)
            else:
                mb.showerror('ERROR', 'Entry field 2 should only contain either integers or floats !')
                e2.focus()
                return
        else:
            mb.showerror('ERROR', 'Entry field 2 should not be an empty field !')
            e2.focus()
            return
    else:
        mb.showerror('ERROR', 'Entry field 2 should not have any special characters !')
        e2.focus()
        return

    if (str(cVar.get())) == '0':
        er = nv1 + nv2
        addMsg = 'The result of your addition = ' + str(er)
        mb.showinfo('Result', addMsg)
        ar = mb.askquestion("Another Operation", "Do you want to test another operation with these values")
        if ar == 'yes':
            e1.focus()
            return
        else:
            text1.set('')
            text2.set('')
            e1.focus()
            return

    if (str(cVar.get())) == '1':
        er = nv1 - nv2
        subMsg = 'The result of your subtraction = ' + str(er)
        mb.showinfo('Result', subMsg)
        ar = mb.askquestion("Another Operation", "Do you want to test another operation with these values")
        if ar == 'yes':
            e1.focus()
            return
        else:
            text1.set('')
            text2.set('')
            e1.focus()
            return

    if (str(cVar.get())) == '2':
        er = nv1 * nv2
        multMsg = 'The result of your multiplication = ' + str(er)
        mb.showinfo('Result', multMsg)
        ar = mb.askquestion("Another Operation", "Do you want to test another operation with these values")
        if ar == 'yes':
            e1.focus()
            return
        else:
            text1.set('')
            text2.set('')
            e1.focus()
            return

    if (str(cVar.get())) == '3':
        if nv2 == 0:
            mb.showerror('ERROR', 'You can NOT do division by ZERO !!!')
            e1.focus()
            return
        else:
            er = nv1 / nv2
            divMsg = 'The result of your division = ' + str(er)
            mb.showinfo('Result', divMsg)
            ar = mb.askquestion("Another Operation", "Do you want to test another operation with these values")
            if ar == 'yes':
                e1.focus()
                return
            else:
                text1.set('')
                text2.set('')
                e1.focus()
                return

wi = tk.Tk()
wi.geometry("800x700")
wi.title("A Simple Calculator")
wi.config(bg='powderblue')

cVar = tk.IntVar()

rb1 = tk.Radiobutton(wi, text='+', bg='yellow', variable=cVar, value=0)
rb1.config(font=('courier', 12, 'bold'))
rb1.grid(row=0, column=0)
rb1.place(x=380, y=10)
rb2 = tk.Radiobutton(wi, text='-', bg='yellow', variable=cVar, value=1)
rb2.config(font=('courier', 12, 'bold'))
rb2.grid(row=1, column=1)
rb2.place(x=380, y=50)
rb3 = tk.Radiobutton(wi, text='*', bg='yellow', variable=cVar, value=2)
rb3.config(font=('courier', 12, 'bold'))
rb3.grid(row=2, column=2)
rb3.place(x=380, y=90)
rb4 = tk.Radiobutton(wi, text='/', bg='yellow', variable=cVar, value=3)
rb4.config(font=('courier', 12, 'bold'))
rb4.grid(row=3, column=3)
rb4.place(x=380, y=130)

text1 = tk.StringVar()
e1 = tk.Entry(wi, textvariable=text1, width=20, bg='lightgreen')
e1.config(font=('courier', 14, 'bold'))
e1.place(x=140, y=70)

text2 = tk.StringVar()
e2 = tk.Entry(wi, textvariable=text2, width=20, bg='lightgreen')
e2.config(font=('courier', 14, 'bold'))
e2.place(x=440, y=70)

b1 = tk.Button(wi, text='Evaluate', width=10, height=1,
               bg='peach puff', fg='navy', command=evaluate_Calculate)
b1.config(font=('helvetica', 14, 'bold'))
b1.place(x=335, y=180)

wi.mainloop()
