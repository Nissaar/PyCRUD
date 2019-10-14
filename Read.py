import sys
from tkinter import *
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password", #db password
    database="dbpy"
    )

mycursor = mydb.cursor()

sql = "SELECT * FROM test"
mycursor.execute(sql)
myresult = mycursor.fetchall()

window = Tk()
window.title("View Database")
window.geometry("500x500")

frame = Frame(window)
frame.pack()

tree = ttk.Treeview(frame, columns = (1,2,3), height = 25, show = "headings")
tree.pack(side = 'left')

tree.heading(1, text="ID")
tree.heading(2, text="Name")
tree.heading(3, text="Phone No")

tree.column(1, width = 159)
tree.column(2, width = 159)
tree.column(3, width = 159)

scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scroll.pack(side = 'right', fill = 'y')

tree.configure(yscrollcommand=scroll.set)

for val in myresult:
    tree.insert('', 'end', values = (val[0], val[1], val[2]))


window.mainloop()

