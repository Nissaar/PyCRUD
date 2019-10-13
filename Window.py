import sys
import os
from tkinter import *

def EntryForm():
    os.system('py C:/Users/nisgo/Desktop/Python/Project/entryform.py')

window = Tk()
window.title("PyDB App")
window.geometry("1000x1000")

insertButton = Button(window, text = "Entry form", background = "white", foreground = "red", command = EntryForm)
insertButton.place(x=10, y=10)

window.mainloop()

