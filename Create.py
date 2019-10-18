import sys
import os
from tkinter import *
import mysql.connector

def Create():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="nissaar1307",
        database="dbpy"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO test (name, Bounty) VALUES (%s,%s)"
    val = (nameEntry.get(), BountyEntry.get())
    mycursor.execute(sql,val)
    mydb.commit()
    exit()

def Cancel():
    exit()

window = Tk()
window.title("Create")
window.geometry("300x100")

oneframe = Frame(window)
oneframe.grid(column=0,row=0)

twoframe = Frame(window)
twoframe.grid(column=0,row=1)


namelabel = Label(oneframe, text = "Name", width=15, bg="beige")
namelabel.pack(side = "left")

nameEntry = Entry(oneframe, background = "white", justify = "center")
nameEntry.pack(side= "right")

Bountylabel = Label(twoframe, text = "Bounty", width=15, bg="grey")
Bountylabel.pack(side = "left")

BountyEntry = Entry(twoframe, background = "white", justify = "center")
BountyEntry.pack(side= "right")

okButton = Button(window, width = "18", background = "white", foreground = "red", text = "OK", command = Create)
okButton.place(x=10, y=70)

cancelButton = Button(window, width = "18", background = "white", foreground = "red", text = "Cancel", command = Cancel)
cancelButton.place(x=160, y=70)

window.mainloop()
