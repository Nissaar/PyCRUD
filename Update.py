import sys
from tkinter import *
import mysql.connector
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="nissaar1307",
    database="dbpy"
    )


def Update():
    mycursor = mydb.cursor()
    sql = "UPDATE test SET name = (%s) WHERE ID = %s"
    sql1 = "UPDATE test SET Bounty = (%s) WHERE ID = %s"
    val = (nameEntry.get(),IDEntry.get())
    val1 = (BountyEntry.get(),IDEntry.get())
    mycursor.execute(sql, val)
    mycursor.execute(sql1, val1)
    mydb.commit()
    os.system('py C:/Users/nisgo/Desktop/Python/Project/Read.py')

def Cancel():
    exit()

window = Tk()
window.title("Update")
window.geometry("250x150")

oneframe = Frame(window)
oneframe.grid(column=0,row=0)

twoframe = Frame(window)
twoframe.grid(column=0,row=3)

threeframe = Frame(window)
threeframe.grid(column=0, row=4)

namelabel = Label(twoframe, text = "Name", width=8, bg="grey")
namelabel.pack(side = "left")

nameEntry = Entry(twoframe, background = "white", justify = "center")
nameEntry.pack(side= "right")

Bountylabel = Label(threeframe, text = "Bounty", width=8, bg="grey")
Bountylabel.pack(side = "left")

BountyEntry = Entry(threeframe, background = "white", justify = "center")
BountyEntry.pack(side= "right")

def fetchfromdb():
    mycursor = mydb.cursor()
    sql = "SELECT * FROM test WHERE ID = %s"
    val = (IDEntry.get(),)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for val in myresult:
        nameEntry.insert(0, val[1])
        BountyEntry.insert(0, val[2])

IDlabel = Label(oneframe, text = "ID", width=8, bg="grey")
IDlabel.pack(side = "left")

IDEntry = Entry(oneframe, background = "white", justify = "center")
IDEntry.pack(side= "right")

fetchButton = Button(window, width = "26", background = "white", foreground = "red", text = "Fetch", command = fetchfromdb)
fetchButton.grid(column=0, row=2, padx=33)


UpdateButton = Button(window, width = "26", background = "white", foreground = "red", text = "Update", command = Update)
UpdateButton.grid(column=0, row=5, padx=33)

cancelButton = Button(window, width = "26", background = "white", foreground = "red", text = "Cancel", command = Cancel)
cancelButton.grid(column=0, row=7, padx=33)

window.mainloop()

