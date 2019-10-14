import sys
import os
from tkinter import *

def EntryForm():
    os.system('py C:/Users/username/Desktop/Python/Project/entryform.py')

def ViewDB():
    os.system('py C:/Users/username/Desktop/Python/Project/viewDB.py')

def EditDB():
    os.system('py C:/Users/username/Desktop/Python/Project/Edit.py')

def DeleteRow():
    os.system('py C:/Users/username/Desktop/Python/Project/Delete.py')

window = Tk()
window.title("PyDB App")
window.geometry("400x500")

insertButton = Button(window, height = "15", width = "25", text = "Entry form", background = "white", foreground = "red", command = EntryForm)
insertButton.place(x=10, y=10)

readButton = Button(window, height = "15", width = "25", text = "View DB", background = "white", foreground = "red", command = ViewDB)
readButton.place(x=200, y=10)

updateButton = Button(window, height = "15", width = "25", text = "Edit", background = "white", foreground = "red", command = EditDB)
updateButton.place(x=10, y=250)

deleteButton = Button(window, height = "15", width = "25", text = "Delete", background = "white", foreground = "red", command = DeleteRow)
deleteButton.place(x=200, y=250)

window.mainloop()

