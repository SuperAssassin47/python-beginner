#Import the necessary modules
import tkinter                       
from tkinter import *                
from tkinter import messagebox as mb 
import pyautogui                     


#The main crux of the application 
root = Tk()                               
root.geometry('500x500')                  
root.title('Alert System')                
root.resizable(width=FALSE, height=FALSE)


#The title on the client area of the application
Label(root, text='Alert System', font='Helvetica 20 bold').place(x=160, y=10)

#Function for the "Send Alert" button
def send_alert():
    mb.showinfo('Hello', "I'm an alert")

#Button to "Send Alert" (output a messagebox alerting the user of a message)
Button(root, text='Send Alert', font='arial 14 bold', bg='Red', command=send_alert).place(x=187, y=130)

#Start the GUI
root.mainloop()
