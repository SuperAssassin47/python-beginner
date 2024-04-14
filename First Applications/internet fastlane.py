import webbrowser
from tkinter import *
import sys, os

application_path = os.path.dirname(sys.executable)

root = Tk()
root.title('Internet Fastlane')
root.geometry('1000x1000')

def cambridgeregionalcollege():
    webbrowser.open('https://www.camre.ac.uk/')

def outlook():
    webbrowser.open('https://outlook.live.com/mail/0/')

def google():
    webbrowser.open('https://www.google.co.uk/')

def instagram():
    webbrowser.open('https://www.instagram.com/')

def hpwolfsecurity():
    webbrowser.open('https://www.hp.com/gb-en/security/endpoint-security-solutions.html')

def facebook():
    webbrowser.open('https://en-gb.facebook.com/')

def twitter():
    webbrowser.open('https://twitter.com/i/flow/login')

def linkedin():
    webbrowser.open('https://uk.linkedin.com/')

def discord():
    webbrowser.open('https://discord.com/')

def codecademy():
    webbrowser.open('https://www.codecademy.com/')

def ubisoft():
    webbrowser.open('https://www.ubisoft.com/en-gb/')


def fandom():
    webbrowser.open('https://www.fandom.com/')


def youtube():
    webbrowser.open('https://www.youtube.com/')


def stackoverflow():
    webbrowser.open('https://stackoverflow.com/')


def github():
    webbrowser.open('https://github.com/')


def ubisoftconnect():
    webbrowser.open('https://ubisoftconnect.com/en-GB/')


def codewars():
    webbrowser.open('https://www.codewars.com/users/sign_in')


def amazon():
    webbrowser.open('https://www.amazon.co.uk/')


def w3schools():
    webbrowser.open('https://www.w3schools.com/')


def programiz():
    webbrowser.open('https://www.programiz.com/')


def gmail():
    webbrowser.open('https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&ifkv=AeAAQh4WtQT9xkpoUGKtqdI-qSvuPEqT8S_k53QrAt3o6qUk_7ePshBB2nRzKKGzxjva8GXKlWHmoA&flowName=GlifWebSignIn&flowEntry=ServiceLogin')


def protonmail():
    webbrowser.open('https://proton.me/')


def hp():
    webbrowser.open('https://www.hp.com/us-en/home.html')

def corbettmaths():
    webbrowser.open('https://corbettmaths.com/')

Label(root, text='Internet Fastlane!', font='Helvetica 25 bold').pack()

mycambridgeregionalcollege = Button(root, text='CRC', command=cambridgeregionalcollege, font='LUCIDA 10 bold').pack()

myoutlook = Button(root, text='Outlook', command=outlook, font='LUCIDA 10 bold').pack()

mygoogle = Button(root, text='Google', command=google, font='LUCIDA 10 bold').pack()

myinstagram = Button(root, text='Instagram', command=instagram, font='LUCIDA 10 bold').pack()

myhpwolfsecurity = Button(root, text='HP Wolf Security', command=hpwolfsecurity, font='LUCIDA 10 bold').pack()

myfacebook = Button(root, text='FaceBook', command=facebook, font='LUCIDA 10 bold').pack()

mytwitter = Button(root, text='Twitter', command=twitter, font='LUCIDA 10 bold').pack()

mylinkedin = Button(root, text='LinkedIn', command=linkedin, font='LUCIDA 10 bold').pack()

mydiscord = Button(root, text='Discord', command=discord, font='LUCIDA 10 bold').pack()

mycodecademy = Button(root, text='Codecademy', command=codecademy, font='LUCIDA 10 bold').pack()

myubisoft = Button(root, text='Ubisoft', command=ubisoft, font='LUCIDA 10 bold').pack()

myfandom = Button(root, text='Fandom', command=fandom, font='LUCIDA 10 bold').pack()

myyoutube = Button(root, text='YouTube', command=youtube, font='LUCIDA 10 bold').pack()

mystackoverflow = Button(root, text='StackOverflow', command=stackoverflow, font='LUCIDA 10 bold').pack()

mygithub = Button(root, text='GitHub', command=github, font='LUCIDA 10 bold').pack()

myubisoftconnect = Button(root, text='Ubisoft Connect', command=ubisoftconnect, font='LUCIDA 10 bold').pack()

mycodewars = Button(root, text='CodeWars', command=codewars, font='LUCIDA 10 bold').pack()

myamazon = Button(root, text='Amazon', command=amazon, font='LUCIDA 10 bold').pack()

myw3schools = Button(root, text='W3Schools', command=w3schools, font='LUCIDA 10 bold').pack()

myprogamiz = Button(root, text='Programiz', command=programiz, font='LUCIDA 10 bold').pack()

mygmail = Button(root, text='G-mail', command=gmail, font='LUCIDA 10 bold').pack()

myprotonmail = Button(root, text='ProtonMail', command=protonmail, font='LUCIDA 10 bold').pack()

myhp = Button(root, text='HP', command=hp, font='LUCIDA 10 bold').pack()

mycorbettmaths = Button(root, text='CorbettMaths', command=corbettmaths, font='LUCIDA 10 bold').pack()
root.mainloop()
