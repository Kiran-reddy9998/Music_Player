import pygame
from tkinter import *
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os
from numpy.ma import var

music_player = tkr.Tk()
music_player.title('Music Player')
music_player.geometry('950x450')
music_player.iconbitmap("windows_media_player.ico")

directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = Listbox(music_player, font='Helvetica 12 bold', bg='yellow', selectmode=tkr.SINGLE, width=27, height=21)

for item in song_list:
    if '.mp3' in item:
        pos = 0
        play_list.insert(pos, item)
        pos += 1
pygame.init()
pygame.mixer.init()

file_label = Label(music_player, text='#  Change the world by being YOUESELF  # ', font='Helvetica 12 bold')
file_label.place(x=190, y=5)


def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def stop():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


def vol_bar(val):
    volume = int(val) / 10
    pygame.mixer.music.set_volume(volume)


Button_1 = tkr.Button(music_player, width=4, height=1, font='Helvetica 12 bold', text='Play', command=play, bg='green',
                      fg='white')
Button_2 = tkr.Button(music_player, width=4, height=1, font='Helvetica 12 bold', text='Stop', command=stop, bg='green',
                      fg='white')
Button_3 = tkr.Button(music_player, width=6, height=1, font='Helvetica 12 bold', text='Pause', command=pause,
                      bg='green', fg='white')
Button_4 = tkr.Button(music_player, width=7, height=1, font='Helvetica 12 bold', text='Unpause', command=unpause,
                      bg='green', fg='white')
scale_1 = Scale(music_player, from_=0, to=10, orient=HORIZONTAL, command=vol_bar)
scale_1.place(x=55, y=200)
lbl_1 = Label(music_player, text='Volume:', font='Helvetica 15 bold')
lbl_1.place(x=30, y=170)
lbl_1 = Label(music_player, text='+', font='Helvetica 19 bold')
lbl_1.place(x=150, y=250)
lbl_1 = Label(music_player, text='-', font='Helvetica 22 bold')
lbl_1.place(x=50, y=250)

var = tkr.StringVar()
song_title = tkr.Label(music_player, font='Helvetica 12 bold', textvariable=var)
song_title.place(x=295, y=130)
Button_1.place(x=365, y=300)
Button_2.place(x=365, y=400)
Button_3.place(x=295, y=350)
Button_4.place(x=405, y=350)
play_list.place(x=690, y=10)


music_player.mainloop()
