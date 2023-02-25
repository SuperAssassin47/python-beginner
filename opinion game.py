import tkinter
from tkinter import *

root = Tk()
root.title('game')
root.geometry('400x400')

label1 = Label(root, text='Opinion Game', font='Helvetica 18 bold', fg='blue').place(x=110, y=10)
label2 = Label(root, text='There are no right or wrong answers.\nGood luck and may the fates guide you! ;)',
               font='Helvetica 12', fg='blue').place(x=50, y=70)

def play():
    new1 = Toplevel(root)
    new1.geometry('400x400')

    label3 = Label(new1, text='Who would win...?', font='Helvetica 18 bold', fg='green').place(x=90, y=10)

    def NATO():
        new2 = Toplevel(new1)
        new2.geometry('300x300')

        label4 = Label(new2, text='You have chosen NATO...', font='Helvetica 12 bold', fg='gold').place(x=50, y=10)
        label5 = Label(new2, text='Thanks for playing!', font='arial 12', fg='gold').place(x=80, y=50)

    def Russia():
        new3 = Toplevel(new1)
        new3.geometry('300x300')

        label6 = Label(new3, text='You have chosen Russia...', font='Helvetica 12 bold', fg='gold').place(x=50, y=10)
        label7 = Label(new3, text='Thanks for playing!', font='arial 12', fg='gold').place(x=80, y=50)

    btn2 = Button(new1, text='NATO', font='arial 12 bold', bg='blue', fg='red', padx=40, pady=20, command=NATO).place(x=50, y=190)
    btn3 = Button(new1, text='Russia', font='arial 12 bold', bg='red', fg='blue', padx=40, pady=20, command=Russia).place(x=190, y=190)


btn1 = Button(root, text='Play', font='arial 18', padx=20, pady=10, command=play).place(x=145, y=170)


root.mainloop()