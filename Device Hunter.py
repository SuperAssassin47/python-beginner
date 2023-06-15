#Import the necessary modules####
import tkinter                  #
from tkinter import *           #
from scapy.all import *         #
#################################

#The main crux of the application############
root = Tk()                                 #
root.geometry('500x500')                    #
root.title('Device Hunter')                 #
root.resizable(width=FALSE, height=FALSE)   #
#############################################

#The title of the application
Label(root, text='Device Hunter', font='Helvetica 20 bold').place(x=150, y=10)


#Function for "Hunt" button
def Hunt():
    packet = IP(dst = '192.168.1.1')
    
    #Outputs the raw bits of the packet, in this case, the raw bits of the Ethernet packet using a destination IP Address
    hexdump(packet)

#Button to sniff the Ethernet packet and "hexdump" (output) the raw bits of it
Button(root, text='Hunt', font='arial 14 bold', bg='Green', command=Hunt).place(x=215, y=70)

#Start the GUI
root.mainloop()
