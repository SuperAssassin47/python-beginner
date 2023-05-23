import tkinter
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mb
from PIL import Image, ImageTk
import moviepy
import moviepy.editor
import os

master = Tk()
master.geometry('500x500')
master.title('Video Convertor from MP4 to MP3')
master.resizable(width=FALSE, height=FALSE)

video_link = StringVar()
download_link = StringVar()

Label(master, text='Video Convertor from MP4 to MP3', font='Helvetica 17 bold').place(x=70, y=10)

Label(master, text='Video Link: ', font='arial 14 bold').place(x=30, y=100)
Entry(master, textvariable=video_link, font='arial 14', width=29).place(x=140, y=100)

def select_video():
    global filename, onlyfilename
    filename = filedialog.askopenfilename(initialdir="/", title="Choose MP4",filetypes=(("Text files", "*.Mp4*"), ("all files", "*.*")))
    onlyfilename = os.path.basename(filename)

Label(master, text='Select video (MP4):', font='arial 14 bold').place(x=30, y=170)
Button(master, text='Select Video', font='arial 14 bold', bg='Red', relief='raised', command=select_video).place(x=30, y=197)

def Browse_directory():
    download_directory = filedialog.askdirectory(initialdir='C:/Users/Crazy/Music/iTunes', title='Save Music')

    download_link.set(download_directory)

Label(master, text='Destination: ', font='arial 14 bold').place(x=30, y=270)
Entry(master, textvariable=download_link, width=24, font='arial 14').place(x=150, y=270)

Button(master, text='Browse Directory', font='arial 13 bold', bg='Green', command=Browse_directory).place(x=30, y=320)


def convert_to_mp3():
    movie = moviepy.editor.VideoFileClip(filename)
    audio=movie.audio

    aud_fname = ''
    for i in onlyfilename:
        if i == '.':
            break
        else:
            aud_fname = aud_fname + i
    print(aud_fname)
    audio.write_audiofile(f'{aud_fname}.mp3')
    mb.showinfo('Converted to MP3!', 'Video successfully converted to audio file!\n\nAudio file saved to File Manager')


Button(master, text='Convert to MP3', font='arial 18 bold', bg='Red', command=convert_to_mp3).place(x=30, y=370)

master.mainloop()