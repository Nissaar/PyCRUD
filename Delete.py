import os
from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nissaar1307",
    database="dbpy"
    )

def Delete():
    mycursor = mydb.cursor()
    sql = "DELETE FROM test WHERE ID = %s"
    val = (IDEntry.get())
    mycursor.execute(sql, val)
    mydb.commit()
    os.system('py C:/Users/nisgo/Desktop/Python/Project/Read.py')

def Cancel():
    exit()

window = Tk()
window.title("Delete")
window.geometry("250x90")

oneframe = Frame(window)
oneframe.grid(column=0,row=0)

IDlabel = Label(oneframe, text = "ID")
IDlabel.pack(side = "left")

IDEntry = Entry(oneframe, background = "white", justify = "center")
IDEntry.pack(side= "right")

DeleteButton = Button(window, width = "34", background = "white", foreground = "red", text = "Delete", command = Delete)
DeleteButton.grid(column=0, row=5)

cancelButton = Button(window, width = "34", background = "white", foreground = "red", text = "Cancel", command = Cancel)
cancelButton.grid(column=0, row=7)

window.mainloop()


