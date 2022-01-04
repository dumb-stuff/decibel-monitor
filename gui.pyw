import sounddevice as sd
import numpy as np
import tkinter

window = tkinter.Tk()
window.title("What am I doing in my life")
var = tkinter.StringVar()
title = tkinter.Label(window,font="Helvetica 12 bold",textvariable=var)
var.set(f"Volume is now {0}db")
duration = -1  # seconds

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(f"Volume is now {int(volume_norm)}db",end="\r")
    var.set(f"Volume is now {int(volume_norm)}db")

with sd.Stream(callback=print_sound):
    title.pack()
    window.mainloop()