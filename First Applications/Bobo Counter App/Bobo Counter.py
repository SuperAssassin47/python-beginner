import tkinter
from tkinter import *

root = Tk()
root.geometry('300x300')
root.resizable(width=FALSE, height=FALSE)
root.title('Manual Bobo Counter')
number = IntVar()

Label(root, text='Bobo Counter', font='arial 17 bold').place(x=65, y=10)

Label(root, textvariable=number).grid(padx=137, pady=74)


def ping_bobo():
    number.set(number.get() + 1)


button = Button(root, text='+', font='arial 14 bold', bg='Black', fg='White', width=2, command=ping_bobo).place(x=100,
                                                                                                                y=100)


def remove_bobo():
    number.set(number.get() - 1)


btn2 = Button(root, text='-', font='arial 14 bold', bg='Black', fg='White', width=2, command=remove_bobo).place(x=150,
                                                                                                                y=100)

root.mainloop()
