import os
import tkinter as tk
from tkinter import messagebox as msgbox


window=tk.Tk()

def startHotSpot():
   msgbox.showinfo( "Hello Python", "Hello World")

B = tk.Button(window, text ="Start Hotspot", command = startHotSpot)


greeting = tk.Label(text="Hello, Tkinter")

greeting.pack()
B.pack()
window.mainloop()


print("app ended ...")
os.system('clear')
