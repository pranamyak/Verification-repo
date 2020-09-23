import pygame
from tkinter import *
import os

music = Tk()
music.title("Audio Player")
music.geometry("200x400")
music.configure(background ="black")

os.chdir("songs")
songlist = os.listdir()



playlist = Listbox(music , highlightcolor = "blue" , bg = "light sea green" , selectmode = SINGLE)
i =0
for x in songlist :
    playlist.insert(i,x)
    i+=1

pygame.init()
pygame.mixer.init()

def ExitPlayer():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()


a,b = 0,0
bplay = True
once = True
def Play_Pause():
    global bplay,a,b,once

    if once == True :
        a = playlist.get(ACTIVE)
        once = False
    else :
        b = playlist.get(ACTIVE)
        once = True


    if bplay == True and a==b:
        pygame.mixer.music.pause()
        bplay = False
    elif bplay==False and a==b:
        pygame.mixer.music.unpause()
        bplay = True
    elif a!= b :
        pygame.mixer.music.load(playlist.get(ACTIVE))
        var.set(playlist.get(ACTIVE))
        pygame.mixer.music.play()


def nextnow():
    current = playlist.get(ACTIVE)
    length = len(songlist)
    p = songlist.index(current)
    p = (p+1)%7
    playlist.activate(p)
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()


def onebefore():
    current = playlist.get(ACTIVE)
    length = len(songlist)
    p = songlist.index(current)
    p = (p -1+7) % 7
    playlist.activate(p)
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()
    

def end():
    music.destroy()

b1 = Button(music , width = 25 , text ="Quit" ,fg = "blue" , bg ="cyan", command = end)
b2 = Button(music , width = 25 , text ="STOP and Play from beginning" , fg = "red" , bg = "yellow" , command = ExitPlayer)
b3 = Button(music , width = 25 , text ="Play/pause" ,fg = "blue" , bg ="cyan" , command = Play_Pause)
b4 = Button(music , width = 25 , text ="Play the next song" , fg = "red" , bg = "yellow" , command = nextnow)
b5 = Button(music , width = 25 , text ="Play the previous song" ,fg = "blue" , bg ="cyan", command = onebefore)


var = StringVar()
l1 = Label(music , text = "Select the song from the playlist")

name = Label(music,bg = "black" , fg = "red" ,textvariable = var)



name.pack()
b3.pack(fill ="x")
b4.pack(fill ="x")
b5.pack(fill ="x")
b2.pack(fill ="x")
b1.pack(fill ="x")
l1.pack(fill= "x")
playlist.pack(fill= "both" , expand = "yes")

b1.pack(fill ="x")


music.mainloop()
"""
def Play():
    pygame.mixer.music.load(playlist.get(ACTIVE))
    var.set(playlist.get(ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(volumelevel.get())
b1 = Button(music , width = 25, text = "PLAY" , command = Play)
b1.grid(column=0,row=2)

bplay = True


def Play_Pause():
    global bplay
    if bplay == True:
        pygame.mixer.music.pause()
        bplay = False
    else:

        pygame.mixer.music.unpause()
        bplay = True
"""