from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog

#main screen
master = Tk()
master.title ("Music Player")

#labels
Label (master, text = "Custom Music Player ", font=("Calibri",15), fg = "red").grid(sticky = "N", row = 0, padx = 120 )

