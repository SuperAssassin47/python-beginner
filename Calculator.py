import tkinter
from tkinter import *

expression = ''

#Outputs numbers on button click
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

#Function to do arithmetic
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ''
    except:
        equation.set('Error')
        expression = ''

#Function to clear the display area
def clearall():
    global expression
    expression = ''
    equation.set('')

if __name__ == '__main__':
    root = Tk()
    root.geometry('480x220')
    root.title('Calculator')
    root.resizable(width=FALSE, height=FALSE)

    equation = StringVar()

    #Display area
    Entry(root, textvariable=equation, width=59).place(x=10, y=10)

    #Buttons 1 to 9
    Button(root, text='1', command=lambda: press(1), width=10).place(x=10, y=60)
    Button(root, text='2', command=lambda: press(2), width=10).place(x=100, y=60)
    Button(root, text='3', command=lambda: press(3), width=10).place(x=190, y=60)
    Button(root, text='4', command=lambda: press(4), width=10).place(x=10, y=100)
    Button(root, text='5', command=lambda: press(5), width=10).place(x=100, y=100)
    Button(root, text='6', command=lambda: press(6), width=10).place(x=190, y=100)
    Button(root, text='7', command=lambda: press(7), width=10).place(x=10, y=140)
    Button(root, text='8', command=lambda: press(8), width=10).place(x=100, y=140)
    Button(root, text='9', command=lambda: press(9), width=10).place(x=190, y=140)
    Button(root, text='0', command=lambda: press(0), width=10).place(x=100, y=180)

    #Arithmetic Buttons
    Button(root, text='+', command=lambda: press('+'), width=10).place(x=290, y=60)
    Button(root, text='-', command=lambda: press('-'), width=10).place(x=290, y=100)
    Button(root, text='/', command=lambda: press('/'), width=10).place(x=290, y=140)
    Button(root, text='*', command=lambda: press('*'), width=10).place(x=290, y=180)
    Button(root, text='=', command=equalpress, width=10).place(x=190, y=180)

    #Misc Buttons
    Button(root, text='%', command=lambda: press('%'), width=10).place(x=390, y=60)
    Button(root, text='3.142', command=lambda: press('3.142'), width=10).place(x=390, y=100)
    Button(root, text='.', command=lambda: press('.'), width=10).place(x=390, y=140)
    Button(root, text='<--', command=clearall, width=10).place(x=10, y=180)

    #Start application (GUI)
    root.mainloop()
