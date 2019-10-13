import sys
import os
from tkinter import *
import mysql.connector

def Create():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",  #db password
        database="dbpy"
    )
    os.system('py C:/Users/username/Desktop/Python/Project/dbconnect.py')
    mycursor = mydb.cursor()
    sql = "INSERT INTO test (name, PhoneNo) VALUES (%s,%s)"
    val = (nameEntry.get(), phoneEntry.get())
    mycursor.execute(sql,val)
    mydb.commit()
    exit()

def Cancel():
    exit()

window = Tk()
window.title("Entry form")
window.geometry("300x100")

oneframe = Frame(window)
oneframe.grid(column=0,row=0)

twoframe = Frame(window)
twoframe.grid(column=0,row=1)


namelabel = Label(oneframe, text = "Name")
namelabel.pack(side = "left")

nameEntry = Entry(oneframe, background = "white", justify = "center")
nameEntry.pack(side= "right")

phonelabel = Label(twoframe, text = "Phone Number")
phonelabel.pack(side = "left")

phoneEntry = Entry(twoframe, background = "white", justify = "center")
phoneEntry.pack(side= "right")

okButton = Button(window, width = "18", background = "white", foreground = "red", text = "OK", command = Create)
okButton.place(x=10, y=70)

cancelButton = Button(window, width = "18", background = "white", foreground = "red", text = "Cancel", command = Cancel)
cancelButton.place(x=160, y=70)

window.mainloop()
