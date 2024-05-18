import tkinter
from tkinter import * 
from PIL import Image, ImageTk, ImageSequence 
import time
import pygame  #pip install pygame
from pygame import mixer
mixer.init()

root = tkinter.Tk()
root.geometry("700x700")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img
    img = Image.open(r"D:\VS code - F-end\1_Projects\jarvis-python\jarvis-python\robot.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0
    mixer.music.load(r"D:\VS code - F-end\1_Projects\jarvis-python\jarvis-python\mixkit-confirmation-tone-2867.wav")
    mixer.music.play()
    
    for img in ImageSequence.Iterator(img):
        img = img.resize((700,700))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.01)
    root.destroy()

play_gif()
root.mainloop()


