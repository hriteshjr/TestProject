from tkinter import*
import pygame

root = Tk()
root.title("Music Player (Programming)")
root.iconbitmap("D:\\logo.png")
root.geometry ('500x300')

pygame.mixer.init()

#create playlist Box
song_box = Listbox(root, bg = 'black', fg = 'green', width=60)
song_box.pack(pady=20)

root.mainloop()