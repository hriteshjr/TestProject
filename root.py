from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube #pip install pytube3



root = Tk()
root.title("YTD Downloader")
root.geometry("350x400") #set window
root.columnconfigure(0,weight=1)#set all content in center.