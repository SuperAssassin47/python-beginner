import tkinter
from tkinter import *
from tkinter import messagebox as mb
import pyautogui
root = Tk()
root.geometry('500x500')
root.title('Alert System')
root.resizable(width=FALSE, height=FALSE)

Label(root, text='Alert System', font='Helvetica 20 bold').place(x=160, y=10)

def send_alert():
    mb.showerror('Alert', 'NUKE INBOUND! TAKE SHELTER IMMEDIATELY!')

Button(root, text='Send Alert', font='arial 14 bold', bg='Red', command=send_alert).place(x=187, y=130)
root.mainloop()
