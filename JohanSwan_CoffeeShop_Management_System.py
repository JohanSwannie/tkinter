import tkinter as tk
from tkinter import *
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import os
import hashlib
import time
import random

operator = ""

class CoffeeShop_Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("1500x800")
        self.title("Swannie's Coffee Shop Management System")

        utility = tk.Frame(self)
        # self.attributes("-fullscreen", True)
        utility.pack(side="top", fill="both", expand=True)

        utility.grid_rowconfigure(0, weight=1)
        utility.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for A in (login_Page, change_Password, add_Users, choice_Menu,
                  coffeeShop_Billing, coffeeShop_PriceChange):
            application_Name = A.__name__
            frame = A(parent=utility, controller=self)
            self.frames[application_Name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("login_Page")

    def show_frame(self, application_Name):
        '''Show a frame for the given page name'''
        frame = self.frames[application_Name]
        frame.tkraise()

class login_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self)
        img = Image.open("Restaurant5.jpg")
        img = img.resize((1500, 800), Image.ANTIALIAS)
        label.img = ImageTk.PhotoImage(img)
        label['image'] = label.img
        label.pack()

        def confirm():
            global user_Okay, userYes
            un = userName.get()
            pw = passWord.get()

            user_Okay = True
            userYes, userComplete = False, False

            if un > "" and len(un) > 9:
                if pw > "" and len(pw) > 9:
                    user_Okay = True
                else:
                    mb.showinfo('Error', 'Password must be at least 10 characters - Please Try again')
                    passWord.set("")
                    entry2.focus_set()
                    user_Okay = False
            else:
                mb.showinfo('Error', 'Username must be at least 10 characters - Please Try again')
                userName.set("")
                entry1.focus_set()
                user_Okay = False

            if user_Okay:
                try:
                    userYes = False
                    with open("CoffeeShop_Users.txt", "r") as rpsw:
                        recs = rpsw.lines()
                        for line in recs:
                            if line.find(un) != -1:
                                if line.find(pw) != -1:
                                    userYes = True
                        userComplete = True
                except Exception as err:
                    errMsg = str(err) + ' - Please try again or phone Johan Swan to fix this error'
                    mb.showinfo('Error', errMsg)
                    userName.set("")
                    passWord.set("")
                    entry1.focus_set()

            if userComplete:
                if userYes:
                    mb.showinfo('Authorized',
                                'You are authorised to perform this function - Click "Billing / Price Menu" to continue')
                    userName.set("")
                    passWord.set("")
                    entry1['state'] = DISABLED
                    entry2['state'] = DISABLED
                    enter_btn['state'] = DISABLED
                    choiceMenu_Button['state'] = NORMAL
                else:
                    mb.showinfo('NOT authorized',
                                'You are NOT authorised to perform this function - Re-enter Username and Password')
                    userName.set("")
                    passWord.set("")
                    entry1.focus_set()

        def signOut():
            userName.set("")
            passWord.set("")
            entry1['state'] = NORMAL
            entry1.focus_set()
            entry2['state'] = NORMAL
            enter_btn['state'] = NORMAL
            choiceMenu_Button['state'] = DISABLED

        userName = StringVar()
        passWord = StringVar()

        label = tk.Label(self, text="Swannie's Coffee Shop - Login Page", fg='white', bg='steel blue',
                         font=('arial', 30, 'bold', 'italic'), padx=2, pady=2,
                         height=1, width=30, bd=10, highlightthickness=10)
        label.place(x=380, y=40)

        label1 = tk.Label(self, text="Please Enter Your Username", font=('slant', 15, 'bold'),
                          bg='powderblue', width=23, bd=10, highlightthickness=10)
        label1.place(x=82, y=180)

        label2 = tk.Label(self, text="Please Enter Your Password", font=('slant', 15, 'bold'),
                          bg='powderblue', widt=23, bd=10, highlightthickness=10)

        label2.place(x=82, y=270)

        entry1 = tk.Entry(self, textvariable=userName, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry1.place(x=420, y=205)
        entry1.focus_set()

        entry2 = tk.Entry(self, textvariable=passWord, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry2.place(x=420, y=295)
        entry2.config(show='*')

        enter_btn = tk.Button(self, text="Confirm", bg='steel blue', font=('helvetica', 12, 'bold'),
                              padx=14, pady=14, height=1, width=20, bd=10,
                              highlightthickness=10, command=confirm)
        enter_btn.place(x=100, y=360)

        pwch_Button = tk.Button(self, text="Change Password", font=('helvetica', 12, 'bold'),
                                fg='black', bg='tomato', bd=10, highlightthickness=10,
                                padx=14, pady=14, height=1, width=20,
                                command=lambda: controller.show_frame("change_Password"))
        pwch_Button.place(x=100, y=470)

        addUsers_Button = tk.Button(self, text="Add Users", font=('helvetica', 12, 'bold'),
                                    fg='black', bg='khaki1', bd=10, highlightthickness=10,
                                    padx=14, pady=14, height=1, width=20,
                                    command=lambda: controller.show_frame("add_Users"))
        addUsers_Button.place(x=100, y=580)

        choiceMenu_Button = tk.Button(self, text="Billing / Price\nMenu", font=('helvetica', 12, 'bold'),
                                    fg='black', bg='MediumOrchid1', bd=10, highlightthickness=10,
                                    padx=14, pady=14, height=2, width=20,
                                    command=lambda: controller.show_frame("choice_Menu"))
        choiceMenu_Button.place(x=1168, y=200)
        choiceMenu_Button['state'] = DISABLED


        signOut_Button = tk.Button(self, text="Sign Out", font=('helvetica', 12, 'bold'),
                                    fg='black', bg='gold', bd=10, highlightthickness=10,
                                    padx=14, pady=14, height=1, width=20, command=signOut)
        signOut_Button.place(x=1168, y=635)

        image2 = Image.open("flowers5.jpg")
        image2 = image2.resize((49, 49), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)

        p1 = 2
        p2 = 2

        for p in range(16):
            phLabel2 = tk.Label(self, image=photo2)
            phLabel2.place(x=p1, y=p2)
            p2 += 50

        p3 = 1450
        p4 = 2

        for p in range(16):
            phLabel2 = tk.Label(self, image=photo2)
            phLabel2.place(x=p3, y=p4)
            p4 += 50

        p5 = 52
        p6 = 1

        for p in range(28):
            phLabel2 = tk.Label(self, image=photo2)
            phLabel2.place(x=p5, y=p6)
            p5 += 50

        p7 = 52
        p8 = 740

        for p in range(28):
            phLabel2 = tk.Label(self, image=photo2)
            phLabel2.place(x=p7, y=p8)
            p7 += 50

class change_Password(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self)
        img = Image.open("changepassword.jpg")
        img = img.resize((1500, 800), Image.ANTIALIAS)
        label.img = ImageTk.PhotoImage(img)
        label['image'] = label.img
        label.pack()

        def confirm():
            global auth_Okay, authYes, saveUser, savePassword

            cn = coffee_User.get()
            opw = old_passWord.get()

            auth_Okay = True
            authYes, authComplete = False, False

            if cn > "" and len(cn) > 9:
                if opw > "" and len(opw) > 9:
                    auth_Okay = True
                else:
                    mb.showinfo('Error', 'Password must be at least 10 characters - Please Try again')
                    old_passWord.set("")
                    entry2.focus_set()
                    auth_Okay = False
            else:
                mb.showinfo('Error', 'Username must be at least 10 characters - Please Try again')
                coffee_User.set("")
                entry1.focus_set()
                auth_Okay = False

            if auth_Okay:
                try:
                    authYes = False
                    with open("CoffeeShop_Users.txt", "r") as rpsw:
                        recs = rpsw.readlines()
                        for line in recs:
                            if line.find(cn) != -1:
                                if line.find(opw) != -1:
                                    authYes = True
                        authComplete = True
                except Exception as err:
                    errMsg = str(err) + ' - Please try again or phone Johan Swan to fix this error'
                    mb.showinfo('Error', errMsg)
                    coffee_User.set("")
                    old_passWord.set("")
                    entry1.focus_set()

            if authComplete:
                if authYes:
                    saveUser = cn
                    savePassword = opw
                    mb.showinfo('Correct Detail',
                                'Username - Password combination correct - go ahead and change your Password')
                    coffee_User.set("")
                    old_passWord.set("")
                    entry1['state'] = DISABLED
                    entry2['state'] = DISABLED
                    enter_btn['state'] = DISABLED
                    entry3['state'] = NORMAL
                    enter2_btn['state'] = NORMAL
                    entry3.focus_set()
                else:
                    mb.showinfo('Incorrect Detail', 'Username - Password combination Incorrect - Please try again')
                    coffee_User.set("")
                    old_passWord.set("")
                    entry1.focus_set()

        def change():

            global pw_special, pw_diGits, user_Okay, pw_alPhas
            global saveUser, oldCombo, newCombo, savePassword

            pw_special, pw_diGits, pw_alPhas = False, False, False
            user_Okay = True

            special_Chars = '!@#$%^&*()_+=-_[]{}\|;:/?.>,<'
            numeRics = '1234567890'
            alphaBetics = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

            pw = new_passWord.get()

            if pw > "":
                for ch1 in pw:
                    for ch2 in special_Chars:
                        if ch1.find(ch2) != -1:
                            pw_special = True
                for ch1 in pw:
                    for ch2 in numeRics:
                        if ch1.find(ch2) != -1:
                            pw_diGits = True
                for ch1 in pw:
                    for ch2 in alphaBetics:
                        if ch1.find(ch2) != -1:
                            pw_alPhas = True
                if len(pw) < 10:
                    mb.showinfo('Error', 'Password must be at least 10 characters - Please Try again')
                    passWord.set("")
                    entry2.focus_set()
                    user_Okay = False
                elif not pw_diGits:
                    mb.showinfo('Error', 'Password must have at least 1 Numeric digit - Please try again')
                    passWord.set("")
                    entry2.focus_set()
                    user_Okay = False
                elif not pw_alPhas:
                    mb.showinfo('Error', 'Password must have at least 1 Alpabetic character - Please try again')
                    passWord.set("")
                    entry2.focus_set()
                    user_Okay = False
                elif not pw_special:
                    mb.showinfo('Error', 'Password must have at least 1 special character - Please try again')
                    passWord.set("")
                    entry2.focus_set()
                    user_Okay = False
            else:
                mb.showinfo('Error', 'Please enter your Password')
                passWord.set("")
                entry2.focus_set()
                user_Okay = False

            if user_Okay:
                try:
                    oldCombo = str(saveUser) + str(savePassword)
                    newCombo = str(saveUser) + str(pw)
                    with open("CoffeeShop_Users.txt", "rt") as ruser:
                        data = ruser.read()
                        data = data.replace(oldCombo, newCombo)
                    with open("CoffeeShop_Users.txt", "wt") as wuser:
                        wuser.write(data)
                    mb.showinfo('Success',
                                'Password Successfully Changed - Click "Change another Password" or CLICK "Back to Login"')
                    new_passWord.set("")
                    entry3['state'] = DISABLED
                    enter2_btn['state'] = DISABLED
                    enter3_btn['state'] = NORMAL
                except Exception as err:
                    errMsg = str(err) + ' - Please try again or phone Johan Swan to fix this error'
                    mb.showinfo('Error', errMsg)
                    new_passWord.set("")
                    entry3.focus_set()

        def change_Another():
            entry1['state'] = NORMAL
            entry1.focus_set()
            entry2['state'] = NORMAL
            enter_btn['state'] = NORMAL
            entry3['state'] = DISABLED
            enter2_btn['state'] = DISABLED
            enter3_btn['state'] = DISABLED

        coffee_User = StringVar()
        old_passWord = StringVar()
        new_passWord = StringVar()

        un_special, pw_special, un_diGits = False, False, False
        un_alPhas, pw_diGits, pw_alPhas, user_Okay, auth_Okay = False, False, False, False, False

        saveUser = ""
        savePassword = ""
        oldCombo = ""
        newCombo = ""

        label = tk.Label(self, text="Swannie's Coffee Shop - Change Password", fg='white', bg='steel blue',
                         font=('arial', 30, 'bold', 'italic'), padx=2, pady=2,
                         height=1, width=38, bd=10, highlightthickness=10)
        label.place(x=270, y=1)

        label1 = tk.Label(self, text="Please Enter Username", font=('slant', 14, 'bold'),
                          bg='powderblue', width=23, bd=10, highlightthickness=10)
        label1.place(x=82, y=195)

        label2 = tk.Label(self, text="Please Enter Old Password", font=('slant', 14, 'bold'),
                          bg='powderblue', widt=23, bd=10, highlightthickness=10)

        label2.place(x=82, y=290)

        label3 = tk.Label(self, text="Please Enter New Password", font=('slant', 14, 'bold'),
                          bg='powderblue', widt=23, bd=10, highlightthickness=10)

        label3.place(x=82, y=385)

        entry1 = tk.Entry(self, textvariable=coffee_User, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry1.place(x=420, y=220)
        entry1.focus_set()

        entry2 = tk.Entry(self, textvariable=old_passWord, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry2.place(x=420, y=310)
        entry2.config(show='*')

        entry3 = tk.Entry(self, textvariable=new_passWord, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry3.place(x=420, y=400)
        entry3.config(show='*')
        entry3['state'] = DISABLED

        enter_btn = tk.Button(self, text="Confirm\nOld Password", bg='steel blue',
                              font=('helvetica', 12, 'bold'), width=16, height=3, bd=3,
                              highlightthickness=3, command=confirm)
        enter_btn.place(x=830, y=230)

        enter2_btn = tk.Button(self, text="Confirm\nNew Password", bg='steel blue', font=('helvetica', 12, 'bold'),
                               width=16, height=3, bd=3, highlightthickness=3, command=change)
        enter2_btn.place(x=830, y=360)
        enter2_btn['state'] = DISABLED

        enter3_btn = tk.Button(self, text="Change Another\nPassword", bg='tomato', font=('helvetica', 12, 'bold'),
                               width=16, height=3, bd=3, highlightthickness=3, command=change_Another)
        enter3_btn.place(x=830, y=490)
        enter3_btn['state'] = DISABLED

        exit_btn2 = tk.Button(self, padx=1, text="Back to Login", bg='salmon', font=('helvetica', 12, 'bold'),
                             width=16, height=3, bd=3, highlightthickness=3,
                             command = lambda: controller.show_frame("login_Page"))
        exit_btn2.place(x=830, y=620)

class add_Users(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self)
        img = Image.open("Password01.jpg")
        img = img.resize((1500, 800), Image.ANTIALIAS)
        label.img = ImageTk.PhotoImage(img)
        label['image'] = label.img
        label.pack()

        def confirm():
            global auth_Okay, authYes

            an = authName.get()
            apw = authPassword.get()

            auth_Okay = True
            authYes, authComplete = False, False

            if an > "" and len(an) > 9:
                if apw > "" and len(apw) > 9:
                    auth_Okay = True
                else:
                    mb.showinfo('Error', 'Password must be at least 10 characters - Please Try again')
                    authPassword.set("")
                    entry2.focus_set()
                    auth_Okay = False
            else:
                mb.showinfo('Error', 'Username must be at least 10 characters - Please Try again')
                authName.set("")
                entry1.focus_set()
                auth_Okay = False

            if auth_Okay:
                try:
                    authYes = False
                    with open("CoffeeShop_Users.txt", "r") as rpsw:
                        recs = rpsw.readlines()
                        for line in recs:
                            if line.find(an) != -1:
                                if line.find(apw) != -1:
                                    authYes = True
                        authComplete = True
                except Exception as err:
                    errMsg = str(err) + ' - Please try again or phone Johan Swan to fix this error'
                    mb.showinfo('Error', errMsg)
                    authName.set("")
                    authPassword.set("")
                    entry1.focus_set()

            if authComplete:
                if authYes:
                    mb.showinfo('Authorized', 'You are authorised to perform this function - go ahead')
                    authName.set("")
                    authPassword.set("")
                    entry1['state'] = DISABLED
                    entry2['state'] = DISABLED
                    confrm_btn['state'] = DISABLED
                    entry3['state'] = NORMAL
                    entry4['state'] = NORMAL
                    enter_btn['state'] = NORMAL
                    entry3.focus_set()
                else:
                    mb.showinfo('NOT authorized',
                                'You are NOT authorised to perform this function - Re-enter Username and Password')
                    authName.set("")
                    authPassword.set("")
                    entry1.focus_set()

        def enter():

            global un_special, pw_special, un_diGits, un_alPhas, pw_diGits, user_Okay
            global pw_alPhas, users_Dict

            un_special, pw_special, un_diGits = False, False, False
            un_alPhas, pw_diGits, pw_alPhas = False, False, False
            user_Okay = True

            special_Chars = '!@#$%^&*()_+=-_[]{}\|;:/?.>,<'
            numeRics = '1234567890'
            alphaBetics = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

            un = userName.get()
            pw = passWord.get()
            print('special chars is :', special_Chars)

            if un > "":
                for ch1 in un:
                    for ch2 in special_Chars:
                        if ch1.find(ch2) != -1:
                            un_special = True
                for ch1 in un:
                    for ch2 in numeRics:
                        if ch1.find(ch2) != -1:
                            un_diGits = True
                for ch1 in un:
                    for ch2 in alphaBetics:
                        if ch1.find(ch2) != -1:
                            un_alPhas = True
                if pw > "":
                    for ch1 in pw:
                        for ch2 in special_Chars:
                            if ch1.find(ch2) != -1:
                                pw_special = True
                    for ch1 in pw:
                        for ch2 in numeRics:
                            if ch1.find(ch2) != -1:
                                pw_diGits = True
                    for ch1 in pw:
                        for ch2 in alphaBetics:
                            if ch1.find(ch2) != -1:
                                pw_alPhas = True
                    if len(un) < 10:
                        mb.showinfo('Error', 'Username must be at least 10 characters - Please Try again')
                        userName.set("")
                        entry3.focus_set()
                        user_Okay = False
                    elif not un_diGits:
                        mb.showinfo('Error', 'Username must have at least one Numeric digit - Please try again')
                        userName.set("")
                        entry3.focus_set()
                        user_Okay = False
                    elif not un_alPhas:
                        mb.showinfo('Error', 'Username must have at least one Alpabetic character - Please try again')
                        userName.set("")
                        entry3.focus_set()
                        user_Okay = False
                    elif not un_special:
                        mb.showinfo('Error', 'Username must have at least 1 special character - Please try again')
                        userName.set("")
                        entry3.focus_set()
                        user_Okay = False
                    elif len(pw) < 10:
                        mb.showinfo('Error', 'Password must be at least 10 characters - Please Try again')
                        passWord.set("")
                        entry4.focus_set()
                        user_Okay = False
                    elif not pw_diGits:
                        mb.showinfo('Error', 'Password must have at least 1 Numeric digit - Please try again')
                        passWord.set("")
                        entry4.focus_set()
                        user_Okay = False
                    elif not pw_alPhas:
                        mb.showinfo('Error', 'Password must have at least 1 Alpabetic character - Please try again')
                        passWord.set("")
                        entry4.focus_set()
                        user_Okay = False
                    elif not pw_special:
                        mb.showinfo('Error', 'Password must have at least 1 special character - Please try again')
                        passWord.set("")
                        entry4.focus_set()
                        user_Okay = False
                else:
                    mb.showinfo('Error', 'Please enter your Password')
                    passWord.set("")
                    entry4.focus_set()
                    user_Okay = False
            else:
                mb.showinfo('Error', 'Please enter your User Name')
                userName.set("")
                entry3.focus_set()
                user_Okay = False

            if user_Okay:
                try:
                    users = ""
                    users = users + str(un) + str(pw) + '\n'
                    with open("CoffeeShop_Users.txt", "a+") as psw:
                        psw.write(users)
                    q1 = mb.askquestion('Success', 'User successfully added, do you want to add another user?')
                    if q1 == 'yes':
                        mb.showinfo('Another User', 'Please Enter Another User')
                        userName.set("")
                        passWord.set("")
                        entry3.focus_set()
                    else:
                        mb.showinfo('Click Back to Login',
                                    'Click "Back to Login" or if the need be then Add Another User')
                        userName.set("")
                        passWord.set("")
                        entry3.focus_set()
                except Exception as err:
                    errMsg = str(err) + ' - Please try again or phone Johan Swan to fix this error'
                    mb.showinfo('Error', errMsg)
                    userName.set("")
                    passWord.set("")
                    entry3.focus_set()

        authName = StringVar()
        authPassword = StringVar()

        userName = StringVar()
        passWord = StringVar()

        un_special, pw_special, un_diGits = False, False, False
        un_alPhas, pw_diGits, pw_alPhas, user_Okay, auth_Okay = False, False, False, False, False

        label = tk.Label(self, text="Swannie's Coffee Shop - Add Users", fg='white', bg='steel blue',
                         font=('arial', 30, 'bold', 'italic'), padx=2, pady=2,
                         height=1, width=34, bd=10, highlightthickness=10)
        label.place(x=340, y=1)

        label1 = tk.Label(self, text="Please Enter Authorised Username", font=('slant', 13, 'bold'),
                          bg='powderblue', width=28, bd=10, highlightthickness=10)
        label1.place(x=82, y=200)

        label2 = tk.Label(self, text="Please Enter Authorised Password", font=('slant', 13, 'bold'),
                          bg='powderblue', widt=28, bd=10, highlightthickness=10)

        label2.place(x=82, y=290)

        entry1 = tk.Entry(self, textvariable=authName, width=40, bg='peach puff',
                          font=('helvetica', 10, 'bold'))
        entry1.place(x=420, y=220)
        entry1.focus_set()

        entry2 = tk.Entry(self, textvariable=authPassword, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry2.place(x=420, y=310)
        entry2.config(show='*')

        confrm_btn = tk.Button(self, text="CONFIRM Authorisation", bg='steel blue', font=('helvetica', 12, 'bold'),
                               width=20, height=3, bd=3, highlightthickness=3, command=confirm)
        confrm_btn.place(x=850, y=170)

        label3 = tk.Label(self, text="Please Enter New Username", font=('slant', 14, 'bold'),
                          bg='powderblue', width=23, bd=10, highlightthickness=10)
        label3.place(x=82, y=480)

        label4 = tk.Label(self, text="Please Enter New Password", font=('slant', 14, 'bold'),
                          bg='powderblue', widt=23, bd=10, highlightthickness=10)

        label4.place(x=82, y=570)

        entry3 = tk.Entry(self, textvariable=userName, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry3.place(x=420, y=500)
        entry3['state'] = DISABLED

        entry4 = tk.Entry(self, textvariable=passWord, width=40, bg='peach puff', font=('helvetica', 10, 'bold'))
        entry4.place(x=420, y=590)
        entry4.config(show='*')
        entry4['state'] = DISABLED

        enter_btn = tk.Button(self, text="CONFIRM", bg='steel blue', font=('helvetica', 12, 'bold'),
                              width=16, height=3, bd=3, highlightthickness=3, command=enter)
        enter_btn.place(x=740, y=650)
        enter_btn['state'] = DISABLED

        exit_btn3 = tk.Button(self, padx=1, text="Back to Login", bg='salmon', font=('helvetica', 12, 'bold'),
                             width=16, height=3, bd=3, highlightthickness=3,
                             command=lambda: controller.show_frame("login_Page"))
        exit_btn3.place(x=940, y=650)


class choice_Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self)
        img = Image.open("menu.jpg")
        img = img.resize((1500, 800), Image.ANTIALIAS)
        label.img = ImageTk.PhotoImage(img)
        label['image'] = label.img
        label.pack()

        cLabel = tk.Label(self, text="Swannie's Coffee Shop - Price / Billing Menu", fg='white',
                          bg='steel blue', font=('arial', 30, 'bold', 'italic'), padx=2, pady=2,
                         height=1, width=34, bd=10, highlightthickness=10)
        cLabel.place(x=310, y=1)

        button1 = tk.Button(self, text="For Coffee Shop Billing Click Here", font=('arial', 15, 'bold'),
                            fg='olive', bg='gold', bd=18, highlightthickness=10,
                            padx=28, pady=28, height=1, width=29,
                            command = lambda: controller.show_frame("coffeeShop_Billing"))

        button1.place(x=500, y=160)

        button2 = tk.Button(self, text="For Coffee Shop Price Changes Click Here", font=('arial', 15, 'bold'),
                            fg='olive', bg='pale turquoise1', bd=18, highlightthickness=10,
                            padx=28, pady=28, height=1, width=29,
                            command = lambda: controller.show_frame("coffeeShop_PriceChange"))
        button2.place(x=500, y=360)

        cBtn_back = Button(self, padx=28, pady=28, bd=16, fg="black", font=('arial', 15, 'bold'),
                          width=31, text="Back to Login", bg="salmon",
                          command = lambda: controller.show_frame("login_Page"))
        cBtn_back.place(x=500, y=560)


class coffeeShop_Billing(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label10 = tk.Label(self)
        img = Image.open("billing.jpg")
        img = img.resize((1500, 800), Image.ANTIALIAS)
        label10.img = ImageTk.PhotoImage(img)
        label10['image'] = label10.img
        label10.place(x=1, y=1)

        def btn_click(number):
            global operator
            operator = operator + str(number)
            calc_txt_inp.set(operator)

        def fun_clear():
            global operator
            operator = ""
            calc_txt_inp.set(operator)

        def calculate():
            global operator
            try:
                sumup = str(eval(operator))
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                sumup = 0
                fun_clear()
            calc_txt_inp.set(sumup)
            operator = ""

        def ref():
            f1 = open('value.txt', 'r')
            line = f1.readlines()
            Flat_White_Price = float(line[0])
            Latte_Price = float(line[1])
            Cappuccino_Price = float(line[2])
            Espresso_p = float(line[3])
            Long_Black_Price = float(line[4])
            Mocha_Price = float(line[5])
            Macchiato_Price = float(line[6])
            f1.close()

            try:
                if Flat_White_Input_Price.get() == "":
                    CoF = 0
                else:
                    CoF = float(Flat_White_Input_Price.get()) * Flat_White_Price
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                Flat_White_Input_Price.set("")

            try:
                if Latte_Input_Price.get() == "":
                    CoS = 0
                else:
                    CoS = float(Latte_Input_Price.get()) * Latte_Price
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                Latte_Input_Price.set("")

            try:
                if Cappuccino_Input_Price.get() == "":
                    CoB = 0
                else:
                    CoB = float(Cappuccino_Input_Price.get()) * Cappuccino_Price
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                Cappuccino_Input_Price.set("")

            try:
                if Espresso_Input_Price .get() == "":
                    CoD = 0
                else:
                    CoD = float(Espresso_Input_Price.get()) * Espresso_p
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                Espresso_Input_Price.set("")

            try:
                if Long_Black_Input_Price .get() == "":
                    CoP = 0
                else:
                    CoP = float(Long_Black_Input_Price.get()) * Long_Black_Price
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                Long_Black_Input_Price.set("")

            try:
                if Mocha_Input_Price .get() == "":
                    CoP = 0
                else:
                    CoP = float(Mocha_Input_Price.get()) * Mocha_Price
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                Mocha_Input_Price.set("")

            try:
                if Macchiato_Input_Price .get() == "":
                    CoC = 0
                else:
                    CoC = float(Macchiato_Input_Price .get()) * Macchiato_Price
            except Exception as e:
                mb.showinfo('Error', 'Incorrect Input')
                Macchiato_Input_Price .set("")

            CostOfMeal = (CoF + CoS + CoB + CoD + CoP + CoC)

            PayTax = (CostOfMeal) * 0.09
            ServiceCharge = (CostOfMeal) * 0.03
            totalTax = PayTax + ServiceCharge
            totalCost = (CostOfMeal + PayTax + ServiceCharge)

            services_inp.set(str('%.2f' % (ServiceCharge)))
            tax_inp.set(str('%.2f' % (PayTax)))
            subtotal_inp.set(str('%.2f' % (CostOfMeal)))
            total_inp.set(str('%.2f' % (totalCost)))
            cost_inp.set(str('%.2f' % (totalTax)))

        def reset():
            Flat_White_Input_Price.set("")
            Latte_Input_Price.set("")
            Cappuccino_Input_Price .set("")
            Espresso_Input_Price .set("")
            total_inp.set("")
            subtotal_inp.set("")
            services_inp.set("")
            tax_inp.set("")
            cost_inp.set("")
            Long_Black_Input_Price .set("")
            Mocha_Input_Price .set("")
            Macchiato_Input_Price .set("")

        operator = ""

        left = Frame(self, width=800, height=700, bg='deep sky blue', relief=SUNKEN)
        left.pack(side=LEFT)

        right = Frame(self, width=300, height=700, bg='deep sky blue', relief=SUNKEN)
        right.pack(side=RIGHT)

        label_info = Label(self, font=('arial', 40, 'bold'),
                           text="Swannie's Coffee Shop Billing System",
                           bg='deep sky blue', fg="navy", bd=10)
        label_info.place(x=340, y=5)

        local_time = time.asctime(time.localtime(time.time()))

        time_Text = 'Time : ' + local_time[0:3] + ' - ' + local_time[8:10] + ' '\
                    + local_time[4:8] + local_time[20:25] + ' - ' + local_time[11:20]
        
        label_info = Label(self, font=('arial', 25, 'bold'), text=time_Text,
                           bg='deep sky blue', fg="navy", bd=10)
        label_info.place(x=490, y=80)

        calc_txt_inp = StringVar()

        calc_txt = Entry(right, font=('arial', 20, 'bold'), textvariable=calc_txt_inp,
                         bd=18, insertwidth=4, bg="powderblue", justify='right')
        calc_txt.grid(columnspan=4)

        btn7 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="7", bg="powder blue", command=lambda: btn_click(7))
        btn7.grid(row=2, column=0)

        btn8 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="8", bg="powder blue", command=lambda: btn_click(8))
        btn8.grid(row=2, column=1)

        btn9 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="9", bg="powder blue", command=lambda: btn_click(9))
        btn9.grid(row=2, column=2)

        plus = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="+", bg="powder blue", command=lambda: btn_click("+"))
        plus.grid(row=2, column=3)

        btn4 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="4", bg="powder blue", command=lambda: btn_click(4))
        btn4.grid(row=3, column=0)

        btn5 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="5", bg="powder blue", command=lambda: btn_click(5))
        btn5.grid(row=3, column=1)

        btn6 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="6", bg="powder blue", command=lambda: btn_click(6))
        btn6.grid(row=3, column=2)

        minus = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                       text="-", bg="powder blue", command=lambda: btn_click("-"))
        minus.grid(row=3, column=3)

        btn1 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="1", bg="powder blue", command=lambda: btn_click(1))
        btn1.grid(row=4, column=0)

        btn2 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="2", bg="powder blue", command=lambda: btn_click(2))
        btn2.grid(row=4, column=1)

        btn3 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="3", bg="powder blue", command=lambda: btn_click(3))
        btn3.grid(row=4, column=2)

        multi = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                       text="*", bg="powder blue", command=lambda: btn_click("*"))
        multi.grid(row=4, column=3)

        btn0 = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="0", bg="powder blue",
                      command=lambda: btn_click(0))
        btn0.grid(row=5, column=0)

        btn_clear = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="C",
                           bg="powder blue",
                           command=fun_clear)
        btn_clear.grid(row=5, column=1)

        btn_equal = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="=",
                           bg="powder blue",
                           command=calculate)
        btn_equal.grid(row=5, column=2)

        division = Button(right, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'), text="/",
                          bg="powder blue",
                          command=lambda: btn_click("/"))
        division.grid(row=5, column=3)

        Flat_White_Input_Price = StringVar()
        Latte_Input_Price = StringVar()
        Cappuccino_Input_Price  = StringVar()
        Espresso_Input_Price  = StringVar()
        total_inp = StringVar()
        subtotal_inp = StringVar()
        services_inp = StringVar()
        tax_inp = StringVar()
        cost_inp = StringVar()
        Long_Black_Input_Price  = StringVar()
        Mocha_Input_Price  = StringVar()
        Macchiato_Input_Price  = StringVar()

        flat_White = Label(left, font=('arial', 16, 'bold'), text="Flat White",
                      bg='deep sky blue', bd=16, anchor='w')
        flat_White.grid(row=0, column=0, sticky=E)
        txt_flatWhite = Entry(left, font=('arial', 16, 'bold'), textvariable=Flat_White_Input_Price,
                          bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_flatWhite.grid(row=0, column=1)

        latte_Coffee = Label(left, font=('arial', 16, 'bold'), text="Latte",
                         bg='deep sky blue', bd=16, anchor='w')
        latte_Coffee.grid(row=1, column=0, sticky=E)
        txt_Sandwich = Entry(left, font=('arial', 16, 'bold'), textvariable=Latte_Input_Price,
                             bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_Sandwich.grid(row=1, column=1)

        cappuccino_Coffee = Label(left, font=('arial', 16, 'bold'), text="Cappuccino",
                       bg='deep sky blue', bd=16, anchor='w')
        cappuccino_Coffee.grid(row=2, column=0, sticky=E)
        txt_Cappuccino = Entry(left, font=('arial', 16, 'bold'), textvariable=Cappuccino_Input_Price ,
                           bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_Cappuccino.grid(row=2, column=1)

        espresso_Coffee = Label(left, font=('arial', 16, 'bold'), text="Espresso",
                       bg='deep sky blue', bd=16, anchor='w')
        espresso_Coffee.grid(row=3, column=0, sticky=E)
        txt_Espresso = Entry(left, font=('arial', 16, 'bold'), textvariable=Espresso_Input_Price ,
                           bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_Espresso.grid(row=3, column=1)

        longBlack_Coffee = Label(left, font=('arial', 16, 'bold'), text="Long Black",
                      bg='deep sky blue', bd=16, anchor='w')
        longBlack_Coffee.grid(row=4, column=0, sticky=E)
        txt_LongBlack = Entry(left, font=('arial', 16, 'bold'), textvariable=Long_Black_Input_Price ,
                          bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_LongBlack.grid(row=4, column=1)

        mocha_Coffee = Label(left, font=('arial', 16, 'bold'), text="Mocha",
                      bg='deep sky blue', bd=16, anchor='w')
        mocha_Coffee.grid(row=5, column=0, sticky=E)
        txt_Mocha = Entry(left, font=('arial', 16, 'bold'), textvariable=Mocha_Input_Price ,
                          bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_Mocha.grid(row=5, column=1)

        macchiato_Cofee = Label(left, font=('arial', 16, 'bold'), text="Macchiato",
                      bg='deep sky blue', bd=16, anchor='w')
        macchiato_Cofee.grid(row=0, column=2, sticky=E)
        txt_Macchiato = Entry(left, font=('arial', 16, 'bold'), textvariable=Macchiato_Input_Price ,
                          bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_Macchiato.grid(row=0, column=3)

        subtotal = Label(left, font=('arial', 16, 'bold'), text="Cost",
                         bg='deep sky blue', bd=16, anchor='w')
        subtotal.grid(row=1, column=2, sticky=E)
        txt_subtotal = Entry(left, font=('arial', 16, 'bold'), textvariable=subtotal_inp,
                             bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_subtotal.grid(row=1, column=3)

        services = Label(left, font=('arial', 16, 'bold'), text="Service Charge",
                         bg='deep sky blue', bd=16, anchor='w')
        services.grid(row=2, column=2, sticky=E)
        txt_services = Entry(left, font=('arial', 16, 'bold'), textvariable=services_inp,
                             bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_services.grid(row=2, column=3)

        tax = Label(left, font=('arial', 16, 'bold'), text="GST",
                    bg='deep sky blue', bd=16, anchor='w')
        tax.grid(row=3, column=2, sticky=E)
        txt_tax = Entry(left, font=('arial', 16, 'bold'), textvariable=tax_inp, bd=10,
                        bg='deep sky blue', insertwidth=4, justify='right')
        txt_tax.grid(row=3, column=3)

        cost = Label(left, font=('arial', 16, 'bold'), text="Total Tax",
                     bg='deep sky blue', bd=16, anchor='w')
        cost.grid(row=4, column=2, sticky=E)
        txt_cost = Entry(left, font=('arial', 16, 'bold'), textvariable=cost_inp,
                         bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_cost.grid(row=4, column=3)

        total = Label(left, font=('arial', 16, 'bold'), text="Total Cost",
                      bg='deep sky blue', bd=16, anchor='w')
        total.grid(row=5, column=2, sticky=E)
        txt_total = Entry(left, font=('arial', 16, 'bold'), textvariable=total_inp,
                          bg='deep sky blue', bd=10, insertwidth=4, justify='right')
        txt_total.grid(row=5, column=3)

        btn_total = Button(left, padx=16, pady=8, bd=16, fg="black", font=('arial', 14, 'bold'),
                           width=17, height=2, text="Total", bg='peach puff', command=ref)
        btn_total.grid(row=7, column=1)

        btn_reset = Button(left, padx=16, pady=8, bd=16, fg="black",
                           bg='deep pink', font=('arial', 14, 'bold'), width=17,
                           height=2, text="Reset", command=reset)
        btn_reset.grid(row=7, column=2)

        btn_exit = Button(left, padx=16, pady=8, bd=16, fg="black", font=('arial', 14, 'bold'),
                          width=17, height=2, text="Back to \n Previous Menu", bg='lightgreen',
                          command = lambda: controller.show_frame("choice_Menu"))
        btn_exit.grid(row=7, column=3)

        btn_bck = Button(left, padx=16, pady=8, bd=16, fg="black", font=('arial', 14, 'bold'),
                         width=17, height=2, text="Back to Login", bg='salmon',
                         command = lambda: controller.show_frame("login_Page"))
        btn_bck.grid(row=8, column=2)

class coffeeShop_PriceChange(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label10 = tk.Label(self)
        img = Image.open("pricing.jpg")
        img = img.resize((1500, 800), Image.ANTIALIAS)
        label10.img = ImageTk.PhotoImage(img)
        label10['image'] = label10.img
        label10.place(x=1, y=1)

        def update():
            f = open('value.txt', 'r')
            line = f.readlines()
            Flat_White_Price = float(line[0])
            Latte_Price = float(line[1])
            Cappuccino_Price = float(line[2])
            Espresso_Price = float(line[3])
            Long_Black_Price = float(line[4])
            Mocha_Price = float(line[5])
            Macchiato_Price = float(line[6])
            f.close()

            f2 = open('value.txt', 'w')
            try:
                CoF1 = float(Flat_White_Input_Price.get())
            except Exception as e:
                if Flat_White_Input_Price.get() != "":
                    mb.showinfo('Error', 'Incorrect Input')
                Flat_White_Input_Price.set("")
                f2.write(str(Flat_White_Price) + "\n")
            else:
                f2.write(str(CoF1) + "\n")

            try:
                CoS1 = float(Latte_Input_Price.get())
            except Exception as e:
                if Latte_Input_Price.get() != "":
                    mb.showinfo('Error', 'Incorrect Input')
                Latte_Input_Price.set("")
                f2.write(str(Latte_Price) + "\n")
            else:
                f2.write(str(CoS1) + "\n")

            try:
                CoB1 = float(Cappuccino_Input_Price.get())
            except Exception as e:
                if Cappuccino_Input_Price.get() != "":
                    mb.showinfo('Error', 'Incorrect Input')
                Cappuccino_Input_Price.set("")
                f2.write(str(Cappuccino_Price) + "\n")
            else:
                f2.write(str(CoB1) + "\n")

            try:
                CoD1 = float(Espresso_Input_Price.get())
            except Exception as e:
                if Espresso_Input_Price.get() != "":
                    mb.showinfo('Error', 'Incorrect Input')
                Espresso_Input_Price.set("")
                f2.write(str(Espresso_Price) + "\n")
            else:
                f2.write(str(CoD1) + "\n")

            try:
                CoP1 = float(Long_Black_Input_Price.get())
            except Exception as e:
                if Long_Black_Input_Price.get() != "":
                    mb.showinfo('Error', 'Incorrect Input')
                Long_Black_Input_Price.set("")
                f2.write(str(Long_Black_Price) + "\n")
            else:
                f2.write(str(CoP1) + "\n")

            try:
                CoP1 = float(Mocha_Input_Price.get())
            except Exception as e:
                if Mocha_Input_Price.get() != "":
                    mb.showinfo('Error', 'Incorrect Input')
                Mocha_Input_Price.set("")
                f2.write(str(Mocha_Price) + "\n")
            else:
                f2.write(str(CoP1) + "\n")

            try:
                CoC1 = float(Macchiato_Input_Price.get())
            except Exception as e:
                if Macchiato_Input_Price.get() != "":
                    mb.showinfo('Error', 'Incorrect Input')
                Macchiato_Input_Price.set("")
                f2.write(str(Macchiato_Price))
            else:
                f2.write(str(CoC1))

            mb.showinfo('Update Box', 'Successfully Updated')
            f2.close()

        def reset1():
            Flat_White_Input_Price.set("")
            Latte_Input_Price.set("")
            Cappuccino_Input_Price.set("")
            Espresso_Input_Price.set("")
            Long_Black_Input_Price.set("")
            Mocha_Input_Price.set("")
            Macchiato_Input_Price.set("")

        def printfn():
            f3 = open('value.txt', 'r')
            line2 = f3.readlines()
            Flat_White_Price = float(line2[0])
            Latte_Price = float(line2[1])
            Cappuccino_Price = float(line2[2])
            Espresso_Price = float(line2[3])
            Long_Black_Price = float(line2[4])
            Mocha_Price = float(line2[5])
            Macchiato_Price = float(line2[6])
            print("Flat White " + str(Flat_White_Price))
            print("Latte " + str(Latte_Price))
            print("Macchiato " + str(Macchiato_Price))
            print("Long Black " + str(Long_Black_Price))
            print("Mocha " + str(Mocha_Price))
            print("Cappucinno " + str(Cappuccino_Price))
            print("Espresso " + str(Espresso_Price))
            f3.close()

        label4 = Label(self, font=('arial', 34, 'bold'), text="Swannie's Coffee Shop Change Prices Menu",
                       fg="navy", bd=10)
        label4.place(x=435, y=4)

        Flat_White_Input_Price = StringVar()
        Latte_Input_Price = StringVar()
        Cappuccino_Input_Price = StringVar()
        Espresso_Input_Price = StringVar()
        Long_Black_Input_Price = StringVar()
        Mocha_Input_Price = StringVar()
        Macchiato_Input_Price = StringVar()

        flat_White = Label(self, font=('arial', 16, 'bold'), text="Flat White", bd=16, anchor='w')
        flat_White.grid(row=1, column=0, sticky=E)
        txt_flatWhite = Entry(self, font=('arial', 16, 'bold'), textvariable=Flat_White_Input_Price,
                              bd=10, insertwidth=4, bg="powder blue", justify='right')
        txt_flatWhite.grid(row=1, column=1)

        latte_Coffee = Label(self, font=('arial', 16, 'bold'), text="Latte", bd=16, anchor='w')
        latte_Coffee.grid(row=2, column=0, sticky=E)
        txt_Sandwich = Entry(self, font=('arial', 16, 'bold'), textvariable=Latte_Input_Price,
                             bd=10, insertwidth=4, bg="powder blue", justify='right')
        txt_Sandwich.grid(row=2, column=1)

        cappuccino_Coffee = Label(self, font=('arial', 16, 'bold'), text="Cappuccino", bd=16, anchor='w')
        cappuccino_Coffee.grid(row=3, column=0, sticky=E)
        txt_Cappuccino = Entry(self, font=('arial', 16, 'bold'), textvariable=Cappuccino_Input_Price,
                               bd=10, insertwidth=4, bg="powder blue", justify='right')
        txt_Cappuccino.grid(row=3, column=1)

        espresso_Coffee = Label(self, font=('arial', 16, 'bold'), text="Espresso", bd=16, anchor='w')
        espresso_Coffee.grid(row=4, column=0, sticky=E)
        txt_Espresso = Entry(self, font=('arial', 16, 'bold'), textvariable=Espresso_Input_Price,
                             bd=10, insertwidth=4, bg="powder blue", justify='right')
        txt_Espresso.grid(row=4, column=1)

        longBlack_Coffee = Label(self, font=('arial', 16, 'bold'), text="Long Black", bd=16, anchor='w')
        longBlack_Coffee.grid(row=5, column=0, sticky=E)
        txt_LongBlack = Entry(self, font=('arial', 16, 'bold'), textvariable=Long_Black_Input_Price,
                              bd=10, insertwidth=4, bg="powder blue", justify='right')
        txt_LongBlack.grid(row=5, column=1)

        mocha_Coffee = Label(self, font=('arial', 16, 'bold'), text="Mocha", bd=16, anchor='w')
        mocha_Coffee.grid(row=6, column=0, sticky=E)
        txt_Mocha = Entry(self, font=('arial', 16, 'bold'), textvariable=Mocha_Input_Price,
                              bd=10, insertwidth=4, bg="powder blue", justify='right')
        txt_Mocha.grid(row=6, column=1)

        macchiato_Cofee = Label(self, font=('arial', 16, 'bold'), text="Macchiato", bd=16, anchor='w')
        macchiato_Cofee.grid(row=7, column=0, sticky=E)
        txt_Macchiato = Entry(self, font=('arial', 16, 'bold'), textvariable=Macchiato_Input_Price,
                              bd=10, insertwidth=4, bg="powder blue", justify='right')
        txt_Macchiato.grid(row=7, column=1)

        btn_update = Button(self, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'),
                            width=18, text="Update New Prices", bg="peach puff", command=update)
        btn_update.grid(row=8, column=1)

        btn_reset1 = Button(self, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'),
                            width=18, text="Reset Prices", bg="pink", command=reset1)
        btn_reset1.grid(row=9, column=1)

        btn_exit1 = Button(self, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'),
                           width=18, text="Back to \nPrevious Menu", bg="lightgreen",
                           command = lambda: controller.show_frame("choice_Menu"))
        btn_exit1.grid(row=10, column=1)

        btn_print = Button(self, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'),
                           width=18, text="Print Prices", bg="yellow", command=printfn)
        btn_print.grid(row=9, column=2)

        btn_back = Button(self, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'),
                          width=18, text="Back to Login", bg="salmon",
                          command = lambda: controller.show_frame("login_Page"))
        btn_back.grid(row=9, column=3)

if __name__ == "__main__":
    self = CoffeeShop_Application()
    self.mainloop()
