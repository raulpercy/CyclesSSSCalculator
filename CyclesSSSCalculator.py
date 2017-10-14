#Simple Calculator for Principled Shader Node 
#Blender 2.79
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *
win = tk.Tk()
win.title("SSS Calculator")
def getRGB():
	rgb = askcolor()
	print(rgb)
button = ttk.Button(win, text = "...", command=getRGB)
button.grid(column=0,row=0)
win.mainloop()