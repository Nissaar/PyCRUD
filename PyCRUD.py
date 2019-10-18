import sys
import os
from tkinter import *

def Create():
    os.system('py C:/Users/nisgo/Desktop/Python/Project/Create.py')

def Read():
    os.system('py C:/Users/nisgo/Desktop/Python/Project/Read.py')

def Update():
    os.system('py C:/Users/nisgo/Desktop/Python/Project/Update.py')

def DeleteRow():
    os.system('py C:/Users/nisgo/Desktop/Python/Project/Delete.py')

window = Tk()
window.title("PyDB App")
window.geometry("400x500")

insertButton = Button(window, height = "15", width = "25", text = "Create", background = "grey", foreground = "red", command = Create)
insertButton.place(x=10, y=10)

readButton = Button(window, height = "15", width = "25", text = "Read", background = "grey", foreground = "red", command = Read)
readButton.place(x=200, y=10)

updateButton = Button(window, height = "15", width = "25", text = "Update", background = "grey", foreground = "red", command = Update)
updateButton.place(x=10, y=250)

deleteButton = Button(window, height = "15", width = "25", text = "Delete", background = "grey", foreground = "red", command = DeleteRow)
deleteButton.place(x=200, y=250)

window.mainloop()

