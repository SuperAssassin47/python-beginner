import time
import tkinter
from tkinter import *
from random import shuffle

root = Tk()
root.title('funny')
root.geometry('500x500')
root.resizable(width=FALSE, height=FALSE)

colors = ['green', 'yellow', 'gold', 'orange', 'red']

def pressHere():
    new1 = Toplevel(root)
    new1.geometry('500x500')
    new1.title('dont panic')

    def change_color():
        label1.configure(fg='red')


    label1 = Label(new1, text="Don't Panic!!!", font='Helvetica 24 bold', fg='green')
    label3 = Label(new1, text='The US and NATO will handle everything!!!', font='Helvetica 14', ).place(x=60, y=100)
    label1.place(x=140, y=40)

    btn1 = Button(new1, text='Change color', font='Helvetica 18 bold', fg='blue', bg='red', padx=40, pady=20, command=change_color).place(x=120, y=170)



label0 = Label(root, text='In case of an emergency\nbetween Russia and the US...', font='Helvetica 24 bold', fg='red')
label2 = Label(root, text='WARNING: This may be a sensitive topic for some people!!!', font='Helvetica 10').place(x=80, y=190)
label0.place(x=30, y=50)

btn0 = Button(root, text='Press Here', font='Helvetica 18 bold', fg='blue', bg='red', padx=40, pady=20,
              command=pressHere)
btn0.place(x=130, y=230)

root.mainloop()
