import tkinter
from tkinter import *
import pytube #module needed to be able to use the YouTube module and download videos
from pytube import YouTube
from tkinter import messagebox, filedialog #module needed to use messagebox and filedialog

master = Tk()
master.geometry('500x500')
master.title('YouTube Video Download Wizard')
master.resizable(width=FALSE, height=FALSE)

#turns video link into a string
video_link = StringVar()

#turns download path into a string
download_path = StringVar()

#the title of the application
Label(master, text='YouTube Video Download Wizard', font='Helvetica 17 bold').place(x=60, y=10)

#the link to the video goes in the entry box
Label(master, text='Video Link: ', font='arial 15 bold').place(x=15, y=110)
Entry(master, textvariable=video_link, font='arial 15').place(x=15, y=140)

#the destination directory of the downloaded video
Label(master, text='Destination: ', font='arial 15 bold').place(x=15, y=170)
Entry(master, textvariable=download_path, font='arial 15').place(x=15, y=200)

#the name of the file that is being downloaded
Label(master, text='File Name: ', font='arial 15 bold').place(x=15, y=230)
Entry(master, font='arial 15').place(x=15, y=260)

#function to download video
def download_video():
    Youtube_Link = video_link.get()
    download_folder = download_path.get()
    getVideo = YouTube(Youtube_Link)
    videoStream = getVideo.streams.first()
    videoStream.download(download_folder)
    messagebox.showinfo('Download Complete!',
                        'Downloaded Video has been downloaded successfully and save in\n' + download_folder)

#button to download video
Button(master, text='Download', font='arial 15 bold', bg='Red', command=download_video).place(x=15, y=290)

#function to browse directories
def Browse_directory():
    download_directory = filedialog.askdirectory(initialdir='C:/Users/Crazy/Music/iTunes', title='Save Music')

    download_path.set(download_directory)

#button to browse directories
Button(master, text='Browse Directory', font='arial 13 bold', bg='Green', command=Browse_directory).place(x=245, y=200)

master.mainloop()
