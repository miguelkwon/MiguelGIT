from tkinter import *
import tkinter as tk
import tkinter.ttk
import tkinter.font
import os




window = Tk()
window.title("check box test")

CheckVar1=tk.IntVar()
CheckVar2=IntVar()

tk.Checkbutton(window,text="Music",variable=CheckVar1).grid(row=99,sticky='w')
# c2=Checkbutton(window,text="Video",variable=CheckVar2)

# c1.grid(row=0,column=1, sticky="w")

# c1.pack()
# c2.pack()

window.geometry('800x500+220+200')
window.mainloop()


