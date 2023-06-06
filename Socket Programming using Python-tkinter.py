import tkinter
from tkinter import *
import socket

root = Tk()
root.geometry('400x400')
root.title('Device Listener')
root.resizable(width=FALSE, height=FALSE)

#create the socket
s = socket.socket()

Label(root, text='Enter a message: ', font='arial 14 bold').place(x=10, y=40)

Entry(root, font='arial 14', width=19).place(x=170, y=40)

#function for the button
def socket():
    print('Socket Created!')
    
    #searches for open ports between port 1 and port 200
    port = range(1, 200)
    
    #lists all open ports
    open_ports = []
    
    #function to bind socket to most recent port
    def attach_port(port, result=1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCKSTREAM)
            s.settimeout(0.3)
            r = s.connect_ex((port))
            if r == 0:
                result = r
                s.close()
        except Exception as e:
            pass
        return result

    for port in port:
        response = attach_port(port)
        if response == 1:
            open_ports.append(port)
            
    #if statement to list all open ports and bind socket to the most recent port
    if open_ports:
        print('Ports that are open: ')
        print(sorted(open_ports))
        s.bind(('', port))
        print('Socket binded to %s' % port)
        s.close()
    else:
        #outputs if there are no ports open
        print('No ports are open!')
        
    #function to listen to a binded port and connects to it
    def port_listener():
        c, addr = s.accept()
        print('Retrieved connection from ', addr)
        
        c.send(b'Connected! Thank you!')

        c.close()

#The button to "Send a Message" to someone
Button(root, text='Send Message', font='arial 14 bold', bg='Green', command=socket).place(x=110, y=100)

#start the GUI
root.mainloop()
