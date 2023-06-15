import tkinter
from tkinter import *
from scapy.all import *

root = Tk()
root.geometry('500x500')
root.title('Device Hunter')
root.resizable(width=FALSE, height=FALSE)

Label(root, text='Device Hunter', font='Helvetica 20 bold').place(x=150, y=10)


def Hunt():
    packet = IP(dst = '192.168.1.1')
    hexdump(packet)
Button(root, text='Hunt', font='arial 14 bold', bg='Green', command=Hunt).place(x=215, y=70)

root.mainloop()
